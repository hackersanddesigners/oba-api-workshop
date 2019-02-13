# imagga allows you to let a machine learning algorythm analyze your image
# Setup a free account on https://imagga.com/ and get your api key and secret.

import requests
import json
from settings import *

# the url of the image to analyse.
image_url = 'https://wiki.hackersanddesigners.nl/images/1/13/Schermata_2018-11-25_alle_12.04.38.png'

response = requests.get('https://api.imagga.com/v2/tags?image_url=%s' % image_url,
                        auth=(imagga_api_key, imagga_api_secret))

# here we're using json.dumps to print the result in a readable format.
print( json.dumps( response.json(), indent=2 ) )
