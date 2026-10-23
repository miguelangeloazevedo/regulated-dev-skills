"""Generate assurance views without changing declared assurance states."""
import argparse
from pathlib import Path
from rds_assurance import render_summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for kind, content in render_summary(args.root).items():
        path = args.root / 'docs' / 'assurance' / (kind + '.md')
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                stale.append(kind)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
    if stale:
        parser.exit(1, 'Stale assurance views: ' + ', '.join(stale) + '\n')


if __name__ == '__main__':
    main()
