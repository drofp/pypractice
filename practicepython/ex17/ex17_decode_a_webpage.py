#!/usr/bin/env python3

"""Example 17 from https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
==========================
- Retrieve and print out all the titles from the NY Times homepage:
https://www.nytimes.com/

Useful Tutorials:
https://realpython.com/python-web-scraping-practical-introduction/
https://www.dataquest.io/blog/web-scraping-tutorial-python/
http://altitudelabs.com/blog/web-scraping-with-python-and-beautiful-soup/

Useful Code:
https://stackoverflow.com/questions/45062534/how-to-grab-all-headers-from-a-website-using-beautifulsoup
https://github.com/ireapps/first-web-scraper/blob/master/scrapers/crime/scrape.py

For Reference:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
http://www.pythonforbeginners.com/python-on-the-web/beautifulsoup-4-python/

Parsers:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#differences-between-parsers
"""

import re

import requests
from bs4 import BeautifulSoup

def retrieve_html(url):
    req = requests.get(url)
    req_html = req.text
    return req_html

def get_titles(url):
    req_html = retrieve_html(url)
    soup = BeautifulSoup(req_html, "html.parser")
    # titles = soup.find_all('h1') # Runs MUCH slower than regex equivalent
    titles = soup.find_all(re.compile('^h[1-6]$'), attrs={"class": "story-heading"})

    return titles

def main():
    # print(retrieve_html("https://www.nytimes.com/")) # test requests functionality

    for title in get_titles("https://www.nytimes.com/"):
        print(title.text.strip())

if __name__ == "__main__":
    main()
