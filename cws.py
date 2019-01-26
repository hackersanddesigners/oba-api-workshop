# Search for an image on Contextual websearch via the command line
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
q = "black" #the search query
pageNumber = 1 #the number of requested page
pageSize = 1 #the size of a page
autoCorrect = False #autoCorrectspelling
safeSearch = False #filter results for adult content

response=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI?q={}&pageNumber={}&pageSize={}&autocorrect={}&safeSearch={}".format(q, pageNumber, pageSize, autoCorrect,safeSearch),
headers={
"X-RapidAPI-Key": RapidAPI_Key
}
).json()

value = response["value"]
url = value[0]["url"]
print(url)