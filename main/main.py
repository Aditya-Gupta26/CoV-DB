import requests
from bs4 import BeautifulSoup
url="https://news.google.com/rss/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
#Get the HTML
resp = requests.get(url)

#Parse the HTML
soup = BeautifulSoup(resp.content, features="xml")
#print(soup.prettify())
items = soup.findAll('item')
news_items = []
for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['description'] = item.description.text
    news_item['link'] = item.link.text
    news_item['pubDate'] = item.pubDate.text
    news_items.append(news_item)
    
print(news_items)

import json
import sys

sys.stdout = open('declare.js','w')
jsonobj = json.dumps(news_items)

print("var jsonstr = '{}'", format(jsonobj))