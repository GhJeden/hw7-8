import requests
import lxml
from bs4 import BeautifulSoup

url = "https://cash-backer.club/shops"

header = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"}

session = requests.session()

for j in range(1, 10):
    print(f"PAGE = {j}")
    with open("cashback.txt", "a", encoding="UTF-8") as file:
        file.write(f"{j}\n")
    url = f"https://cash-backer.club/shops?page={j}/"
    response = session.get(url, headers=header)
    print(response)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        allProduct = soup.find("div", class_="row col-lg-9 col-md-9 col-12")
        products = allProduct.find_all("div", class_="product-info")
        for i in range(len(products)):
            try:
                title = products[i].find("div", class_="shop-title").text.strip()
                cashback = products[i].find("div", class_="shop-rate").text.strip()
                with open("cashback.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{title} --->>> {cashback}\n")
            except:
                print(title, cashback)