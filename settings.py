import os
from dotenv import load_dotenv
load_dotenv()


def env():
  dict = {'oba_api_key': os.getenv('oba_api_key'),
          'rapidapi_key': os.getenv('rapidapi_key'),
          'imagga_api_key': os.getenv('imagga_api_key'),
          'imagga_api_secret': os.getenv('imagga_api_secret')}

  return dict
