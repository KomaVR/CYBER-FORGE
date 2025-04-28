import os
import requests
import time

GITHUB_API = "https://api.github.com"
TOKEN = os.getenv("CYBERFORGE_GH_TOKEN")
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}
TOPICS = ["hacking","pentest","security","vulnerability","exploit","reversing","malware","forensics","osint"]

def fetch_repos(topic, per_page=100, pages=3):
    repos = []
    for page in range(1, pages + 1):
        params = {
            "q": f"topic:{topic}",
            "sort": "stars",
            "order": "desc",
            "per_page": per_page,
            "page": page
        }
        r = requests.get(f"{GITHUB_API}/search/repositories", headers=HEADERS, params=params)
        r.raise_for_status()
        for item in r.json().get("items", []):
            repos.append(item["html_url"])
        time.sleep(1)  # avoid rate limit
    return repos

def main():
    out = set()
    for topic in TOPICS:
        print(f"[+] Fetching for topic: {topic}")
        out.update(fetch_repos(topic))
    final = list(out)[:1000]
    with open("sources.txt", "w") as f:
        for url in final:
            f.write(url + "\n")
    print(f"[+] sources.txt generated with {len(final)} entries.")

if __name__ == "__main__":
    main()
  
