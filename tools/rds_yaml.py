"""A tiny parser for the restricted YAML subset used by regulated-dev-skills.

Allowed: nested maps by indentation, block lists of scalars ("- x"), flow lists
of scalars ("[a, b]"), plain or double-quoted strings, null, booleans, integers.
Rejected: anchors, tags, block scalars, flow maps, tabs, duplicate keys.

Standard library only. Works on Python 3.9 and later.
"""
import re


class YamlError(Exception):
    def __init__(self, line, msg):
        super().__init__("line %s: %s" % (line, msg))
        self.line = line
        self.msg = msg


def _strip_comment(s):
    out = []
    quoted = False
    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\" and quoted and i + 1 < len(s):
            out.append(c)
            out.append(s[i + 1])
            i += 2
            continue
        if c == '"':
            quoted = not quoted
        if c == "#" and not quoted and (i == 0 or s[i - 1] in " \t"):
            break
        out.append(c)
        i += 1
    return "".join(out).rstrip()


def _split_flow(s, line):
    parts, cur, quoted, i = [], [], False, 0
    while i < len(s):
        c = s[i]
        if c == "\\" and quoted and i + 1 < len(s):
            cur.append(c)
            cur.append(s[i + 1])
            i += 2
            continue
        if c == '"':
            quoted = not quoted
        if c == "," and not quoted:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(c)
        i += 1
    if quoted:
        raise YamlError(line, "unterminated quote in list")
    parts.append("".join(cur))
    return parts


def _scalar(tok, line):
    t = tok.strip()
    if t == "":
        return None
    if t[0] == '"':
        if len(t) < 2 or t[-1] != '"':
            raise YamlError(line, "unterminated quoted string")
        inner = t[1:-1]
        return inner.replace('\\"', '"').replace("\\\\", "\\")
    if t[0] == "[":
        if t[-1] != "]":
            raise YamlError(line, "unterminated list")
        inner = t[1:-1].strip()
        if not inner:
            return []
        return [_scalar(x, line) for x in _split_flow(inner, line)]
    if t[0] in "{&*|>!%@`":
        raise YamlError(line, "not allowed in the YAML subset: %r" % t[0])
    if t in ("null", "~"):
        return None
    if t == "true":
        return True
    if t == "false":
        return False
    if re.match(r"^-?\d+$", t):
        return int(t)
    return t


def _is_item(text):
    return text == "-" or text.startswith("- ")


def _block(items, i, ind):
    if _is_item(items[i][1]):
        lst = []
        while i < len(items) and items[i][0] == ind and _is_item(items[i][1]):
            rest = items[i][1][1:].strip()
            if rest == "":
                raise YamlError(items[i][2], "nested lists of maps are not allowed")
            lst.append(_scalar(rest, items[i][2]))
            i += 1
        return lst, i
    d = {}
    while i < len(items) and items[i][0] == ind:
        text, n = items[i][1], items[i][2]
        m = re.match(r"^([A-Za-z0-9_.-]+):(?:\s+(.*))?$", text)
        if not m:
            raise YamlError(n, "expected 'key: value'")
        key, val = m.group(1), m.group(2)
        if key in d:
            raise YamlError(n, "duplicate key %r" % key)
        i += 1
        if val is None or val.strip() == "":
            if i < len(items) and items[i][0] > ind:
                sub, i = _block(items, i, items[i][0])
                d[key] = sub
            else:
                d[key] = None
        else:
            d[key] = _scalar(val, n)
    if i < len(items) and items[i][0] > ind:
        raise YamlError(items[i][2], "unexpected indentation")
    return d, i


def parse(text):
    items = []
    for n, raw in enumerate(text.splitlines(), 1):
        lead = raw[: len(raw) - len(raw.lstrip())]
        if "\t" in lead:
            raise YamlError(n, "tabs are not allowed")
        s = _strip_comment(raw)
        if not s.strip():
            continue
        ind = len(s) - len(s.lstrip(" "))
        items.append((ind, s.strip(), n))
    if not items:
        return {}
    val, i = _block(items, 0, items[0][0])
    if i != len(items):
        raise YamlError(items[i][2], "unexpected indentation")
    return val


def split_frontmatter(text):
    """Return (frontmatter_text, body_text, frontmatter_line_count) or raise."""
    if not text.startswith("---\n"):
        raise YamlError(1, "file must start with '---'")
    end = text.find("\n---\n", 3)
    if end == -1:
        if text.rstrip().endswith("\n---"):
            end = text.rstrip().rfind("\n---")
        else:
            raise YamlError(1, "frontmatter is not closed with '---'")
    fm = text[4:end]
    body = text[end + 5:]
    return fm, body, fm.count("\n") + 2
