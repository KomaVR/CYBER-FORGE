import os
import re

def clean_hugo_markdown(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract front matter
                parts = content.split('---')
                if len(parts) < 3:
                    continue  # Skip if not valid front matter

                front_matter = parts[1]
                body = parts[2]

                # Search for url field
                match = re.search(r'url:\s*"(http[s]?://[^"]+)"', front_matter)
                if match:
                    url = match.group(1)
                    # Remove the url line
                    front_matter = re.sub(r'url:\s*"(http[s]?://[^"]+)"\n?', '', front_matter)

                    # Add link at the start of body
                    link_md = f"[Visit Website]({url})\n\n"
                    body = link_md + body.lstrip()

                    # Rebuild content
                    new_content = f"---{front_matter}---{body}"

                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                    print(f"Fixed: {filepath}")

if __name__ == "__main__":
    directory_to_fix = "./site/content"  # Adjust if needed
    clean_hugo_markdown(directory_to_fix)
