import requests
from requests.auth import HTTPBasicAuth
import json
import jsonpath

def test_with_authentication():
    response=requests.get("https://api.github.com/user",auth=HTTPBasicAuth("paultsiouper@gmail.com","Kaiser3#"))
    print(response.text)
