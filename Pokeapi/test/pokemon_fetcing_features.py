import json

import requests


def should_fetch_something():
    request = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    print(json.loads(request.content.decode(encoding="utf-8")))

