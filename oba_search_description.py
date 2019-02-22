# Search for a book in the oba API
# then pass this image to the imagga ML image analysis
import sys
from settings import *
import requests #install from: http://docs.python-requests.org/en/master/
import xmltodict
import json

# Your OBA_API_Key gets loaded from the .env file in settings.py

# The query parameters: (update according to your search query)
q = "hacking" # the search query. Change the hacking for something else to change the query.
pageSize = 1 # one result for now

query = "https://zoeken.oba.nl/api/v1/search/?authorization={}&q={}&pagesize={}".format(oba_api_key, sys.argv[1], pageSize)
result = requests.get(query)

# the oba API returns an XML document. we convert the xml formatted file to json, which is "easier" to read and a more widespread format
data = xmltodict.parse(result.text)

# uncomment this to print the full result
# print(json.dumps(data, indent=4, sort_keys=True))

# get the image url
for k,v in data['aquabrowser']['results'].items():
  image_url = v['coverimages']['coverimage'][-1]['#text']
  print("cover image: " + image_url)

# now send the image to the ML algorithm
response = requests.get('https://api.imagga.com/v2/tags?image_url=' + image_url,
                        auth=(imagga_api_key, imagga_api_secret))

print(json.dumps(response.json(), indent=4, sort_keys=True))

# the response looks like this:
'''
{
  "result": {
    "tags": [
      {
        "confidence": 7.65564250946045,
        "tag": {
          "en": "god"
        }
      },
      {
        "confidence": 7.65040016174316,
        "tag": {
          "en": "card"
        }
      }
    ]
  },
  "status": {
    "text": "",
    "type": "success"
  }
}
'''

# result = response.json();
# print(json.dumps(result, indent=4, sort_keys=True))

# for tag in result['result']['tags']:
#   print( tag['tag']['en'] )
