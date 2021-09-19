from requests import api
from snipe_credentials import get_credentials
from snipe_hardware import get_hardware
import requests

CREDENTIALS_PATH = "~/.snipe/credentials.yaml"
DEFAULT_LIMIT = 1000

creds = get_credentials(CREDENTIALS_PATH)
url = creds["url"]
api_key = creds["api_key"]

print(get_hardware(url, api_key, DEFAULT_LIMIT))
