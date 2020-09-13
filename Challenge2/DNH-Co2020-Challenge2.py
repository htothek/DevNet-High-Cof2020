import json
import requests

url = 'https://api.chucknorris.io/jokes/random'

here = requests.get(url)

joke_json = json.loads(here.text)

print(joke_json['value'].strip('\''))
