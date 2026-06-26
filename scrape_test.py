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

# not needed
# page = pd.read_html(StringIO(str(soup)))

# container = soup.find("div", class_="mw-page-container-inner")
table = soup.find("table", class_="wikitable sortable")

rows = []
current_title = "regional dishes of the united states"
# for type_title in soup.find_all("div", class_="mw-heading mw-heading3"):
    
#     title = type_title.find_all("h3")
#     print(title)

# make a type column for each table?
# tr is table row? td is table data
for element in soup.find_all(["tr", 'h3']):
    # print(tr)
    if element.name == "h3":
        current_h3 = element.get_text(strip=True)
        current_title = current_h3
    
    elif element.name == "tr" and element.has_attr("class") and "anchor" in element["class"]:
        cells = element.find_all("td")
        # skip if 
        # if len(cells) < 5:
        #     continue
        image_tag = cells[0].find("img")
        image_url = "https:" + image_tag["src"] if image_tag else ""

        dish = cells[1].get_text(strip=True)
        region = cells[2].get_text(strip=True)
        location = cells[3].get_text(strip=True)
        description = cells[4].get_text(strip=True)
        
        rows.append({
            "type" : current_title,
            "dish": dish,
            "region": region,
            "location": location,
            "description": description,
            "image_url": image_url
        })
    # pprint.pp(rows[0])
pprint.pp(len(rows))

# df = pd.DataFrame(rows)
# pprint.pp(df)
# df.to_csv("regional_foods_1.csv", index=False)
# concat description
# put rows into dataframe

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