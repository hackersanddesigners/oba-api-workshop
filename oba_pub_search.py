# -- search for a book in the oba api
import os
import sys
import requests
import xmltodict
import json
import time
import settings

# -- get dict of python environment variables loaded from `.env`
env = settings.env()

result_index = []
for i in range(1, int(sys.argv[2])):
  query = "https://zoeken.oba.nl/api/v1/search/?authorization=" + env['oba_api_key'] + "&q=publisher%3A" + sys.argv[1] + "&page=" + str(i)
  result = requests.get(query)
  data = result.text
  data = xmltodict.parse(data)['aquabrowser']

  for k, v in data.items():
    if (k == 'results'):
      for item in v['result']:
        result_index.append(item)

# print(json.dumps(data, indent=4, sort_keys=True))
# print('---')

timestamp = time.strftime("%Y-%m-%d-%H%M%S")
filename = sys.argv[1] + '_' + timestamp
with open('dump/%s.json' % filename, 'w') as fp:
    json.dump(result_index, fp)
    print('dumped to json!')
