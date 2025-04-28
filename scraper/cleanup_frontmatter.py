#!/usr/bin/env python3
import os
import re

TOOLS_DIR = os.path.join(os.path.dirname(__file__), "..", "site", "content", "tools")

def process_file(path):
    text = open(path, 'r', encoding='utf-8').read()
    # Split at front-matter markers
    parts = re.split(r'^---\s*$', text, flags=re.MULTILINE)
    if len(parts) < 3:
        # No proper front matter found → skip
        return False

    # parts[1] is the old front matter, parts[2:] is the rest (could include extra '---')
    old_fm = parts[1].strip().splitlines()
    rest = "\n".join(parts[2:]).lstrip('\n')

    title = None
    category = None
    url = None

    for line in old_fm:
        line = line.strip()
        if line.lower().startswith("title:"):
            title = line.split(":",1)[1].strip().strip('"').strip("'")
        elif line.lower().startswith("category:"):
            category = line.split(":",1)[1].strip().strip('"').strip("'")
        elif line.lower().startswith("url:"):
            url = line.split(":",1)[1].strip().strip('"').strip("'")

    # Fallbacks
    fname = os.path.splitext(os.path.basename(path))[0]
    if not title:
        title = fname
    if not category:
        category = "Miscellaneous"

    # Build new front matter
    fm = [
        "---",
        f'title: "{title}"',
        f'category: "{category}"',
        "---",
        ""
    ]

    # Build body: inject link if we extracted one
    body = []
    if url:
        body.append(f"[🔗 Visit Repository]({url})")
        body.append("")
    body.append(rest)

    new_text = "\n".join(fm + body)

    # Overwrite only if changed
    if new_text != text:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Fixed front matter in {path}")
        return True
    return False

def main():
    count = 0
    for root, _, files in os.walk(TOOLS_DIR):
        for fn in files:
            if fn.endswith(".md"):
                p = os.path.join(root, fn)
                if process_file(p):
                    count += 1
    print(f"\nCompleted. Fixed {count} file(s).")

if __name__ == "__main__":
    main()
      
