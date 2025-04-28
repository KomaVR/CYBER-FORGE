from generate_sources import main as gen_src
from scrape import scrape_sources
from generate_hugo_content import generate_hugo_content

def main():
    print("[*] Generating source list...")
    gen_src()
    print("[*] Scraping and classifying tools...")
    scrape_sources()
    print("[*] Generating Hugo content...")
    generate_hugo_content()
    print("[+] Bootstrap complete. Run `cd ../site && hugo server -D`")

if __name__ == "__main__":
    main()
