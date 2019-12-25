#!/usr/bin/python

import sys
import urllib.request
import urllib.parse
from html.parser import HTMLParser
from bs4 import BeautifulSoup

url = 'https://www.facetofacegames.com/products/search?q='
url += str(sys.argv[1])

htmlResponse = urllib.request.urlopen(url)
htmlText = htmlResponse.read().decode('utf-8')

soup = BeautifulSoup(htmlText, 'html.parser')

#find all the divs on the page
divs = soup.find_all('div')
results = []

#search the divs for the first one with attributes that match a card result
# add
for div in divs:
    if div.attrs == {'class': ['product-price-qty']}:
        results.append(div)

print(results[0].text)
