import os

import pytest

from conftest import PokeApiClient, LinkWalker
from models.ability import Ability


def should_get_ability_data_in_the_correct_model(api_client: PokeApiClient):
    api_client.get("ability/moxie", Ability)


def should_return_same_data_for_name_and_number_fetch(api_client: PokeApiClient):
    ability_from_id = api_client.get("ability/1", Ability)
    ability_from_name = api_client.get(f"ability/{ability_from_id.name}", Ability)
    assert ability_from_name == ability_from_id


@pytest.mark.skipif(os.getenv("SKIP_LONG", default=None) is not None, reason="Skipped long test")
def should_have_functioning_links_to_other_resources(api_client: PokeApiClient, link_walker: LinkWalker):
    ability = api_client.get("ability/drought", Ability)
    link_walker.assert_links_exist(ability.model_dump())
