import sys
import json
import requests

k = "dLtqFzfAmRuxENewou"

if (sys.argv[1] == 'stats'):
  url = "https://gender-api.com/get-stats?&key=" + k
  r = requests.get(url)
  data = r.text
else:
  url = "https://gender-api.com/get?key=" + k + "&name=" + sys.argv[1] + "&country=" + sys.argv[2]
  r = requests.get(url)
  data = r.text

pprint = json.loads(data)
print(json.dumps(pprint, indent=4, sort_keys=True))


