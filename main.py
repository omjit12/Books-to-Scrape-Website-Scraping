import requests
import pandas as pd 
from bs4 import BeautifulSoup

main_url = "https://books.toscrape.com/catalogue/page-{}.html"

product_name = []
product_price = []
product_availabilty = []
product_rating = []

for page in range(1,51):
    print(f"Scraping page {page}")

    url = main_url.format(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    # print(soup.prettify())

    books = soup.find_all("article",class_="product_pod")

    for book in books:
        name = book.h3.a["title"]
        product_name.append(name)

        price = book.find("p",class_="price_color").text
        product_price.append(price)

        availabilty = book.find("p",class_="instock availability").text.strip()
        product_availabilty.append(availabilty)

        rating = book.find("p", class_="star-rating")["class"][1]
        product_rating.append(rating)

df = pd.DataFrame({
    "BOOK_NAME": product_name,
    "PRICE": product_price,
    "RATING": product_rating,
    "AVAILABILITY": product_availabilty
})

print(df.head())

df.to_csv("books_to_scrape.csv")