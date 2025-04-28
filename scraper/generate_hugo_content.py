import sqlite3
import os
import re

DB_PATH = 'tools.db'
CONTENT_DIR = '../site/content/tools'

template = """---
title: "{name}"
description: "{desc}"
url: "{url}"
category: "{cat}"
---
"""

def safe_filename(name):
    # Remove unsafe URL parts (e.g., ?jwt=...)
    name = name.split('?')[0]
    # Replace non-word characters with underscore
    name = re.sub(r'[^\w\-]', '_', name)
    # Trim to 100 chars max to avoid Linux file name limits
    return name[:100]

def generate_hugo_content():
    os.makedirs(CONTENT_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name, description, url, category FROM tools")
    rows = c.fetchall()
    for name, desc, url, cat in rows:
        fname = safe_filename(name.lower()) + '.md'
        filepath = os.path.join(CONTENT_DIR, fname)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(template.format(
                name=name,
                desc=desc.replace('"','\\"'),
                url=url,
                cat=cat
            ))
    print(f"[+] Generated {len(rows)} Hugo pages.")
    conn.close()

if __name__ == "__main__":
    generate_hugo_content()
