import os
import re

def fix_markdown(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                if "---" not in content:
                    continue

                parts = content.split("---")
                if len(parts) < 3:
                    continue

                front_matter, body = parts[1], parts[2]

                # Check if any https:// URL is still in front matter
                if "http://" in front_matter or "https://" in front_matter:
                    print(f"Fixing {path}...")

                    # Extract URL if it exists
                    url_match = re.search(r'(http[s]?://[^\s"\']+)', front_matter)
                    if url_match:
                        url = url_match.group(1)

                        # Remove entire line with the URL
                        front_matter = re.sub(r'^.*(http[s]?://[^\s"\']+).*$', '', front_matter, flags=re.MULTILINE)

                        # Add link to body
                        link = f"[Visit Website]({url})\n\n"
                        body = link + body.lstrip()

                        # Rebuild full content
                        new_content = f"---\n{front_matter.strip()}\n---\n{body}"

                        with open(path, "w", encoding="utf-8") as f:
                            f.write(new_content)

if __name__ == "__main__":
    fix_markdown("./site/content")
