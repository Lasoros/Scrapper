from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.find_all("span" , attrs = {"class" : "text" }) 
# Inspect item on page you want to scrape. <span class = "text" itemprop="text">
authors = soup.find_all("small" , attrs = {"class" : "author"})
# Inspect item on page you want to scrape. <small class = "author" itemprop="author">


file = open("scrape_test_quotes.csv" , "w")
writer = csv.writer(file)

writer.writerow(["Quotes" , "Authors"])


for quote , author in zip(quotes , authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text , author.text])
file.close()

# for quote in quotes :
#     print(quote.text)

# for author in authors :
#     print(author.text)
# No longer needed as the above code takes both using the zip function