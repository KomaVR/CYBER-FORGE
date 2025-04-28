import sqlite3, os
DB_PATH = 'tools.db'
CONTENT_DIR = '../site/content/tools'

template = """---
title: "{name}"
description: "{desc}"
url: "{url}"
category: "{cat}"
---

"""

def generate_hugo_content():
    os.makedirs(CONTENT_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name, description, url, category FROM tools")
    rows = c.fetchall()
    for name, desc, url, cat in rows:
        fname = name.lower().replace(' ', '_').replace('/', '_') + '.md'
        with open(os.path.join(CONTENT_DIR, fname), 'w', encoding='utf-8') as f:
            f.write(template.format(name=name, desc=desc.replace('"','\\"'), url=url, cat=cat))
    print(f"[+] Generated {len(rows)} Hugo pages.")
    conn.close()

if __name__ == "__main__":
    generate_hugo_content()
  
