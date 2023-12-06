import os

import pytest

from conftest import PokeApiClient
from models.pokemon import Pokemon


def should_get_pokemon_data_in_the_correct_model(api_client: PokeApiClient):
    pokemon_json = api_client.get("pokemon/ditto")
    Pokemon(**pokemon_json)


def should_return_same_data_for_name_and_number_fetch(api_client: PokeApiClient):
    pokemon_name_json = api_client.get("pokemon/bulbasaur")
    pokemon_id_json = api_client.get("pokemon/1")
    assert Pokemon(**pokemon_name_json) == Pokemon(**pokemon_id_json)


def assert_links_exist(fields: dict, api_client: PokeApiClient):
    for name, value in fields.items():
        if type(value) is list:
            for entry in value:
                assert_links_exist(entry, api_client)
        elif type(value) is dict:
            assert_links_exist(value, api_client)
        elif name is "url":
            api_client.assert_get(value)


@pytest.mark.skipif(os.getenv("SKIP_LONG", default=None) is not None, reason="Skipped long test")
def should_have_functioning_links_to_other_resources(api_client: PokeApiClient):
    pokemon_json = api_client.get("pokemon/smeargle")
    pokemon = Pokemon(**pokemon_json)
    assert_links_exist(pokemon.model_dump(), api_client)
