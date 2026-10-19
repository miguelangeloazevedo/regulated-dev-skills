#!/usr/bin/env python3
"""regulated-dev-skills validator. Standard library only, Python 3.9 or later.

  validate.py repo [--root DIR]               check the skills repository itself
  validate.py records DIR [--roles F] [--project F] [--report] [--release]
                                              check a project's records
  validate.py project FILE                    check the project block
  validate.py hash FILE                       print a record's revision hash
  validate.py schemas [--write|--check]       derive or check schemas/*.json

Exit status is 1 when any error is found. Warnings never fail the run, except with
--release, which turns release blockers (stale or suspect approvals, linked but
unverified requirements, test cases without a result, undecided class while IEC 62304
is claimed, SOUP without an evaluated anomaly list at class B and C) into errors.
"""
import argparse
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rds_yaml import YamlError, parse, split_frontmatter  # noqa: E402

# ----------------------------------------------------------------- constants
GROUPS = ["gates", "lifecycle", "regulated", "extraction"]
INVOCATIONS = ["model", "typed"]
SKILL_STATUS = ["draft", "reviewed", "deprecated"]
BACKENDS = ["standalone", "jira", "qity", "notion"]
CEILING = {"standalone": 2, "jira": 2, "qity": 2, "notion": 0}
JURISDICTIONS = ["eu", "us"]

TYPES = {"vrp": "VRP", "rmr": "RMR", "cls": "CLS", "plan": "PLAN", "cr": "CR", "prb": "PRB", "rev": "REV", "rel": "REL", "un": "UN", "sys": "SYS", "sw": "SW", "spec": "SPEC", "tc": "TC", "tr": "TR",
         "haz": "HAZ", "rc": "RC", "soup": "SOUP", "find": "FIND", "dec": "DEC", "bl": "BL"}
PREFIX_TO_TYPE = {v: k for k, v in TYPES.items()}
RECORD_STATUS = ["draft", "in_review", "approved", "superseded", "obsolete"]
CLAIMS = ["observed", "inferred", "proposed"]
ORIGINS = ["authored", "extraction"]
VERIFIER_KINDS = ["human", "other_family", "same_family_fresh"]
OUTCOMES = ["pass", "fail", "blocked"]
BLOCKED_KINDS = ["content", "scope", "timing"]

# link field -> {source type: [allowed target types]}   ("*" means any)
LINKS = {
    "derives_from": {"sys": ["un"], "sw": ["sys"]},
    "specifies": {"spec": ["sw"]},
    "verifies": {"tc": ["sys", "sw", "spec", "rc"]},
    "validates": {"tc": ["un"]},
    "result_of": {"tr": ["tc"]},
    "mitigates": {"rc": ["haz"]},
    "implements": {"sw": ["rc"], "spec": ["rc"]},
    "relates_to": {"find": ["*"], "prb": ["*"], "rev": ["*"]},
    "addresses": {"cr": ["prb", "find"]},
    "releases": {"rel": ["bl"]},
    "supersedes": {t: ["same"] for t in TYPES},
}
REQUIRED_SECTIONS = {
    "cls": ["Qualification", "Classification", "Software safety class", "Overlays"],
    "plan": ["Stages and reviews", "Verification and validation", "Risk management", "Configuration management"],
    "haz": ["Hazard", "Sequence of events", "Hazardous situation", "Harm"],
    "rc": ["Control", "Mechanism"],
    "tc": ["Procedure", "Expected result"],
    "tr": ["Result"],
    "cr": ["Change", "Reason", "Impact"],
    "prb": ["Observed", "Safety relevance"],
    "rev": ["Design under review", "Read-list", "Findings", "Statement"],
    "rel": ["Baseline", "Decision"],
    "soup": ["Item", "Requirements", "Anomaly list"],
    "rmr": ["Plan", "Overall residual risk", "Benefit-risk", "Production and post-production"],
    "vrp": ["Scope", "Results", "Conclusion"],
    "un": ["Statement", "Rationale", "Validation method"],
    "sys": ["Statement", "Rationale", "Acceptance criteria"],
    "sw": ["Statement", "Rationale", "Acceptance criteria"],
    "spec": ["Statement", "Rationale", "Acceptance criteria"],
}
SKILL_SECTIONS = ["Reads", "Process", "Anti-patterns and their tells", "Refuses", "Writes", "Done when", "See also"]
ROLES = ["chain step", "gate", "run-once setup", "runs inside the chain", "periodic", "standalone"]
DOCS_REQUIRED = ["What it does", "When to reach for it", "It's working if", "Where it fits"]
DOCS_ORDER = ["What it does", "When to reach for it", "Prerequisites", "*", "Common questions", "It's working if", "Where it fits"]
EM_DASH = "\u2014"

errors = []
warnings = []


def err(code, path, msg):
    errors.append((code, path, msg))


def warn(code, path, msg):
    warnings.append((code, path, msg))


def rel(path, root):
    try:
        return os.path.relpath(path, root)
    except ValueError:
        return path


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


