import os
from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)

OBA_API_Key = os.getenv('OBA_API_Key')
RapidAPI_Key = os.getenv('RapidAPI_Key')
MS_Azure_Key = os.getenv('MS_Azure_Key')