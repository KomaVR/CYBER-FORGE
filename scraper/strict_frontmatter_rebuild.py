#!/usr/bin/env python3
import os
import re

# Path to your generated tool pages
TOOLS_DIR = os.path.join(os.path.dirname(__file__), "..", "site", "content", "tools")

def rebuild_frontmatter(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find front matter bounds
    if not lines or lines[0].strip() != '---':
        return False
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break
    if end_idx is None:
        # no closing delimiter
        return False

    # Extract original front matter and body
    fm_lines = lines[1:end_idx]
    body_lines = lines[end_idx+1:]

    # Parse title and category (if present)
    title = None
    category = None
    for line in fm_lines:
        if line.lower().startswith('title:'):
            # strip off 'title:' and quotes
            title = line.split(':',1)[1].strip().strip('"').strip("'")
        elif line.lower().startswith('category:'):
            category = line.split(':',1)[1].strip().strip('"').strip("'")

    # Fallback if missing
    if not title:
        # Use filename (without extension) as title
        title = os.path.splitext(os.path.basename(path))[0]
    if not category:
        category = "Miscellaneous"

    # Build brand-new front matter
    new_fm = [
        '---\n',
        f'title: "{title}"\n',
        f'category: "{category}"\n',
        '---\n',
        '\n'
    ]

    # Prepend original front matter lines that aren't url-related into body
    # And also catch any removed url lines
    extra = []
    for line in fm_lines:
        if re.match(r'^\s*url\s*:', line, re.IGNORECASE):
            # convert url to markdown link
            url = line.split(':',1)[1].strip().strip('"').strip("'")
            extra.append(f'[🔗 External Link]({url})\n\n')
        else:
            # put other fm lines into a comment block
            extra.append(f'<!-- {line.rstrip()} -->\n')
    # Append body
    new_body = extra + body_lines

    # Write back
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_fm + new_body)
    print(f"Rebuilt front matter: {path}")
    return True

def main():
    fixed = 0
    for root, _, files in os.walk(TOOLS_DIR):
        for fn in files:
            if fn.endswith('.md'):
                full = os.path.join(root, fn)
                if rebuild_frontmatter(full):
                    fixed += 1
    print(f"\nDone. Rebuilt front matter in {fixed} files.")

if __name__ == "__main__":
    main()
