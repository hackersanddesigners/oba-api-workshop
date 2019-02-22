# Search for an image on Contextual websearch via the command line
# Outputs the URL of the image found
import sys
import json
from settings import *
from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)

import requests #install from: http://docs.python-requests.org/en/master/

# Your RapidAPI_Key gets loaded from the .env file in settings.py

#The query parameters: (update according to your search query)
q = "world" #the search query
pageNumber = 1 #the number of requested page
pageSize = 1 #the size of a page
autoCorrect = False #autoCorrectspelling
safeSearch = False #filter results for adult content

response=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI?q={}&pageNumber={}&pageSize={}&autocorrect={}&safeSearch={}".format(sys.argv[1], pageNumber, sys.argv[2], autoCorrect,safeSearch),
headers={
"X-RapidAPI-Key": rapidapi_key
}
).json()

# print(json.dumps(response, indent=4, sort_keys=True))

result = response["value"]

for item in result:
  url = item['url']
  print('→ ' + url + '\n')
