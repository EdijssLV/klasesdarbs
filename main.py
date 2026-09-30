import requests
from bs4 import BeautifulSoup


url = "https://www.rimi.lv/e-veikals/lv/produkti/gala-zivis-un-gatava-kulinarija/c/SH-6"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text(separator="\n", strip=True)

print(text)
