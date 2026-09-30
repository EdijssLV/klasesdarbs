import requests
import re
from bs4 import BeautifulSoup


url = "https://www.rimi.lv/e-veikals/lv/produkti/gala-zivis-un-gatava-kulinarija/c/SH-6"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
)

response.raise_for_status()


def scrape():
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("li", class_="product-grid__item")

    for product in products:

        title_element = product.find("p", class_="card__name")
        
        if not title_element:
            continue

        title = title_element.get_text(strip=True)
        match = re.search(r"^(.*?)\s*(\d+(?:[.,]\d+)?\s*(?:g|kg|ml|l))\s*$", title, flags=re.IGNORECASE)

        if match:
            title = match.group(1).strip()
            weight = match.group(2).strip()


        price_div = product.find("div", class_="price-tag card__price")
        if not price_div:
            continue
        price_element = price_div.find("span", class_="sr-only")

        if not price_element:
            continue

        price_text = price_element.get_text(" ", strip=True)
        price = float(price_text.split("€")[0].strip())
        
        
        print(title)
        print(price)
        print(weight)
        print("---")


scrape()
