import functools
import json

import pytest
import requests


class PokeApiClient:

    def __init__(self, api_url: str):
        self._api_url = api_url

    @functools.lru_cache
    def raw_get(self, url: str):
        return json.loads(requests.get(url).content)

    def get(self, route: str):
        return self.raw_get(f"{self._api_url}/{route}")

    def assert_get(self, route: str):
        assert self.raw_get(route) is not None


@pytest.fixture
def api_client(api_url: str = "https://pokeapi.co/api/v2") -> PokeApiClient:
    return PokeApiClient(api_url)
