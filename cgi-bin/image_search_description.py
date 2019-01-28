#!/usr/bin/env python3

# example for searching in the contextual websearch image api
# by: heerko@hackersanddesigners.nl
import sys, os
sys.path.append(os.getcwd())
from settings import *
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


	import requests
	# import matplotlib.pyplot as plt
	import json
	# from PIL import Image
	#from io import BytesIO

	# Replace <Subscription Key> with your valid subscription key.
	subscription_key = MS_Azure_Image_Key
	assert subscription_key

	# You must use the same region in your REST call as you used to get your
	# subscription keys. For example, if you got your subscription keys from
	# westus, replace "westcentralus" in the URI below with "westus".
	#
	# Free trial subscription keys are generated in the "westus" region.
	# If you use a free trial subscription key, you shouldn't need to change
	# this region.
	vision_base_url = "https://westeurope.api.cognitive.microsoft.com/vision/v2.0/"

	analyze_url = vision_base_url + "analyze"

	# Set image_url to the URL of an image that you want to analyze.
	image_url = url # "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" +  "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"

	headers = {'Ocp-Apim-Subscription-Key': subscription_key }
	params  = {'visualFeatures': 'Categories,Description,Color'}
	data    = {'url': image_url}
	response = requests.post(analyze_url, headers=headers, params=params, json=data)
	response.raise_for_status()

	# The 'analysis' object contains various fields that describe the image. The most
	# relevant caption for the image is obtained from the 'description' property.
	analysis = response.json()
	#print(json.dumps(response.json()))
	image_caption = analysis["description"]["captions"][0]["text"].capitalize()

	print( image_caption )
	# Display the image and overlay it with the caption.
	# image = Image.open(BytesIO(requests.get(image_url).content))
	# plt.imshow(image)
	# plt.axis("off")
	# _ = plt.title(image_caption, size="x-large", y=-0.1)
	# plt.show()

# print the search form
print('<form><input name="q" value="%s"/><input type="submit" value="send" /></form>' % value )

# end the html
print('</body></html>')