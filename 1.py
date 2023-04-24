import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(response.content, 'html.parser')

quotes = [quote.get_text() for quote in soup.findAll("span", {"class": "text"})]
authors = [author.get_text() for author in soup.findAll("small", {"class": "author"})]
data = {"QUOTES":quotes, "AUTHOR":authors}

pd.set_option('display.max_colwidth', None)
pd.set_option("colheader_justify", 'center')
table = pd.DataFrame(data)
print(table)
