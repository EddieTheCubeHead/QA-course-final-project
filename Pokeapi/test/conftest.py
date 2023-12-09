import os

import pytest

from models.ability import Ability
from models.berry import Berry
from models.pokemon import Pokemon
from utils.api_client import PokeApiClient, TypedPokeApiClient
from utils.link_walker import LinkWalker
from utils.timer import Timer


FETCHABLE_TYPES = (Berry, Ability, Pokemon)


@pytest.fixture
def api_client() -> PokeApiClient:
    api_url = os.getenv("POKEAPI_URL", "https://pokeapi.co/api/v2/")
    return PokeApiClient(api_url)


@pytest.fixture(scope="class")
def typed_client(request) -> TypedPokeApiClient:
    api_url = os.getenv("POKEAPI_URL", "https://pokeapi.co/api/v2/")
    return TypedPokeApiClient(api_url, request.param)


@pytest.fixture
def link_walker(api_client: PokeApiClient):
    return LinkWalker(api_client)


@pytest.fixture
def timer():
    return Timer()
