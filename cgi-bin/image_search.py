#!/usr/bin/env python3

# example for searching in the contextual websearch image api
# make sure this image inside /cgi-bin and that its executable bit is set
# then run: python3 -m http.server --cgi (or equivalent)
# visit: http://0.0.0.0:8000/cgi-bin/image_search.py in your browser
#
from ..settings import *
import cgi
import requests #install from: http://docs.python-requests.org/en/master/

form = cgi.FieldStorage()
value = ""

# print a required header and begin the html document
print("Content-type: text/html")
print("")
print('<html><body>')

if "q" in form:
	value = str(form['q'].value)
	# Your_X_RapidAPI_Key get loaded by settings.py from .env

	#The query parameters: (update according to your search query)
	q = value #the search query
	pageNumber = 1 #the number of requested page
	pageSize = 1 #the size of a page
	autoCorrect = False #autoCorrectspelling
	safeSearch = True #filter results for adult content

	response=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI?q={}&pageNumber={}&pageSize={}&autocorrect={}&safeSearch={}".format(q, pageNumber, pageSize, autoCorrect,safeSearch),
		headers={
			"X-RapidAPI-Key": RapidAPI_Key
		}
	).json()

	url = response["value"][0]["url"] # get the image url from the response
	print('<img src="%s" />' % url ) # display the image

# print the search form
print('<form><input name="q" value="%s"/><input type="submit" value="send" /></form>' % value )

# end the html
print('</body></html>')