import os
import yaml

content_dir = '../site/content/tools'

for root, _, files in os.walk(content_dir):
    for filename in files:
        if filename.endswith('.md'):
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                # Only process if file has frontmatter
                if lines and lines[0].strip() == '---':
                    frontmatter = []
                    body = []
                    in_frontmatter = True

                    for line in lines[1:]:
                        if line.strip() == '---' and in_frontmatter:
                            in_frontmatter = False
                            continue
                        if in_frontmatter:
                            frontmatter.append(line)
                        else:
                            body.append(line)

                    try:
                        yaml.safe_load(''.join(frontmatter))  # Try to parse
                    except yaml.YAMLError:
                        print(f"Skipping broken YAML in file: {filepath}")
                        continue  # Skip broken files

                    # (Optional) You could also modify or reformat the frontmatter here if needed
                    # Save the file again
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write('---\n')
                        f.writelines(frontmatter)
                        f.write('---\n')
                        f.writelines(body)
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
