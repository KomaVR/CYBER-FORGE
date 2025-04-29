import os
import re
import yaml

def fix_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.strip().startswith('---'):
        print(f"Skipping (no frontmatter): {filepath}")
        return

    # Split frontmatter and body
    try:
        parts = content.split('---')
        if len(parts) < 3:
            print(f"Invalid frontmatter in {filepath}")
            return
        front_matter = parts[1]
        body = '---'.join(parts[2:])

        fm_data = yaml.safe_load(front_matter) or {}

        # Find [Visit Website](URL)
        match = re.search(r'\[Visit Website\]\((.*?)\)', body, re.IGNORECASE)
        if match:
            url = match.group(1).strip()
            if url:
                fm_data['external_link'] = url

            # Remove the [Visit Website] markdown line
            body = re.sub(r'\[Visit Website\]\(.*?\)', '', body, flags=re.IGNORECASE).strip()

        # Rebuild .md file
        new_content = "---\n" + yaml.safe_dump(fm_data, sort_keys=False) + "---\n" + body.strip() + "\n"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Fixed: {filepath}")

    except Exception as e:
        print(f"Failed to fix {filepath}: {e}")

def main():
    tools_dir = "../site/content/tools"

    for root, dirs, files in os.walk(tools_dir):
        for file in files:
            if file.endswith('.md'):
                fix_markdown_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
  
