# Search for a book in the oba API
# then pass this image to the imagga ML image analysis

from settings import *
import requests #install from: http://docs.python-requests.org/en/master/
from requests_xml import XMLSession
import json


import requests #install from: http://docs.python-requests.org/en/master/

# Your OBA_API_Key gets loaded from the .env file in settings.py

# The query parameters: (update according to your search query)
q = "hacking" # the search query. Change the hacking for something else to change the query.
pageSize = 1 # one result for now

query = "https://zoeken.oba.nl/api/v1/search/?authorization={}&q={}&pagesize={}".format(OBA_API_Key, q, pageSize)

session = XMLSession()
result = session.get(query)

# the oba API returns an XML document.
# requests_xml allows us to query/search the XML with xpath.
# get the cover image from the XML
image_url =  result.xml.xpath('//coverimage[2]/text()', first=True)

print( "cover image: " + image_url )

# now send the image to the ML algorithm
response = requests.get('https://api.imagga.com/v2/tags?image_url=%s' % image_url,
                        auth=(imagga_api_key, imagga_api_secret))

print( json.dumps( response.json(), indent=2 ) )

#the response looks like this:
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
result = response.json();
for tag in result['result']['tags']:
	print( tag['tag']['en'] )
