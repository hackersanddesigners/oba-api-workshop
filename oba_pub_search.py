# search for a book in the oba api
from settings import *
from os.path import join, dirname
from dotenv import load_dotenv
import sys
import requests
import xmltodict
import json
import time

# get the api keys from the .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# your oba_api_key gets loaded from the .env file in settings.py

for i in range(int(sys.argv[2])):
  query = "https://zoeken.oba.nl/api/v1/search/?authorization=" + oba_api_key + "&q=publisher%3A" + sys.argv[1] + "&page=" + str(i)
  result = requests.get(query)
  data = result.text
  data = xmltodict.parse(data)['aquabrowser']

  result_index.append(data)

print(json.dumps(data, indent=4, sort_keys=True))
print('---')

timestamp = time.strftime("%Y-%m-%d-%H%M%S")
filename = sys.argv[1] + '_' + timestamp
with open('dump/%s.json' % filename, 'w') as fp:
    json.dump(result_index, fp)
    print('dumped to json!')
