import requests as reqs
from bs4 import BeautifulSoup as BS
import time

Messier_Years = {}
Messier_Discoverers = {}

'''     #(Old Code trying to read a already downloaded HTML File)
with open("List of discoverers of Messier objects - Wikipedia.html", "r", encoding="utf-8") as f:
    htmlpage = f.read()
'''

Unique_Resource_Locator = "https://en.wikipedia.org/wiki/List_of_discoverers_of_Messier_objects"
Resource = reqs.get(Unique_Resource_Locator)

soup = BS(Resource.text, "html.parser")

tables = soup.find_all("table")
table = None
for t in tables:
    headers = [th.get_text(strip=True).lower() for th in t.find_all("th")]
    if "messier" in headers and "year" in headers:
        table = t
        break

if not table:
    raise Exception("Could not find the Messier table!")

rows = table.find_all("tr")

for i in rows:
    cell = i.find_all("td")
    if (len(cell) >= 4):
        Messier_Num = cell[0].get_text(strip=True)
        Messier_Disco_Year = cell[3].get_text(strip=True)
        Messier_Years[Messier_Num] = Messier_Disco_Year

time.sleep(1)
print(Messier_Years)