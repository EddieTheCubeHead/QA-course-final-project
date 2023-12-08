import os

import pytest

from utils.api_client import PokeApiClient
from utils.link_walker import LinkWalker
from utils.timer import Timer


@pytest.fixture
def api_client(api_url: str = None) -> PokeApiClient:
    if api_url is None:
        api_url = os.getenv("POKEAPI_URL", "https://pokeapi.co/api/v2/")
    return PokeApiClient(api_url)


@pytest.fixture
def link_walker(api_client: PokeApiClient):
    return LinkWalker(api_client)


@pytest.fixture
def timer():
    return Timer()
