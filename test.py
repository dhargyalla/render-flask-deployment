import requests
from bs4 import BeautifulSoup

url = "https://www.codewithtd.com/portfolio"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

cards = []
for card_div in soup.select(".card"):  # adjust selector based on actual HTML structure
    image = card_div.select_one("img.card-img-top")["src"]
    description = card_div.select_one(".card-text").get_text(strip=True)
    tags = [ span.get_text(strip=True) for span in card_div.select(".badge") ]
    link = card_div.select_one(".btn-group a")["href"]
    cards.append({
        "image": image,
        "description": description,
        "tags": tags,
        "link": link
    })

print(cards)
