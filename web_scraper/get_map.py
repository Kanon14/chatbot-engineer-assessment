import requests
import re
import csv
from bs4 import BeautifulSoup

def extract_direction_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator="\n")

    # Regex to match [Direction](ANY_LINK)
    matches = re.findall(r'\[Direction\]\((https?://[^\s)]+)\)', text)
    return matches

def main():
    all_links = set()

    for page in range(1, 23):  # Pages 1–22
        print(f"Scraping page {page}...")
        url = f"https://r.jina.ai/https://zuscoffee.com/category/store/kuala-lumpur-selangor/page/{page}/"
        links = extract_direction_links(url)
        all_links.update(links)

    # Save to CSV
    with open("data/zus_all_direction_links.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["map_link"])
        for link in sorted(all_links):
            writer.writerow([link])

    print(f"\n✅ Extracted {len(all_links)} unique [Direction] links.")

if __name__ == "__main__":
    main()