# ------------------------------------------------------------------- schemas
def schema_docs():
    skill = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "regulated-dev-skills skill frontmatter (derived from tools/validate.py)",
        "type": "object",
        "required": ["name", "description", "metadata"],
        "properties": {
            "name": {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$", "maxLength": 64},
            "description": {"type": "string", "maxLength": 250},
            "disable-model-invocation": {"type": "boolean"},
            "argument-hint": {"type": "string"},
            "metadata": {
                "type": "object",
                "required": ["group", "invocation", "role", "leading_word", "neighbours", "status", "reviewed_by", "reviewed_on", "as_of", "sources"],
                "properties": {
                    "group": {"enum": GROUPS},
                    "invocation": {"enum": INVOCATIONS},
                    "role": {"enum": ROLES},
                    "leading_word": {"type": "string", "minLength": 3},
                    "neighbours": {"type": "array", "items": {"type": "string"}, "minItems": 1, "maxItems": 3},
                    "status": {"enum": SKILL_STATUS},
                    "reviewed_by": {"type": "string"},
                    "reviewed_on": {"type": "string"},
                    "as_of": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
                    "sources": {"type": "array", "items": {"type": "string"}},
                },
            },
        },
    }
    record = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "regulated-dev-skills record frontmatter (derived from tools/validate.py)",
        "type": "object",
        "required": ["id", "type", "title", "status"],
        "properties": {
            "id": {"type": "string", "pattern": "^(%s)-\\d+$" % "|".join(TYPES.values())},
            "type": {"enum": sorted(TYPES)},
            "title": {"type": "string"},
            "status": {"enum": RECORD_STATUS},
            "authored_by": {"type": "string"},
            "origin": {"enum": ORIGINS},
            "claims": {"type": "object", "additionalProperties": {"enum": CLAIMS}},
            "approval": {
                "type": "object",
                "required": ["by", "role", "on", "revision"],
                "properties": {"by": {"type": "string"}, "role": {"type": "string"}, "on": {"type": "string"},
                               "revision": {"type": "string", "pattern": "^[0-9a-f]{64}$"}, "ref": {"type": "string"}},
            },
            "verifier": {"enum": VERIFIER_KINDS},
            "signed_by": {"type": "object", "required": ["by", "role", "on"]},
            "outcome": {"enum": OUTCOMES},
            "revision": {"type": "string"},
            "anchor": {"type": "string"},
            "anchor_hash": {"type": "string"},
            "commit": {"type": "string"},
        },
    }
    for field in LINKS:
        record["properties"][field] = {"type": "array", "items": {"type": "string"}}
    project = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "regulated-dev-skills project block (derived from tools/validate.py)",
        "type": "object",
        "required": ["rds_version", "backend", "evidence_level", "roles_file", "artefacts_dir", "jurisdictions", "standards"],
        "properties": {
            "rds_version": {"const": 1},
            "backend": {"enum": BACKENDS},
            "evidence_level": {"enum": [0, 1, 2, 3]},
            "roles_file": {"type": "string"},
            "artefacts_dir": {"type": "string"},
            "jurisdictions": {"type": "array", "items": {"enum": JURISDICTIONS}},
            "standards": {"type": "array", "items": {"type": "string"}},
            "safety_class": {"description": "A, B, C or none, or a map of software system to one of those; absent while not decided"},
            "intake": {"type": "string"},
            "record_system_validated": {"type": "string"},
        },
        "x-backend-ceiling": CEILING,
    }
    roles = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "regulated-dev-skills roles file (derived from tools/validate.py)",
        "type": "object",
        "required": ["roles", "approvers"],
        "properties": {
            "roles": {"type": "object", "additionalProperties": {"type": "array", "items": {"type": "string"}}},
            "approvers": {"type": "object", "propertyNames": {"enum": sorted(TYPES)},
                          "additionalProperties": {"type": "array", "items": {"type": "string"}}},
        },
    }
    return {"skill-frontmatter.schema.json": skill, "record.schema.json": record,
            "project-block.schema.json": project, "roles.schema.json": roles}


