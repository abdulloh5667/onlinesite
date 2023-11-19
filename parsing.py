import requests
from bs4 import BeautifulSoup

content = []

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

response = requests.get("https://elmakon.uz/uz/noutbuki-printery-kompyutery/noutbuki/", headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
main_product = soup.find("div", class_="grid-list")
block = main_product.find_all("div", class_="ty-column4")
for item in block:
    image = item.find("div", class_="ut2-gl__image").find("a").find("img")["src"]
    description = item.find("div", class_="ut2-gl__name").find("a").get_text()
    price = item.find("span", class_="ty-price-num").get_text() + " UZS"
    sale = item.find("p").get_text()

    content.append({
        "Rasm": image,
        "Tavsif": description,
        "Narxi": price,
        "Muddatli to'lov": sale
    })


print(content)








