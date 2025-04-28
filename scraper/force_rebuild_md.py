#!/usr/bin/env python3
import os
import re

# Paths
REPO_ROOT = os.path.dirname(__file__)
TOOLS_DIR = os.path.normpath(os.path.join(REPO_ROOT, "..", "site", "content", "tools"))

# Regex to find first URL in the file
URL_FIND_RE = re.compile(r'(https?://[^\s"\'`]+)')

def force_rebuild(path):
    text = open(path, 'r', encoding='utf-8').read()

    # Extract URL if present on first line or anywhere
    url_match = URL_FIND_RE.search(text)
    url = url_match.group(1) if url_match else None

    # Remove all old front matter and strip any leading URL line
    # Split off existing front matter if any
    parts = re.split(r'^---.*?---\s*', text, flags=re.DOTALL)
    body = parts[-1].lstrip()  # take everything after the last front matter

    # Also strip a leading bare URL if body starts with it
    if url and body.startswith(url):
        body = body[len(url):].lstrip()

    # Derive title from filename
    fname = os.path.splitext(os.path.basename(path))[0]
    title = fname.replace('_', ' ').replace('-', ' ').strip().title()

    # Minimal front matter
    fm = [
        '---',
        f'title: "{title}"',
        'category: "Miscellaneous"',
        '---',
        ''
    ]

    # Build new body
    new_body = []
    if url:
        new_body.append(f"[🔗 Visit Site]({url})")
        new_body.append("")
    new_body.append(body)

    new_content = "\n".join(fm + new_body)

    # Overwrite
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Rebuilt: {path}")

def main():
    count = 0
    for root, _, files in os.walk(TOOLS_DIR):
        for fn in files:
            if fn.endswith('.md'):
                full = os.path.join(root, fn)
                force_rebuild(full)
                count += 1
    print(f"\nDone: Rebuilt {count} files.")

if __name__ == "__main__":
    main()
