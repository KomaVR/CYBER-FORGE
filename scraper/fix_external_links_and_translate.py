#!/usr/bin/env python3
import os
import re
import yaml
import requests

LIBRETRANSLATE_URL = "https://libretranslate.de/translate"

def translate_text(text: str) -> str:
    """Translate any text to English using LibreTranslate."""
    if not text.strip():
        return text
    try:
        response = requests.post(LIBRETRANSLATE_URL, data={
            "q": text,
            "source": "auto",
            "target": "en",
            "format": "text"
        }, timeout=10)
        response.raise_for_status()
        return response.json()["translatedText"]
    except Exception as e:
        print(f"[WARN] Translation failed for: {text[:30]}…: {e}")
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

    fm = yaml.safe_load(raw_fm) or {}

    # Rename external_category → categories (list)
    if "external_category" in fm:
        fm["categories"] = [fm.pop("external_category")]

    # Extract external link from body
    m = re.search(r'\[Visit Website\]\((.*?)\)', body, re.IGNORECASE)
    if m:
        fm["external_link"] = m.group(1).strip()
        body = re.sub(r'\[Visit Website\]\(.*?\)', "", body, flags=re.IGNORECASE).strip()

    # Translate front matter
    for key in ["title", "description"]:
        if key in fm and isinstance(fm[key], str):
            fm[key] = translate_text(fm[key])

    if "categories" in fm and isinstance(fm["categories"], list):
        fm["categories"] = [translate_text(c) for c in fm["categories"]]

    # Translate body
    body = translate_text(body)

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
    
