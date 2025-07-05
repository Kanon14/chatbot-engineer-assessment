import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

def extract_from_google_maps(url):
    try:
        # Step 1: Request the page
        response = requests.get(url, timeout=10, headers={
            "User-Agent": "Mozilla/5.0"
        }, allow_redirects=True)

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n")

        row = {}

        # 📍 Extract store name and location (This section works)
        meta_tag = soup.find("meta", property="og:site_name")
        if meta_tag:
            content = meta_tag.get("content", "")
            parts = content.split("·")
            row["store_name"] = parts[0].strip()
            row["location"] = parts[1].strip() if len(parts) > 1 else "Not found"
        else:
            row["store_name"] = "Not found"
            row["location"] = "Not found"

        # 🕒 Extract today's operating hour from raw pattern 
        today = datetime.today()
        y, m, d = today.year, today.month, today.day
        pattern = rf"\[{y},{m},{d}\],\[\[\"([^\"]*am[^\"]*pm[^\"]*)\""
        print(pattern)
        hour_match = re.search(pattern, text)
        print(hour_match)
        row["today_hour"] = hour_match.group(1) if hour_match else "Not found"

        # 🧰 Extract services under "Service options"
        services = []
        lines = text.split("\n")
        for i, line in enumerate(lines):
            if "Service options" in line:
                for j in range(i + 1, i + 6):
                    if j < len(lines):
                        s = lines[j].strip()
                        if s:
                            services.append(s)
                break
        row["services"] = services if services else ["Not found"]

        return row

    except Exception as e:
        print("❌ Error fetching URL:", e)
        return {
            "store_name": "Error",
            "location": "Error",
            "today_hour": "Error",
            "services": ["Error"]
        }

def main():
    # 📄 Load the first link from CSV
    df = pd.read_csv("data/zus_all_direction_links.csv")

    if df.empty:
        print("⚠️ CSV file is empty.")
        return

    test_link = df.loc[0, "map_link"]
    print("🔗 Testing link:", test_link)

    result = extract_from_google_maps(test_link)

    # 🖨️ Output
    print("\n✅ Extracted Info:")
    print("Store Name:", result["store_name"])
    print("Location:", result["location"])
    print("Today’s Hour:", result["today_hour"])
    print("Services:", ", ".join(result["services"]))

if __name__ == "__main__":
    main()