def cmd_schemas(root, write, check):
    docs = schema_docs()
    outdir = os.path.join(root, "schemas")
    for name, doc in docs.items():
        text = json.dumps(doc, indent=2, sort_keys=True) + "\n"
        path = os.path.join(outdir, name)
        if write:
            os.makedirs(outdir, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        elif check:
            if not os.path.exists(path) or read(path) != text:
                err("RDS001", "schemas/" + name, "schema is out of date; run: python3 tools/validate.py schemas --write")


# ------------------------------------------------------------ revision hash
def revision_hash(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")
    out = []
    in_fm = False
    fm_closed = False
    skipping = False
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            in_fm = True
            out.append(line)
            continue
        if in_fm and not fm_closed:
            if line.strip() == "---":
                fm_closed = True
                skipping = False
                out.append(line)
                continue
            if skipping:
                if line.startswith(" ") or line.strip() == "":
                    continue
                skipping = False
            if line.startswith("status:"):
                continue
            if line.startswith("approval:") or line.startswith("signed_by:"):
                skipping = True
                continue
        out.append(line)
    norm = "\n".join(l.rstrip() for l in out).rstrip() + "\n"
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


UPWARD = ("derives_from", "specifies", "implements", "verifies", "validates", "mitigates", "result_of")


def class_for(project, fm):
    """Safety class that governs a record: the project's class, or its software system's class."""
    if project is None:
        return None
    sc = project.get("safety_class")  # absent means not decided; never defaulted
    if isinstance(sc, dict):
        sysname = fm.get("system")
        if sysname in sc:
            return sc[sysname]
        for c in ("C", "B", "A"):
            if c in sc.values():
                return c
        return "none" if sc else None
    return sc


# --------------------------------------------------------- project block
def load_project_block(path):
    text = read(path)
    m = re.search(r"<!-- regulated-dev-skills:start -->(.*?)<!-- regulated-dev-skills:end -->", text, re.S)
    if not m:
        raise YamlError(1, "no regulated-dev-skills block found")
    f = re.search(r"```yaml\n(.*?)```", m.group(1), re.S)
    if not f:
        raise YamlError(1, "block has no yaml fence")
    return parse(f.group(1))


def check_project(path, display=None):
    disp = display or path
    try:
        p = load_project_block(path)
    except (YamlError, OSError) as e:
        err("RDS301", disp, str(e))
        return None
    if not isinstance(p, dict):
        err("RDS301", disp, "the block must be a map")
        return None
    for k in ("rds_version", "backend", "evidence_level", "roles_file", "artefacts_dir", "jurisdictions", "standards"):
        if k not in p:
            err("RDS302", disp, "missing key %r" % k)
    if p.get("rds_version") != 1:
        err("RDS303", disp, "rds_version must be 1")
    if p.get("backend") not in BACKENDS:
        err("RDS305", disp, "backend must be one of %s" % BACKENDS)
    lvl = p.get("evidence_level")
    if lvl not in (0, 1, 2, 3) or isinstance(lvl, bool):
        err("RDS306", disp, "evidence_level must be 0, 1, 2 or 3")
    elif lvl == 3 and not p.get("record_system_validated"):
        err("RDS307", disp, "evidence level 3 needs record_system_validated: a reference to the validation of the record system")
    elif lvl < 3 and p.get("backend") in CEILING and lvl > CEILING[p["backend"]]:
        err("RDS307", disp, "backend %r supports at most evidence level %d" % (p["backend"], CEILING[p["backend"]]))
    elif p.get("backend") == "jira" and lvl == 2:
        warn("RDS307", disp, "jira at level 2 needs a signature add-on bound to the item revision; document it")
    for j in p.get("jurisdictions") or []:
        if j not in JURISDICTIONS:
            err("RDS308", disp, "unknown jurisdiction %r (v0.1 covers %s)" % (j, JURISDICTIONS))
    sc = p.get("safety_class")
    if "safety_class" in p and not (sc in ("A", "B", "C", "none") or (isinstance(sc, dict) and sc and all(v in ("A", "B", "C", "none") for v in sc.values()))):
        err("RDS310", disp, "safety_class must be A, B, C or none, or a map of software system to one of those; leave it out while it is not decided")
    if p.get("backend") and p.get("backend") != "standalone":
        warn("RDS312", disp, "backend %r has no adapter in this version; only standalone is implemented" % p.get("backend"))
    if "safety_class" not in p:
        warn("RDS311", disp, "no safety class decided: class-dependent checks are not run. Decide it with /intake, or record the chosen depth in the PLAN")
    if not isinstance(p.get("standards"), list) or not p.get("standards"):
        err("RDS309", disp, "standards must pin at least one edition, for example \"ISO 14971:2019\"")
    else:
        for s in p["standards"]:
            if not re.search(r"\d{4}", str(s)):
                err("RDS309", disp, "standard %r has no pinned edition year" % s)
    return p


# ------------------------------------------------------------- roles file
def check_roles(path):
    try:
        r = parse(read(path))
    except (YamlError, OSError) as e:
        err("RDS401", path, str(e))
        return None
    if not isinstance(r, dict):
        err("RDS402", path, "the roles file must be a map")
        return None
    if not isinstance(r.get("roles"), dict) or not isinstance(r.get("approvers"), dict):
        err("RDS402", path, "roles file needs 'roles' and 'approvers' maps")
        return None
    for t, rl in r["approvers"].items():
        if t not in TYPES:
            err("RDS403", path, "approvers: unknown record type %r" % t)
        for role in rl or []:
            if role not in r["roles"]:
                err("RDS404", path, "approvers.%s names unknown role %r" % (t, role))
    return r


# ----------------------------------------------------------------- records
def load_records(artefacts, disp_root):
    recs = {}
    base = os.path.join(artefacts, "records")
    if not os.path.isdir(base):
        return recs
    for dirpath, _dirs, files in os.walk(base):
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            disp = rel(path, disp_root)
            text = read(path)
            try:
                fm_text, body, _n = split_frontmatter(text)
                fm = parse(fm_text)
            except YamlError as e:
                err("RDS201", disp, str(e))
                continue
            if not isinstance(fm, dict):
                err("RDS201", disp, "frontmatter must be a map")
                continue
            rid_ = fm.get("id", fn[:-3])
            if rid_ in recs:
                err("RDS221", disp, "duplicate id %s (also in %s)" % (rid_, recs[rid_]["disp"]))
                continue
            recs[rid_] = {"fm": fm, "body": body, "path": path, "disp": disp, "text": text}
    return recs


def check_records(artefacts, roles_path=None, project_path=None, disp_root=None):
    disp_root = disp_root or artefacts
    roles = check_roles(roles_path) if roles_path else None
    project = check_project(project_path, rel(project_path, disp_root)) if project_path else None
    recs = load_records(artefacts, disp_root)
    children = {}
    stale = []
    for rid, r in sorted(recs.items()):
        fm, body, disp = r["fm"], r["body"], r["disp"]
        t = fm.get("type")
        if t not in TYPES:
            err("RDS202", disp, "type must be one of %s" % sorted(TYPES))
            continue
        m = re.match(r"^([A-Z]+)-(\d+)$", str(rid))
        if not m or PREFIX_TO_TYPE.get(m.group(1)) != t:
            err("RDS203", disp, "id %r does not match type %r (expected %s-<number>)" % (rid, t, TYPES[t]))
        if os.path.basename(r["path"])[:-3] != str(rid):
            err("RDS203", disp, "file name must be %s.md" % rid)
        if fm.get("status") not in RECORD_STATUS:
            err("RDS204", disp, "status must be one of %s" % RECORD_STATUS)
        if not fm.get("title"):
            err("RDS204", disp, "title is required")
        for field, spec in LINKS.items():
            if field not in fm:
                continue
            if t not in spec:
                err("RDS205", disp, "%s is not a valid link field for type %s" % (field, t))
                continue
            targets = fm[field] if isinstance(fm[field], list) else [fm[field]]
            for tid in targets:
                if tid not in recs:
                    err("RDS206", disp, "%s: %s does not exist" % (field, tid))
                    continue
                tt = recs[tid]["fm"].get("type")
                allowed = spec[t]
                ok = "*" in allowed or tt in allowed or ("same" in allowed and tt == t)
                if not ok:
                    err("RDS207", disp, "%s: %s is type %s, expected %s" % (field, tid, tt, allowed))
                children.setdefault(tid, []).append(rid)
        if t == "sw":
            parents = fm.get("derives_from") or []
            if not parents:
                err("RDS208", disp, "a software requirement derives from at least one system requirement")
        if t == "sys" and not fm.get("derives_from"):
            warn("RDS208", disp, "system requirement has no user need above it")
        for c, v in (fm.get("claims") or {}).items():
            if v not in CLAIMS:
                err("RDS209", disp, "claims.%s must be one of %s" % (c, CLAIMS))
        for sec in REQUIRED_SECTIONS.get(t, []):
            ms = re.search(r"^## %s\s*$(.*?)(?=^## |\Z)" % re.escape(sec), body, re.M | re.S)
            if not ms:
                err("RDS210", disp, "missing section '## %s'" % sec)
            elif not ms.group(1).strip():
                err("RDS210", disp, "section '## %s' is empty" % sec)
        for ln in body.splitlines():
            if "BLOCKED" in ln and not re.search(r"BLOCKED\((%s)\)" % "|".join(BLOCKED_KINDS), ln):
                err("RDS211", disp, "BLOCKED must carry a kind: BLOCKED(content), BLOCKED(scope) or BLOCKED(timing)")
        if fm.get("origin") == "extraction":
            for k in ("anchor", "anchor_hash", "commit"):
                if not fm.get(k):
                    err("RDS212", disp, "extracted records need %r" % k)
            if fm.get("status") == "approved" and not fm.get("approval"):
                err("RDS212", disp, "approved without approval block")
        if t == "tr":
            if fm.get("verifier") not in VERIFIER_KINDS:
                err("RDS213", disp, "test result needs verifier in %s" % VERIFIER_KINDS)
            if fm.get("outcome") not in OUTCOMES:
                err("RDS213", disp, "test result needs outcome in %s" % OUTCOMES)
            if not fm.get("revision"):
                err("RDS213", disp, "test result must name the revision under test")
            cls = class_for(project, fm)
            covered = False
            if cls in ("B", "C") and fm.get("covered_by"):
                rep_ = recs.get(fm["covered_by"])
                mine = revision_hash(r["text"])
                if not rep_ or rep_["fm"].get("type") != "vrp":
                    err("RDS220", disp, "covered_by must name a VRP verification report")
                elif not isinstance(rep_["fm"].get("signed_by"), dict) or not all(rep_["fm"]["signed_by"].get(k) for k in ("by", "role", "on")):
                    err("RDS220", disp, "the verification report %s is not signed" % fm["covered_by"])
                elif rep_["fm"]["signed_by"].get("revision") != revision_hash(rep_["text"]):
                    err("RDS220", disp, "the verification report %s changed after it was signed (signed_by.revision must equal its own hash)" % fm["covered_by"])
                elif not re.search(r"%s\s.*%s" % (re.escape(rid), mine[:12]), rep_["text"]):
                    err("RDS220", disp, "report %s does not list this result with its current hash (%s...)" % (fm["covered_by"], mine[:12]))
                elif roles and rep_["fm"]["signed_by"].get("by") not in (roles["roles"].get(rep_["fm"]["signed_by"].get("role")) or []):
                    err("RDS220", disp, "report signer is not listed under its role")
                elif rep_["fm"]["signed_by"].get("by") in (fm.get("authored_by"), fm.get("built_by")):
                    err("RDS220", disp, "the report signer must not be the author or the builder")
                covered = True
            if cls in ("B", "C") and not covered:
                sb = fm.get("signed_by")
                if not isinstance(sb, dict) or not all(sb.get(k) for k in ("by", "role", "on")):
                    err("RDS220", disp, "at class %s a named human independent of the build signs each result (signed_by: by, role, on); without it this is a pre-check" % cls)
                elif sb.get("by") == fm.get("authored_by") or sb.get("by") == fm.get("built_by"):
                    err("RDS220", disp, "the signer must not be the author or the builder")
                elif roles and sb.get("by") not in (roles["roles"].get(sb.get("role")) or []):
                    err("RDS220", disp, "signer %s is not listed under role %s in the roles file" % (sb.get("by"), sb.get("role")))
                elif project and project.get("evidence_level", 0) >= 1 and not sb.get("ref"):
                    err("RDS220", disp, "evidence level %s needs signed_by.ref (the host's own record of the signature)" % project["evidence_level"])
                elif sb.get("revision") != revision_hash(r["text"]):
                    err("RDS220", disp, "signed_by.revision must equal the result's revision hash (%s...); the result changed after it was signed, or the hash is missing" % revision_hash(r["text"])[:8])
        ap = fm.get("approval")
        if ap and fm.get("status") not in ("approved", "obsolete"):
            err("RDS214", disp, "record carries an approval but its status is %r; an approval holds only while the record is approved" % fm.get("status"))
        if fm.get("status") == "obsolete" and not fm.get("obsoleted_by"):
            err("RDS214", disp, "an obsolete record names what replaced it or why (obsoleted_by)")
        if fm.get("status") == "approved" and not ap:
            err("RDS214", disp, "status approved but no approval block")
        if ap:
            if not isinstance(ap, dict):
                err("RDS214", disp, "approval must be a map")
                continue
            for k in ("by", "role", "on", "revision"):
                if not ap.get(k):
                    err("RDS214", disp, "approval is missing %r" % k)
            if project and project.get("evidence_level", 0) >= 1 and not ap.get("ref"):
                err("RDS215", disp, "evidence level %s needs approval.ref (the host's own approval)" % project["evidence_level"])
            _on, _asof = str(ap.get("on", "")), str(fm.get("as_of", ""))
            import datetime as _dt
            if _on and _on > _dt.date.today().isoformat():
                err("RDS223", disp, "approval is dated in the future (%s)" % _on)
            if _on and _asof and _on < _asof:
                err("RDS223", disp, "approval (%s) is dated before the record's as_of date (%s)" % (_on, _asof))
            if not fm.get("authored_by"):
                err("RDS216", disp, "an approved record must name authored_by, or the author-not-approver check cannot run")
            if ap.get("by") and ap.get("by") == fm.get("authored_by"):
                err("RDS216", disp, "the author cannot approve their own record")
            if roles:
                if ap.get("by") not in (roles["roles"].get(ap.get("role")) or []):
                    err("RDS217", disp, "%s is not listed under role %s" % (ap.get("by"), ap.get("role")))
                if ap.get("role") not in (roles["approvers"].get(t) or []):
                    err("RDS217", disp, "role %s may not approve type %s" % (ap.get("role"), t))
            current = revision_hash(r["text"])
            if ap.get("revision") and ap["revision"] != current:
                stale.append(rid)
                warn("RDS218", disp, "STALE: approval revision %s... does not match current %s..." % (str(ap["revision"])[:8], current[:8]))
        for mm in re.finditer(r"\*\*(\d+)\*\*<!--count:([a-z0-9-]+)-->", body):
            n, key = int(mm.group(1)), mm.group(2)
            actual = None
            if key.startswith("records-") and key[8:] in TYPES:
                actual = sum(1 for x in recs.values() if x["fm"].get("type") == key[8:])
            elif key.startswith("children-"):
                actual = len(children.get(key[9:], []))
            if actual is None:
                err("RDS219", disp, "unknown count key %r" % key)
            elif actual != n:
                err("RDS219", disp, "count marker %s says %d, actual %d" % (key, n, actual))
    # suspect: an approved record whose upward link points at a record that is stale, unapproved,
    # or approved after it. Its approval rests on a parent that has moved.
    suspect = []
    for rid, r in recs.items():
        fm = r["fm"]
        ap = fm.get("approval")
        if not isinstance(ap, dict) or rid in stale:
            continue
        for k in UPWARD:
            v = fm.get(k) or []
            for pid in ([v] if isinstance(v, str) else v):
                pr = recs.get(pid)
                if not pr:
                    continue
                pap = pr["fm"].get("approval")
                why = None
                if pid in stale:
                    why = "is stale"
                elif pr["fm"].get("status") != "approved":
                    why = "is not approved"
                elif isinstance(pap, dict) and str(pap.get("on", "")) > str(ap.get("on", "")):
                    why = "was approved after this record (%s > %s)" % (pap.get("on"), ap.get("on"))
                if why:
                    suspect.append(rid)
                    warn("RDS222", r["disp"], "SUSPECT: parent %s %s; re-review this record" % (pid, why))
    SUSPECT[:] = sorted(set(suspect))
    return recs, children, stale


SUSPECT = []


def release_gate(recs, cov, project_path, disp, baseline=None):
    if baseline:
        import subprocess as _sp
        here = os.path.dirname(os.path.abspath(project_path or disp))
        inside = _sp.run(["git", "-C", here, "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True).stdout.strip() == "true"
        if not inside or os.environ.get("RDS_BASELINE_UNCHECKED") == "1":
            warn("RDS411", "baseline", "the baseline was not checked against git (%s)" % ("not inside a git work tree" if not inside else "RDS_BASELINE_UNCHECKED=1"))
        if inside and os.environ.get("RDS_BASELINE_UNCHECKED") != "1":
            ok = _sp.run(["git", "-C", here, "cat-file", "-e", baseline + "^{commit}"], capture_output=True).returncode == 0
            if ok:
                head = _sp.run(["git", "-C", here, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
                base = _sp.run(["git", "-C", here, "rev-parse", baseline + "^{commit}"], capture_output=True, text=True).stdout.strip()
                dirty = _sp.run(["git", "-C", here, "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
                if head != base or dirty:
                    warn("RDS410", "baseline", "the working tree is not the baseline (%s); release from a clean checkout of the baseline so what is released is what was tested" % ("uncommitted changes" if dirty else "HEAD is " + head[:8]))
            if not ok:
                warn("RDS407", "baseline", "baseline %s does not resolve to a commit in this repository; the results cannot be tied to the tested configuration" % baseline)
    proj = None
    if project_path:
        try:
            proj = load_project_block(project_path)
        except Exception:
            proj = None
    for k, why in (("stale_approvals", "approval is stale"), ("suspect_approvals", "approval rests on a parent that moved"),
                   ("linked_but_unverified", "has a test case but no passing current result"),
                   ("test_cases_without_result", "test case has no result"),
                   ("without_verification", "requirement or specification has no test case"),
                   ("specifications_without_requirement", "specification specifies no requirement")):
        for rid in cov.get(k) or []:
            err("RDS401", rid, "release blocker: %s" % why)
    for rid, r in recs.items():
        fm = r["fm"]
        if fm.get("type") in ("cls", "plan", "un", "sys", "sw", "spec", "haz", "rc", "rmr", "soup", "tc", "rev") and fm.get("status") not in ("approved", "obsolete"):
            err("RDS406", rid, "release blocker: record in scope is %r, not approved" % fm.get("status"))
        if fm.get("type") == "sys" and not fm.get("derives_from"):
            err("RDS401", rid, "release blocker: system requirement has no user need above it")
        if fm.get("type") == "un":
            vtcs = [x for x, y in recs.items() if y["fm"].get("type") == "tc" and rid in ([y["fm"].get("validates")] if isinstance(y["fm"].get("validates"), str) else (y["fm"].get("validates") or []))]
            passing = [x for x, y in recs.items() if y["fm"].get("type") == "tr" and y["fm"].get("outcome") == "pass" and any(tc in (y["fm"].get("result_of") or []) for tc in vtcs)]
            if not passing:
                err("RDS401", rid, "release blocker: user need has no passing validation result")
        if baseline and fm.get("type") == "tr" and str(fm.get("revision", "")) != str(baseline):
            err("RDS404", rid, "release blocker: result is on revision %s, not the release baseline %s" % (fm.get("revision"), baseline))
    if proj is not None:
        if int(proj.get("evidence_level", 0) or 0) < 1:
            err("RDS408", "project block", "release blocker: evidence level 0; approvals and signatures are unauthenticated text, so release needs level 1 or above (export as an uncontrolled draft instead)")
        for rid, r in recs.items():
            if r["fm"].get("type") == "plan":
                ms = re.search(r"^## QMS boundary\s*$(.*?)(?=^## |\Z)", r["text"], re.M | re.S)
                if not ms or not ms.group(1).strip():
                    err("RDS409", rid, "release blocker: the development plan has no QMS boundary section with owners")
                elif re.search(r"owner:\s*(tbd|none|\?)?\s*$", ms.group(1), re.I | re.M):
                    err("RDS409", rid, "release blocker: a QMS boundary item has no owner")
        claims = any("62304" in str(s) for s in (proj.get("standards") or []))
        sc = proj.get("safety_class")
        device = sc in ("A", "B", "C") or (isinstance(sc, dict) and any(v in ("A", "B", "C") for v in sc.values()))
        if device:
            have = {r["fm"].get("type") for r in recs.values()}
            for typ, what in (("cls", "a classification"), ("plan", "a development plan"), ("un", "user needs"), ("sw", "software requirements"), ("rmr", "a risk management report"), ("rev", "a design review")):
                if typ not in have:
                    err("RDS405", "records", "release blocker: device software needs %s (%s record)" % (what, TYPES[typ]))
        if claims and "safety_class" not in proj:
            err("RDS402", "project block", "release blocker: IEC 62304 is claimed and no safety class is decided (62304 4.3 g); a person must decide it with /intake")
        for rid, r in recs.items():
            fm = r["fm"]
            if fm.get("type") == "soup" and class_for(proj, fm) in ("B", "C") and not fm.get("anomalies_evaluated"):
                err("RDS403", r["disp"], "release blocker: SOUP item has no anomalies_evaluated date at class B or C (62304 7.1.3)")


def coverage_report(recs, children, stale):
    by_status = {}
    for r in recs.values():
        by_status[r["fm"].get("status")] = by_status.get(r["fm"].get("status"), 0) + 1
    def of(t):
        return [rid for rid, r in recs.items() if r["fm"].get("type") == t]
    def lst(v):
        return [v] if isinstance(v, str) else (v or [])
    good_tc = set()
    for rid, r in recs.items():
        fm = r["fm"]
        if fm.get("type") == "tr" and fm.get("outcome") == "pass" and rid not in stale:
            for tc in lst(fm.get("result_of")):
                good_tc.add(tc)
    linked, verified = set(), set()
    for rid, r in recs.items():
        if r["fm"].get("type") == "tc":
            for tid in lst(r["fm"].get("verifies")):
                linked.add(tid)
                if rid in good_tc:
                    verified.add(tid)
    no_ver = [rid for t in ("sys", "sw", "spec") for rid in of(t) if rid not in linked]
    linked_unver = sorted(x for x in linked if x not in verified)
    sw_orphans = [rid for rid in of("sw") if not (recs[rid]["fm"].get("derives_from") or [])]
    multi = [rid for rid in of("sw") if len(recs[rid]["fm"].get("derives_from") or []) > 1]
    unsigned = [rid for rid in of("tr") if not isinstance(recs[rid]["fm"].get("signed_by"), dict)]
    with_result = {tid for rid in of("tr") for tid in (recs[rid]["fm"].get("result_of") or [])}
    no_result = [rid for rid in of("tc") if rid not in with_result]
    spec_orphans = [rid for rid in of("spec") if not (recs[rid]["fm"].get("specifies") or [])]
    blocked = {}
    for r in recs.values():
        for k in BLOCKED_KINDS:
            n = len(re.findall(r"BLOCKED\(%s\)" % k, r["body"]))
            if n:
                blocked[k] = blocked.get(k, 0) + n
    return {"records": len(recs), "by_status": by_status, "verified": sorted(verified), "linked_but_unverified": linked_unver, "stale_approvals": sorted(stale), "suspect_approvals": list(SUSPECT),
            "software_requirements_without_parent": sw_orphans, "software_requirements_with_several_parents": multi, "results_without_human_signature": unsigned, "test_cases_without_result": no_result, "specifications_without_requirement": spec_orphans,
            "without_verification": no_ver, "blocked_by_kind": blocked}


# --------------------------------------------------------------- repo checks
def discover_skills(root):
    skills = []
    base = os.path.join(root, "skills")
    if not os.path.isdir(base):
        return skills
    for g in sorted(os.listdir(base)):
        gp = os.path.join(base, g)
        if not os.path.isdir(gp):
            continue
        for n in sorted(os.listdir(gp)):
            sp = os.path.join(gp, n, "SKILL.md")
            if os.path.isfile(sp):
                skills.append((g, n, sp))
    return skills


def check_skill(root, g, n, sp):
    disp = rel(sp, root)
    text = read(sp)
    try:
        fm_text, body, _ = split_frontmatter(text)
        fm = parse(fm_text)
    except YamlError as e:
        err("RDS101", disp, str(e))
        return None
    if not isinstance(fm, dict):
        err("RDS101", disp, "frontmatter must be a map")
        return None
    if fm.get("name") != n or not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", str(fm.get("name"))) or len(str(fm.get("name"))) > 64:
        err("RDS102", disp, "name must equal the folder name %r (lowercase, hyphens, <= 64)" % n)
    d = fm.get("description")
    meta = fm.get("metadata") or {}
    for k in ("group", "invocation", "role", "leading_word", "neighbours", "status", "reviewed_by", "reviewed_on", "as_of", "sources"):
        if k not in meta:
            err("RDS103", disp, "metadata.%s is missing" % k)
    if meta.get("group") != g:
        err("RDS104", disp, "metadata.group %r does not match the folder %r" % (meta.get("group"), g))
    if g not in GROUPS:
        err("RDS104", disp, "unknown group folder %r" % g)
    if meta.get("invocation") not in INVOCATIONS:
        err("RDS105", disp, "metadata.invocation must be model or typed")
    typed = fm.get("disable-model-invocation") is True
    if (meta.get("invocation") == "typed") != typed:
        err("RDS106", disp, "invocation and disable-model-invocation disagree")
    if not isinstance(d, str) or not d:
        err("RDS107", disp, "description is required")
    elif meta.get("invocation") == "model":
        first = d.split(". ")[0].rstrip(".") + "."
        if not d.startswith("Use when"):
            err("RDS108", disp, "a model-invoked description starts 'Use when'")
        if len(first) > 57:
            err("RDS108", disp, "trigger sentence is %d characters; the first 57 must be a self-contained trigger" % len(first))
        if len(d) > 250:
            err("RDS108", disp, "description is %d characters; the limit is 250" % len(d))
    else:
        if len(d) > 100:
            err("RDS109", disp, "typed description is %d characters; the limit is 100" % len(d))
        if d.startswith("Use when"):
            err("RDS109", disp, "a typed description is a human summary, not a trigger")
    if meta.get("role") not in ROLES:
        err("RDS116", disp, "metadata.role must be one of %s" % ROLES)
    nb = meta.get("neighbours")
    if not isinstance(nb, list) or not 1 <= len(nb) <= 3:
        err("RDS117", disp, "metadata.neighbours needs one to three skill names")
    if not isinstance(meta.get("leading_word"), str) or len(meta.get("leading_word", "")) < 3:
        err("RDS118", disp, "metadata.leading_word is required")
    if meta.get("status") not in SKILL_STATUS:
        err("RDS111", disp, "metadata.status must be one of %s" % SKILL_STATUS)
    if meta.get("status") == "reviewed" and (meta.get("reviewed_by") in (None, "none") or str(meta.get("reviewed_by")).startswith("models only") or meta.get("reviewed_on") in (None, "none")):
        err("RDS111", disp, "status reviewed needs reviewed_by and reviewed_on")
    if meta.get("status") == "draft" and meta.get("reviewed_by") not in (None, "none") and not str(meta.get("reviewed_by")).startswith("models only"):
        warn("RDS111", disp, "draft skill names a reviewer; set status to reviewed")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(meta.get("as_of", ""))):
        err("RDS112", disp, "metadata.as_of must be YYYY-MM-DD")
    if not isinstance(meta.get("sources"), list):
        err("RDS112", disp, "metadata.sources must be a list (may be empty)")
    elif len(meta["sources"]) != len(set(map(str, meta["sources"]))):
        err("RDS110", disp, "metadata.sources lists the same source twice")
    heads = re.findall(r"^## (.+?)\s*$", body, re.M)
    want = (["When to use"] if meta.get("invocation") == "model" else []) + SKILL_SECTIONS
    if re.search(r"^## Regulated specifics", body, re.M):
        err("RDS113", disp, "'Regulated specifics' is obsolete: every skill is regulated")
    see = re.search(r"^## See also\s*\n(.*)", body, re.M | re.S)
    if see:
        for n in (meta.get("neighbours") or []):
            if "`%s`" % n not in see.group(1):
                err("RDS119", disp, "See also does not mention neighbour %s" % n)
    ap = re.search(r"^## Anti-patterns and their tells\s*\n(.*?)(?=^## )", body, re.M | re.S)
    if ap and not re.search(r"^\| .+ \| .+ \|$", ap.group(1), re.M):
        err("RDS122", disp, "Anti-patterns section needs a table")
    ref = re.search(r"^## Refuses\s*\n(.*?)(?=^## )", body, re.M | re.S)
    if ref:
        for l in ref.group(1).splitlines():
            if l.startswith("- ") and "*Instead:*" not in l:
                err("RDS123", disp, "refusal without '*Instead:*': %s" % l[:60])
    pos = -1
    for w in want:
        if w not in heads:
            err("RDS113", disp, "missing section '## %s'" % w)
        else:
            idx = heads.index(w)
            if idx < pos:
                err("RDS113", disp, "section '## %s' is out of order" % w)
            pos = idx
    proc = re.search(r"^## Process\s*\n(.*?)(?=^## )", body, re.M | re.S)
    if proc:
        steps = [l for l in proc.group(1).splitlines() if re.match(r"^\d+\. ", l)]
        if not steps:
            err("RDS114", disp, "Process has no numbered steps")
        for s in steps:
            if "*Done when:*" not in s:
                err("RDS114", disp, "step without a completion criterion: %s" % s[:60])
    return fm


def check_docs_page(root, g, n, meta):
    disp = "docs/%s/%s.md" % (g, n)
    path = os.path.join(root, "docs", g, n + ".md")
    if not os.path.exists(path):
        err("RDS160", disp, "missing docs page")
        return
    text = read(path)
    if re.search(r"^# ", text, re.M):
        err("RDS161", disp, "no H1 on a docs page")
    heads = re.findall(r"^## (.+?)\s*$", text, re.M)
    for h in DOCS_REQUIRED:
        if h not in heads:
            err("RDS162", disp, "missing section '## %s'" % h)
    def rank(h):
        return DOCS_ORDER.index(h) if h in DOCS_ORDER else DOCS_ORDER.index("*")
    ranks = [rank(h) for h in heads]
    if ranks != sorted(ranks):
        err("RDS163", disp, "sections out of order: %s" % heads)
    if not [h for h in heads if h not in DOCS_ORDER]:
        err("RDS164", disp, "needs at least one free-form section in the skill's own vocabulary")
    lw = str(meta.get("leading_word", ""))
    if lw and lw.lower() not in text.lower():
        err("RDS165", disp, "leading word %r does not appear on the page" % lw)
    if "FLOWS.md" not in text:
        err("RDS166", disp, "Where it fits must link FLOWS.md")
    if re.search(r"(npx skills|plugin install|marketplace add)", text):
        err("RDS167", disp, "docs pages carry no install commands")


STAGES = [
    ("Start", ["setup", "intake", "development-plan"], "Plan review"),
    ("Needs and use", ["user-needs", "usability (use specification, user interface specification)", "risk"], "Design input review"),
    ("Requirements and design", ["requirements", "specifications", "usability (formative evaluation)"], "Design review"),
    ("Build and verify", ["implement", "unit-verification", "verify"], "Verification review"),
    ("Validate and release", ["usability (summative)", "validation (design validation)", "approve", "package", "release"], "Release review"),
    ("After release", ["maintenance", "problem-resolution"], "Periodic review"),
]
CHAIN = [s.split(" ")[0] for _, ss, _ in STAGES for s in ss]


def render_flows(metas):
    out = ["# Flows", "", "<!-- generated by tools/validate.py flows --write; do not edit -->", "",
           "How the skills hand off to each other. The tables are generated from each skill's `neighbours`. The stage table is kept in the validator; it shows the usual order, not the only one.", "",
           "## The stages", "", "Each stage ends with a `design-review` at the boundary the development plan names. `usability` appears three times on purpose: it starts with the needs, runs formative evaluation during design and summative evaluation at the end, where `validation` uses its results.", "",
           "| Stage | Skills, in order | Ends with |", "| --- | --- | --- |"]
    for name, ss, review in STAGES:
        cells = ", ".join("`%s`%s" % (s.split(" ")[0], s[len(s.split(" ")[0]):]) for s in ss if s.split(" ")[0] in metas)
        out.append("| %s | %s | `design-review`: %s |" % (name, cells, review))
    out += ["", "`traceability`, `risk`, `security-diligence` and `configuration-management` run alongside every stage. Post-market work beyond software maintenance sits outside the skills and in your QMS: the PMS plan, the PMS report (class I) or PSUR (class IIa and above), trend reports and PMCF; `maintenance` names an owner for each. `problem-resolution` takes any defect back into the chain. `impact` prices any change and sends reclassification triggers back to `intake`.", "",
            "For existing code: `design-inputs-from-code`, `hazards-from-code`, `soup-from-code` -> `gap-assessment` -> `requirements`.", "",
            "## Every skill", "", "| Skill | Invoked | Role | Leading word | Hands to or from |", "| --- | --- | --- | --- | --- |"]
    for n in sorted(metas, key=lambda x: (GROUPS.index(metas[x][0]) if metas[x][0] in GROUPS else 99, x)):
        g, m = metas[n]
        inv = "typed" if m.get("invocation") == "typed" else "model"
        nbs = ", ".join("[`%s`](docs/%s/%s.md)" % (x, metas[x][0], x) for x in (m.get("neighbours") or []) if x in metas)
        out.append("| [`%s`](docs/%s/%s.md) | %s | %s | %s | %s |" % (n, g, n, inv, m.get("role", ""), m.get("leading_word", ""), nbs))
    return "\n".join(out) + "\n"


def iter_text_files(root):
    skip = {".git", "node_modules", "__pycache__"}
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in skip]
        for fn in files:
            if fn == "LICENSE":
                continue
            if fn.endswith((".md", ".json", ".yml", ".yaml", ".py", ".svg", ".txt", ".html", ".sh")):
                yield os.path.join(dirpath, fn)


def check_repo(root):
    skills = discover_skills(root)
    if not skills:
        err("RDS100", "skills/", "no skills found")
    names = {}
    for g, n, sp in skills:
        if n in names:
            err("RDS115", rel(sp, root), "duplicate skill name %r" % n)
        names[n] = g
        check_skill(root, g, n, sp)
    metas = {}
    for g, n, sp in skills:
        try:
            metas[n] = (g, (parse(split_frontmatter(read(sp))[0]).get("metadata") or {}))
        except YamlError:
            pass
    for n, (g, meta) in metas.items():
        for nb in meta.get("neighbours") or []:
            if nb not in metas:
                err("RDS117", "skills/%s/%s/SKILL.md" % (g, n), "neighbour %r does not exist" % nb)
            if nb == n:
                err("RDS117", "skills/%s/%s/SKILL.md" % (g, n), "a skill cannot be its own neighbour")
        check_docs_page(root, g, n, meta)
    flows = render_flows(metas)
    fp = os.path.join(root, "FLOWS.md")
    if not os.path.exists(fp) or read(fp) != flows:
        err("RDS150", "FLOWS.md", "out of date; run: python3 tools/validate.py flows --write")
    if not os.path.exists(os.path.join(root, "CHANGELOG.md")):
        err("RDS151", "CHANGELOG.md", "missing")
    # manifest
    manifest = os.path.join(root, ".claude-plugin", "plugin.json")
    if os.path.exists(manifest):
        try:
            listed = set(json.loads(read(manifest)).get("skills", []))
        except ValueError as e:
            listed = set()
            err("RDS120", ".claude-plugin/plugin.json", "invalid JSON: %s" % e)
        have = {"./skills/%s/%s" % (g, n) for g, n, _ in skills}
        for x in sorted(have - listed):
            err("RDS121", ".claude-plugin/plugin.json", "skill not listed: %s" % x)
        for x in sorted(listed - have):
            err("RDS121", ".claude-plugin/plugin.json", "lists a skill that does not exist: %s" % x)
    else:
        warn("RDS120", ".claude-plugin/plugin.json", "missing")
    # catalogue and counts in README
    readme = os.path.join(root, "README.md")
    if os.path.exists(readme):
        rt = read(readme)
        for g, n, _ in skills:
            if "docs/%s/%s.md" % (g, n) not in rt:
                err("RDS130", "README.md", "does not link docs/%s/%s.md" % (g, n))
        counts = {"skills": len(skills),
                  "skills-typed": 0, "skills-model": 0}
        for g, n, sp in skills:
            try:
                fm = parse(split_frontmatter(read(sp))[0])
                counts["skills-" + str((fm.get("metadata") or {}).get("invocation"))] = counts.get("skills-" + str((fm.get("metadata") or {}).get("invocation")), 0) + 1
            except YamlError:
                pass
        for mm in re.finditer(r"\*\*(\d+)\*\*<!--count:([a-z0-9-]+)-->", rt):
            key = mm.group(2)
            if key in counts and counts[key] != int(mm.group(1)):
                err("RDS131", "README.md", "count marker %s says %s, actual %d" % (key, mm.group(1), counts[key]))
    else:
        err("RDS130", "README.md", "missing")
    # em dashes and links
    for path in iter_text_files(root):
        text = read(path)
        disp = rel(path, root)
        if EM_DASH in text:
            ln = text[:text.index(EM_DASH)].count("\n") + 1
            err("RDS140", disp, "em dash at line %d; this repository does not use them" % ln)
        if path.endswith(".md"):
            for m in re.finditer(r"\]\(([^)\s]+)\)", text):
                tgt = m.group(1)
                if re.match(r"^(https?:|mailto:|#)", tgt):
                    continue
                tgt = tgt.split("#")[0]
                if not tgt:
                    continue
                full = os.path.normpath(os.path.join(os.path.dirname(path), tgt))
                if not os.path.exists(full):
                    err("RDS141", disp, "broken link: %s" % m.group(1))
    cmd_schemas(root, write=False, check=True)
    for fn, src in (("validate.py", "tools"), ("rds_yaml.py", "tools"), ("RECORDS.md", "spec")):
        a, b = os.path.join(root, src, fn if fn != "RECORDS.md" else "records.md"), os.path.join(root, "skills", "gates", "setup", "scripts", fn)
        if not os.path.exists(b) or read(a) != read(b):
            err("RDS170", "skills/gates/setup/scripts/" + fn, "must be identical to its source in tools/ or spec/; copy it")


def report(root):
    for code, path, msg in sorted(set(warnings)):
        print("warning %s %s: %s" % (code, path, msg))
    for code, path, msg in sorted(set(errors)):
        print("error   %s %s: %s" % (code, path, msg))
    print("%d error(s), %d warning(s)" % (len(set(errors)), len(set(warnings))))
    print("Structure check only: links, hashes, roles, sections and counts. It does not assess whether a classification, a risk judgement or a verification is correct.")
    return 1 if errors else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("repo")
    p.add_argument("--root", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    p = sub.add_parser("records")
    p.add_argument("dir")
    p.add_argument("--roles")
    p.add_argument("--project")
    p.add_argument("--report", action="store_true")
    p.add_argument("--release", action="store_true")
    p.add_argument("--baseline", help="with --release: the revision every test result must name")
    p = sub.add_parser("project")
    p.add_argument("file")
    p = sub.add_parser("hash")
    p.add_argument("file")
    p = sub.add_parser("flows")
    p.add_argument("--root", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    p.add_argument("--write", action="store_true")
    p = sub.add_parser("schemas")
    p.add_argument("--root", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    g = p.add_mutually_exclusive_group()
    g.add_argument("--write", action="store_true")
    g.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    cmd = a.cmd or "repo"
    if cmd == "repo":
        root = os.path.abspath(getattr(a, "root", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))
        check_repo(root)
        return report(root)
    if cmd == "records":
        recs, children, stale = check_records(os.path.abspath(a.dir), a.roles, a.project, os.path.abspath(a.dir))
        cov = coverage_report(recs, children, stale)
        if a.report:
            print(json.dumps(cov, indent=2, sort_keys=True))
        if a.release:
            release_gate(recs, cov, a.project, a.dir, a.baseline)
        return report(a.dir)
    if cmd == "project":
        check_project(a.file)
        return report(a.file)
    if cmd == "hash":
        print(revision_hash(read(a.file)))
        return 0
    if cmd == "flows":
        root = os.path.abspath(a.root)
        metas = {}
        for g, n, sp in discover_skills(root):
            metas[n] = (g, parse(split_frontmatter(read(sp))[0]).get("metadata") or {})
        text = render_flows(metas)
        if a.write:
            with open(os.path.join(root, "FLOWS.md"), "w", encoding="utf-8") as f:
                f.write(text)
        else:
            print(text)
        return 0
    if cmd == "schemas":
        root = os.path.abspath(a.root)
        cmd_schemas(root, write=a.write, check=not a.write)
        return report(root)
    return 2


if __name__ == "__main__":
    sys.exit(main())
