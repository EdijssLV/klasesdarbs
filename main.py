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

        # TITLE
        try:
            title_element = product.find("p", class_="card__name")

            if not title_element:
                raise ValueError("Title not found")

            title = title_element.get_text(strip=True)

        except Exception as e:
            title = "N/A"
            print(f"Title error: {e}")


        # WEIGHT
        try:
            match = re.search(r"^(.*?)\s*(\d+(?:[.,]\d+)?\s*(?:g|kg|ml|l))\s*$", title, flags=re.IGNORECASE)

            if not match:
                raise ValueError("Weight not found")

            title = match.group(1).strip()
            weight = match.group(2).strip()

        except Exception as e:
            weight = "N/A"
            print(f"Weight error: {e}")


        # PRICE
        try:
            price_div = product.find("div", class_="price-tag card__price")

            if not price_div:
                raise ValueError("Price div not found")

            price_element = price_div.find("span", class_="sr-only")

            if not price_element:
                raise ValueError("Price element not found")

            price_text = price_element.get_text(" ",strip=True)

            price = float(price_text.split("€")[0].strip())

        except Exception as e:
            price = "N/A"
            print(f"Price error: {e}")


        # OUTPUT
        print(f"Title: {title}")
        print(f"Weight: {weight}")
        print(f"Price: {price}")
        print("---")


scrape()
