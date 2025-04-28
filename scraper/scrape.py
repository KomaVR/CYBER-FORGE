import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from db_utils import initialize_database, add_tool
from classify import classify_tool

SOURCE_FILE = 'sources.txt'
MAX_WORKERS = 8

def fetch(url):
    try:
        r = requests.get(url, timeout=8)
        return url, r.text if r.status_code == 200 else None
    except:
        return url, None

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    tools = []
    for li in soup.select('li'):
        a = li.find('a', href=True)
        if a and a['href'].startswith('http'):
            name = a.text.strip() or a['href'].split('/')[-1]
            url  = a['href']
            desc = li.text.replace(a.text, '').strip(' -–')
            tools.append((name, desc, url))
    return tools

def scrape_sources():
    initialize_database()
    with open(SOURCE_FILE) as f:
        urls = [u.strip() for u in f if u.strip() and not u.startswith('#')]
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(fetch, url): url for url in urls}
        for future in as_completed(futures):
            url, html = future.result()
            if html:
                for name, desc, link in parse(html):
                    cat = classify_tool(name, desc)
                    add_tool(name, desc, link, cat)
    print("[+] scrape complete.")

if __name__ == "__main__":
    scrape_sources()
  
