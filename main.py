import requests
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

    print(products)

scrape()