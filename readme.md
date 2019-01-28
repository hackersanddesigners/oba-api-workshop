# What is this?
Proposal for some examples for the H&D API workshop @ OBA

All examples store the API keys in a file called .env in the project root.

# To install

```bash
#Create a .env file
touch .env


# Add your API keys to the .env file
# (or add them with your favorite texteditor)
echo "OBA_API_Key = ABCD1234
RapidAPI_Key = 987654321
MS_Azure_TTS_Key = 123456789" >> .env

#install  python_dotenv
pip install -U python-dotenv

```

## Command line examples

### cws.py

Search for an image on Contextual websearch via the command line
The most basic example. Edit the line q = "black" to change the query.
Then run:

```bash
python cws.py
```


### ms_tts.py

Input a piece of text to convert to speech using Microsoft's TTS api


## Browser-based examples

### cgi-bin/image_search.py

Example for searching in the contextual websearch image api
make sure this example is inside /cgi-bin and that its executable bit is set by running:

```bash
chmod +x cgi_bin/image_search.py
```

then to start the webserver run:

```bash
python3 -m http.server --cgi
```

or equivalent for your python installation

visit: http://0.0.0.0:8000/cgi-bin/image_search.py in your browser

### cgi-bin/image_search_description.py

Same as 3 but then use the result of the image search to get a machine description of that image using the Microsoft machine learning API

```bash
chmod +x cgi_bin/image_search_description.py
```
```bash
python3 -m http.server --cgi
```

or equivalent for your python installation
