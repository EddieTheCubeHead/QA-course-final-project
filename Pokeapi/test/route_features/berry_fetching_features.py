import os

import pytest

from conftest import PokeApiClient, LinkWalker
from models.berry import Berry


def should_get_ability_data_in_the_correct_model(api_client: PokeApiClient):
    api_client.get(Berry, "sitrus")


def should_return_same_data_for_name_and_number_fetch(api_client: PokeApiClient):
    berry_from_id = api_client.get(Berry, "1")
    berry_from_name = api_client.get(Berry, berry_from_id.name)
    assert berry_from_name == berry_from_id


@pytest.mark.skipif(os.getenv("SKIP_LONG", default=None) is not None, reason="Skipped long test")
def should_have_functioning_links_to_other_resources(api_client: PokeApiClient, link_walker: LinkWalker):
    berry = api_client.get(Berry, "oran")
    link_walker.assert_links_exist(berry.model_dump())
