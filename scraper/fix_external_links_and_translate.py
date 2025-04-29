#!/usr/bin/env python3
import os
import re
import yaml
from googletrans import Translator, constants

translator = Translator()

def translate_text(text: str) -> str:
    """Translate any text to English."""
    # Skip empty
    if not text.strip():
        return text
    # Use Googletrans to translate
    try:
        return translator.translate(text, dest="en").text
    except Exception as e:
        print(f"[WARN] Translation failed for text: {text[:30]}…: {e}")
        return text

def fix_markdown_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        print(f"SKIP (no front matter): {path}")
        return

    parts = content.split("---")
    if len(parts) < 3:
        print(f"SKIP (invalid front matter): {path}")
        return

    raw_fm = parts[1]
    body = "---".join(parts[2:]).strip()

    # Load front matter
    fm = yaml.safe_load(raw_fm) or {}

    # 1) Rename external_category → categories (list)
    if "external_category" in fm:
        fm["categories"] = [fm.pop("external_category")]

    # 2) Pull [Visit Website](URL) into external_link
    m = re.search(r'\[Visit Website\]\((.*?)\)', body, re.IGNORECASE)
    if m:
        fm["external_link"] = m.group(1).strip()
        body = re.sub(r'\[Visit Website\]\(.*?\)', "", body, flags=re.IGNORECASE).strip()

    # 3) Translate front-matter fields to English
    for key in ["title", "description"]:
        if key in fm and isinstance(fm[key], str):
            fm[key] = translate_text(fm[key])

    # Also translate each category if present
    if "categories" in fm and isinstance(fm["categories"], list):
        fm["categories"] = [translate_text(c) for c in fm["categories"]]

    # 4) Translate the body
    body = translate_text(body)

    # Reassemble the file
    new_fm = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    new_content = f"---\n{new_fm}\n---\n\n{body}\n"

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Fixed & translated: {path}")

def main():
    tools_dir = os.path.join(os.path.dirname(__file__), "..", "site", "content", "tools")
    for root, _, files in os.walk(tools_dir):
        for fn in files:
            if fn.endswith(".md"):
                fix_markdown_file(os.path.join(root, fn))

if __name__ == "__main__":
    main()
