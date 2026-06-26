# print('i be workin')

from io import StringIO

import pandas as pd
import requests
from bs4 import BeautifulSoup
import pprint

url = "https://en.wikipedia.org/wiki/List_of_regional_dishes_of_the_United_States"

headers = {
    "User-Agent": "regional_foods_scraper/1.0 (bmccarthy90@gmail.com)"
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")

page = pd.read_html(StringIO(str(soup)))

# container = soup.find("div", class_="mw-page-container-inner")
table = soup.find("table", class_="wikitable sortable")

rows = []

for tr in soup.find_all("tr", class_="anchor"):
    cells = tr.find_all("td")
    if len(cells) < 5:
        continue

    image_tag = cells[0].find("img")
    image_url = "https:" + image_tag["src"] if image_tag else ""

    dish = cells[1].get_text(strip=True)
    region = cells[2].get_text(strip=True)
    location = cells[3].get_text(strip=True)
    description = cells[4].get_text(strip=True)

    rows.append({
        "dish": dish,
        "region": region,
        "location": location,
        "description": description,
        "image_url": image_url
    })
pprint.pp(rows)

# df = pd.DataFrame(rows)

# print(df)
# print(f"Found {len(table)} tables")
# for i, df in enumerate(tables):
#     print(f"\nTable {i}: {df.shape}")
#     print(df.head(2))

# correct Brand Account column for pd.read_html:
# for t in soup.select('[title="Yes"]'):
#     t.replace_with("Yes")

# df = pd.read_html(StringIO(str(soup)))[0].fillna("")
# print(df)