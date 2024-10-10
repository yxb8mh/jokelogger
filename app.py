#!/usr/bin/python3

import requests
import json
import logging


url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
response = json.loads(response.text)
#rewriting the response value

id = response['id'] #calling the key out, the value of the id will be called out
setup = response['setup']
punchline = response['punchline']

print(id, setup, punchline)
