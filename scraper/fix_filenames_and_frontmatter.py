# scraper/fix_filenames_and_frontmatter.py

import os
import re
import yaml

def sanitize_filename(filename):
    # Remove invalid characters from filenames
    return re.sub(r'[^a-zA-Z0-9\-_.]', '_', filename)

def fix_front_matter(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if content.startswith('---'):
            parts = content.split('---')
            if len(parts) >= 3:
                front_matter_raw = parts[1]
                body = '---'.join(parts[2:])
                
                front_matter = yaml.safe_load(front_matter_raw)
                if isinstance(front_matter, dict):
                    # Force all fields to strings properly
                    fixed_fm = {}
                    for key, value in front_matter.items():
                        if isinstance(value, str):
                            fixed_fm[key] = value.replace('"', "'")
                        else:
                            fixed_fm[key] = value
                    new_front_matter = yaml.safe_dump(fixed_fm, allow_unicode=True)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write('---\n' + new_front_matter + '---\n' + body.strip())
    except Exception as e:
        print(f"Error fixing front matter in {filepath}: {e}")

def main():
    content_dir = 'site/content/tools'

    for filename in os.listdir(content_dir):
        old_path = os.path.join(content_dir, filename)
        if filename.endswith('.md'):
            # Fix front matter inside file
            fix_front_matter(old_path)
            
            # Sanitize filename
            new_filename = sanitize_filename(filename)
            new_path = os.path.join(content_dir, new_filename)
            
            if old_path != new_path:
                print(f"Renaming {filename} -> {new_filename}")
                os.rename(old_path, new_path)

if __name__ == "__main__":
    main()
