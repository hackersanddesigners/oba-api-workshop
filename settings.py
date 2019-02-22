import os
from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)

oba_api_key = os.getenv('oba_api_key')
rapidapi_key = os.getenv('rapidapi_key')
imagga_api_key = os.getenv('imagga_api_key')
imagga_api_secret = os.getenv('imagga_api_secret')
# MS_Azure_Key = os.getenv('MS_Azure_Key')
# MS_Azure_Image_Key = os.getenv('MS_Azure_Image_Key')
