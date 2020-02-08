oba api workshop
================

All examples store the API keys in a file called `.env` in the project root.

## Setup

Make a file called `.env`

```
$ touch .env
```

Add your API keys to the `.env` file (or use your favorite text editor)

```
$ echo "oba_api_key = abcd1234" >> .env
$ echo "rapidapi_key = 987654321" >> .env
$ echo "ms_azure_tts_key = 123456789" >> .env
```

Then add a line for every key in `settings.py`

```
oba_api_key = os.getenv('oba_api_key')
```

If installing on your own machine, make sure you have python 3 and install the needed libraries. If using python 3.4 or higher, we suggest to make a new python virtual environment using the `venv` option, so to not install the packages globally (you don't want to deal [with this](https://xkcd.com/1987/) afterwards)

```
$ python3.4 -m venv env
$ source env/bin/activate
```

Then use python with `python` and install the following packages

```
$ pip install python-dotenv
$ pip install requests
$ pip install xmltodict
```

## Code examples

### oba_book_search.py

Search for a book with the OBA API.
The most basic example. Edit the line q = "black" to change the query.
Then run:

```
$ python ??
```

### oba_pub_search.py


```
$ python oba_pub_search.py <publisher-name> <total-number-of-pages>
```

the API does not give back total number of pages (?), so the poor way to do it is to use OBA's website search tool, eg <https://zoeken.oba.nl/?q=publisher%3A%22IHLIA%22&uilang=en> and count number of pages at the bottom :P

(we could use a generator to be fancy tho!!)

### imagga.py

Analyse an image with the free Imagga machine learning algorithm API
Change the url. Then:

```
$ python imagga.py
```

### image_search_description.py

Example for searching in the contextual websearch image api

```
$ python image_search_description.py
```

### oba_search_description.py

Same as the above, but searches for a book then sends the image to imagga.
Doesn't work yet :(

### cws.py

Needs account with creditcard...

Search for an image on Contextual websearch via the command line
The most basic example. Edit the line q = "hacking" to change the query.
Then run:

```
$ python cws.py
```
