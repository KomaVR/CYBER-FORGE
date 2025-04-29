#!/usr/bin/env python3
import os
import re

# Directory where your tool pages live
TOOLS_DIR = os.path.join("site", "content", "tools")

# Matches the entire front matter and body, capturing both parts
FRONT_MATTER_RE = re.compile(
    r'^(?P<delim>---\s*\n)'        # opening delimiter
    r'(?P<front>.*?\n)'            # front matter content (non-greedy)
    r'(?P=delim)'                  # closing delimiter (same as opening)
    r'(?P<body>.*)$',              # rest of file
    re.DOTALL
)

# Matches a url: line inside front matter
URL_LINE_RE = re.compile(r'^\s*url\s*:\s*["\']?(https?://[^\s"\'`]+)["\']?', re.IGNORECASE)

def fix_file(path):
    text = open(path, 'r', encoding='utf-8').read()
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return False

    front = m.group('front').splitlines()
    body = m.group('body')

    new_front = []
    extracted_url = None

    for line in front:
        um = URL_LINE_RE.match(line)
        if um:
            extracted_url = um.group(1)
            # skip this line entirely
        else:
            new_front.append(line)

    if not extracted_url:
        # no url line found
        return False

    # Reassemble
    new_content = []
    new_content.append(m.group('delim'))
    new_content.append("\n".join(new_front).rstrip() + "\n")
    new_content.append(m.group('delim'))
    # Insert the link at the top of the body
    new_content.append(f"\n[🔗 Visit Site]({extracted_url})\n\n")
    new_content.append(body.lstrip('\n'))

    with open(path, 'w', encoding='utf-8') as f:
        f.write("".join(new_content))

    print(f"Fixed: {path}")
    return True

def main():
    fixed = 0
    for root, _, files in os.walk(TOOLS_DIR):
        for fn in files:
            if fn.endswith('.md'):
                full = os.path.join(root, fn)
                if fix_file(full):
                    fixed += 1
    print(f"\nDone. Fixed {fixed} file(s).")

if __name__ == "__main__":
    main()
