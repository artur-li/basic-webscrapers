import requests
from bs4 import BeautifulSoup

# payload = {field: input}
payload = {'username': "adfdsfs", "password": "fdsf"}

# post payload to specified login url
response = requests.post("http://quotes.toscrape.com/login", payload)
print(response)
