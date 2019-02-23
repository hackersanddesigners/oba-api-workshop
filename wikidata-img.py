# search for an image on the wikidata database,
# feed the image to a Machine Learning API to get a description of it

import sys
from settings import *
import requests
import json
import random
from bs4 import BeautifulSoup

s = requests.session()
url = "https://en.wikipedia.org/w/api.php"
params = {
    "action":"query",
    "format":"json",
    "prop": "images",
    "titles": sys.argv[1],
}

r = s.get(url=url, params=params)
data = r.json()
# print(json.dumps(data, indent=4, sort_keys=True))
result = r.json()

for k,v in result['query']['pages'].items():
  # print(json.dumps(v['images'], indent=4, sort_keys=True))
  imgs = []
  for image in v['images']:
    if '.jpg' in image['title']:
      print(image)
      imgs.append(image['title'])

  print(imgs)

  print('---\nrandomly selected ↓')
  img = random.choice(imgs)
  img = img

img_url = 'https://www.mediawiki.org/wiki/' + img
print(img_url)

r = s.get(url=img_url)
data = r.text

soup = BeautifulSoup(data, "html.parser")
img_deeplink = soup.find('a', class_="internal")
print('---')
print('https:' + img_deeplink['href'].replace(' ', '_'))
image_url = 'https:' + img_deeplink['href']

# now send the image to the ML algorithm
response = requests.get('https://api.imagga.com/v2/tags?image_url=' + image_url,
                        auth=(imagga_api_key, imagga_api_secret))

print(response.url)

print(json.dumps(response.json(), indent=4, sort_keys=True))
