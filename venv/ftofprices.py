#!/usr/bin/python

import sys
import argparse
import urllib.request
import urllib.parse
from html.parser import HTMLParser
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("cardName", type=str, help="Card name specified, delimited by underscores(_).")
parser.add_argument('-l', '--limit', type=int, default=20, help='Limit list size.')
args = parser.parse_args()

url = 'https://www.facetofacegames.com/products/search?q='
url += str(sys.argv[1]).replace("_", "+")

htmlResponse = urllib.request.urlopen(url)
htmlText = htmlResponse.read().decode('utf-8')
soup = BeautifulSoup(htmlText, 'html.parser')
    
# this is the order form on each list item that is returned from the search
forms = soup.findAll("form", attrs={"class" : "add-to-cart-form"}, limit=3*args.limit) # is buggy when out of stock results come back.
# the form tag contains all useful card info, example form tag below:
    # <form class="add-to-cart-form" data-vid="457187"
    #  data-name="Rampant Growth" data-id="89787" data-price="CAD$ 0.49"
    #  data-category="Magic 2010" data-variant="NM-Mint, English">

# Loop through each form result, filter out repeated results for each set.
# The best condition will always be listed first
currentSet = ""
print("\n\n")
for form in forms:
    # use the data vid tag to filter out results that are out of stock
    # they won't have the appropriate data
    if form["data-vid"] == "":
        # item is out of stock, different tag structure
        name = form.find('a')["href"].split("/")
        print(name[(len(name))-2] + " -- out of stock -- " + form.find("span").text.strip())
        continue

    if currentSet != form["data-category"]:
        currentSet = form["data-category"]
        print(form["data-name"] + " -- " + form["data-category"]
        + (" -- " + form["data-price"]))
    