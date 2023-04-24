import requests
from bs4 import BeautifulSoup
import pandas as pd

# retrieve info
urls = ['http://quotes.toscrape.com/page/1/', 'http://quotes.toscrape.com/page/2/', 'http://quotes.toscrape.com/page/3/', 'http://quotes.toscrape.com/page/4/', 'http://quotes.toscrape.com/page/5/']

# extract info
quotes = []
authors = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    quotes.append([quote.get_text() for quote in soup.findAll("span", {"class": "text"})])
    authors.append([author.get_text() for author in soup.findAll("small", {"class": "author"})])

# formulate info
quotes_updated = []
for inner_list in quotes:
    for quote in inner_list:
        quotes_updated.append(quote)

authors_updated = []
for inner_list in authors:
    for author in inner_list:
        authors_updated.append(author)

data = {"QUOTES": quotes_updated, "AUTHORS": authors_updated}

pd.set_option('display.max_colwidth', 100)
pd.set_option("colheader_justify", 'center')
table = pd.DataFrame(data)
print(table)
