"""Log parser (template)
Combines/filters logs from multiple files and prints structured output.
"""
import glob, re, json, sys

PATTERN = re.compile(r"(?P<ts>\d{4}-\d{2}-\d{2}[^ ]*) (?P<level>[A-Z]+) (?P<msg>.*)")

def parse_line(line):
    m = PATTERN.search(line)
    if not m:
        return None
    return m.groupdict()

def main(paths):
    items = []
    for p in paths:
        for f in glob.glob(p):
            with open(f, errors='ignore') as fh:
                for line in fh:
                    obj = parse_line(line.strip())
                    if obj:
                        items.append(obj)
    print(json.dumps(items[:500], indent=2))

if __name__ == "__main__":
    main(sys.argv[1:] or ["/var/log/*.log"])