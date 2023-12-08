import os

import pytest

from conftest import PokeApiClient, LinkWalker
from models.pokemon import Pokemon


def should_get_pokemon_data_in_the_correct_model(api_client: PokeApiClient):
    api_client.get("pokemon/ditto", Pokemon)


def should_return_same_data_for_name_and_number_fetch(api_client: PokeApiClient):
    pokemon_from_id = api_client.get("pokemon/1", Pokemon)
    pokemon_from_name = api_client.get(f"pokemon/{pokemon_from_id.name}", Pokemon)
    assert pokemon_from_name == pokemon_from_id


@pytest.mark.skipif(os.getenv("SKIP_LONG", default=None) is not None, reason="Skipped long test")
def should_have_functioning_links_to_other_resources(api_client: PokeApiClient, link_walker: LinkWalker):
    pokemon = api_client.get("pokemon/smeargle", Pokemon)
    link_walker.assert_links_exist(pokemon.model_dump())
