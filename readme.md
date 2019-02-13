# What is this?
Proposal for some examples for the H&D API workshop @ OBA

All examples store the API keys in a file called .env in the project root.

# To install

```bash
#Create a .env file
touch .env
```

# Add your API keys to the .env file
# (or add them with your favorite texteditor)
echo "OBA_API_Key = ABCD1234
RapidAPI_Key = 987654321
MS_Azure_TTS_Key = 123456789" >> .env
```

```python3
# Then add a line for every key in settings.py
OBA_API_Key = os.getenv('OBA_API_Key')
```

```bash
# if installing on your own machine, make sure you have python 3
# and install the needed libraries:

pip install -U python-dotenv
pip install -U requests
pip install -U requests_xml
```

## Code examples

### oba_book_search.py

Search for a book with the OBA API.
The most basic example. Edit the line q = "black" to change the query.
Then run:

```bash
python cws.py
```

### imagga.py

Analyse an image with the free Imagga machine learning algorithm API
Change the url. Then:

```bash
python imagga.py
```

### image_search_description.py

Example for searching in the contextual websearch image api

```bash
python image_search_description.py
```


### oba_search_description.py

Same as the above, but searches for a book then sends the image to imagga.
Doesn't work yet :(

### cws.py

Needs account with creditcard...

Search for an image on Contextual websearch via the command line
The most basic example. Edit the line q = "hacking" to change the query.
Then run:

```bash
python cws.py
```
