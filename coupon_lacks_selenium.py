from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://www.dontpayfull.com/at/shopbeam.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

codes = soup.find_all( "span" ,  attrs = {"class" : "code-action" }) 
# Inspect item on page you want to scrape. <span class = "text" itemprop="text">
# authors = soup.find_all("small" , attrs = {"class" : "author"})
# # Inspect item on page you want to scrape. <small class = "author" itemprop="author">


file = open("coupons_test.csv" , "w")
writer = csv.writer(file)

writer.writerow(["Codes"])


for code in codes:
    print(code.text)
    writer.writerow([code.text])
file.close()