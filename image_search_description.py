from settings import *
import requests #install from: http://docs.python-requests.org/en/master/
import json

q = "word" #the search query
pageNumber = 1 #the number of requested page
pageSize = 1 #the size of a page
autoCorrect = False #autoCorrectspelling
safeSearch = True #filter results for adult content

response=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI?q={}&pageNumber={}&pageSize={}&autocorrect={}&safeSearch={}".format(q, pageNumber, pageSize, autoCorrect,safeSearch),
	headers={
		"X-RapidAPI-Key": RapidAPI_Key
	}
).json()

image_url = response["value"][0]["url"] # get the image url from the response
print( "Image found: " + image_url );

# now send the image to the ML algorithm
response = requests.get('https://api.imagga.com/v2/tags?image_url=%s' % image_url,
                        auth=(imagga_api_key, imagga_api_secret))

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
