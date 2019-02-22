# search for a book in the oba api
from settings import *
from os.path import join, dirname
from dotenv import load_dotenv
import sys
import requests
import xmltodict
import json

# get the api keys from the .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# your oba_api_key gets loaded from the .env file in settings.py

# the query parameters: (update according to your search query)
q = "hacking"
pagesize = 1

query = "https://zoeken.oba.nl/api/v1/search/?authorization=" + oba_api_key + "&q=" + sys.argv[1] + "&pagesize=" + sys.argv[2]

result = requests.get(query)
data = result.text
data = xmltodict.parse(data)

# print(json.dumps(data, indent=4, sort_keys=True))
# print('---')

for k,v in data['aquabrowser']['results'].items():
  # print(json.dumps(v, indent=4, sort_keys=True))
  if 'titles' in v:
    title = v['titles']['title']['#text']
    print('title: ' + title + '\n')

    cover = v['coverimages']['coverimage']
    print('cover:')
    for img in cover:
      print('  → ' + img['#text'])

    print('\n--\n')
  else:
    for entry in v:
      title = entry['titles']['title']
      if '#text' in title:
        print('title: ' + title['#text'] + '\n')
      else:
        for t in title:
          print('title: ' + t['#text'] + '\n')

      cover = entry['coverimages']['coverimage']
      # print(cover)
      print('cover:')
      for img in cover:
        print('  → ' + img['#text'])

      print('\n--\n')
