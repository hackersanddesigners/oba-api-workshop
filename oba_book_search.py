# Search for a book in the oba API
from settings import *
from os.path import join, dirname
from dotenv import load_dotenv
from requests_xml import XMLSession

# Get the api keys from the .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

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
# the code below gives us the title of the book
title =  result.xml.xpath('//title', first=True)
print( title.text )
# or get the cover image from the XML
# cover =  result.xml.xpath('//coverimage[1]/text()', first=True)
# print( cover )

# To see all the data we got back uncomment the line below
# print( result.xml.raw_xml )
