import requests
from bs4 import BeautifulSoup
from requests import get

url = 'https://visitdata.org/bydatesel/California/Marin%20County/ALL?datafilename=raw'
response = get(url)
print(response.text)

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

containers = html_soup.find_all('div', class_ = 'tabulator-cell')
print(type(containers))
print(len(containers))