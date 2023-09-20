from bs4 import BeautifulSoup
import requests

url = 'https://shopmichaeljamessmith.com/'
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h2', {'class': 'SectionHeader__Heading SectionHeader__Heading--emphasize Heading u-h1'})
print(title)
