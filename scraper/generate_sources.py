import os
import requests
import time

TOKEN = os.getenv("CYBERFORGE_GH_TOKEN")
if not TOKEN:
    raise RuntimeError("Missing CYBERFORGE_GH_TOKEN environment variable.")

HEADERS = {"Authorization": f"token {TOKEN}"}
GITHUB_API = "https://api.github.com"
TOPICS = ["hacking", "pentest", "security", "vulnerability", "exploit", "reverse-engineering", "malware", "osint", "ctf", "forensics"]
OUTPUT_FILE = "sources.txt"

def search_repositories(topic):
    url = f"{GITHUB_API}/search/repositories?q=topic:{topic}&sort=stars&order=desc&per_page=100"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code} - {response.text}")
    return [repo['html_url'] for repo in response.json().get('items', [])]

def main():
    print("Starting repository scrape...")
    all_urls = set()

    for topic in TOPICS:
        print(f"Searching for topic: {topic}")
        urls = search_repositories(topic)
        all_urls.update(urls)
        time.sleep(2)  # Be nice to GitHub API

    print(f"Found {len(all_urls)} repositories.")
    with open(OUTPUT_FILE, "w") as f:
        for url in sorted(all_urls):
            f.write(url + "\n")
    print(f"Sources written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
    
