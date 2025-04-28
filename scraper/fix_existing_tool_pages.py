#!/usr/bin/env python3
import os
import re

# Directory where your tool pages are generated
TOOLS_DIR = os.path.join(os.path.dirname(__file__), "..", "site", "content", "tools")

# Matches the whole front-matter block and body
FRONT_MATTER_RE = re.compile(
    r'^(---\s*\n)'         # opening delimiter
    r'(.*?)\n'             # front matter content (lazy)
    r'(---\s*\n)'          # closing delimiter
    r'(.*)$',              # rest of file
    re.DOTALL
)

# Finds a url: line
URL_LINE_RE = re.compile(r'^\s*url\s*:\s*["\']?(https?://\S+)["\']?\s*$', re.IGNORECASE)

def fix_file(path):
    text = open(path, 'r', encoding='utf-8').read()
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return False

    open_delim, front, close_delim, body = m.groups()
    new_front_lines = []
    extracted_url = None

    for line in front.splitlines():
        um = URL_LINE_RE.match(line)
        if um:
            extracted_url = um.group(1).strip()
        else:
            new_front_lines.append(line)

    if not extracted_url:
        return False

    # Rebuild front matter without the url line
    new_front = open_delim
    if new_front_lines:
        new_front += "\n".join(new_front_lines).rstrip() + "\n"
    new_front += close_delim

    # Prepend the link into the body
    link_md = f"[🔗 Visit Repository]({extracted_url})\n\n"
    new_body = link_md + body.lstrip("\n")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_front + new_body)

    print(f"Fixed: {path}")
    return True

def main():
    fixed_count = 0
    for root, _, files in os.walk(TOOLS_DIR):
        for fn in files:
            if fn.endswith(".md"):
                full = os.path.join(root, fn)
                if fix_file(full):
                    fixed_count += 1

    print(f"\nDone. Fixed {fixed_count} file(s).")

if __name__ == "__main__":
    main()
