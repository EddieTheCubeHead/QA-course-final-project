import json

import requests

from models import Pokemon


def should_get_data_in_the_correct_model():
    request = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    Pokemon(**json.loads(request.content.decode(encoding="utf-8")))
