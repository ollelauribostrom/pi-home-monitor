import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(join(dirname(__file__), '../.env'))

config = {
    'from': os.environ.get('TWILIO_FROM_NUMBER'),
    'account_sid': os.environ.get('TWILIO_ACCOUNT_SID'),
    'auth_token': os.environ.get('TWILIO_AUTH_TOKEN'),
    'shared_secret': os.environ.get('SHARED_SECRET'),
    'base_url': os.environ.get('BASE_URL')
  }
