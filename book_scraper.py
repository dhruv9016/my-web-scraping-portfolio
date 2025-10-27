import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_ = "product_pod")

titles, prices, ratings = [], [], []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_ = "price_color").text
    rating = book.p["class"][1]

    titles.append(title)
    prices.append(price)
    ratings.append(rating)

print(titles)

import pandas as pd

df = pd.DataFrame({"Title": titles,
                   "Price": prices,
                   "Rating": ratings})

df.to_csv("books.csv", index = False,
          sep= ";")

print("Data Saved to books_csv")