import functools
import json
import os

import pytest
import requests
from pydantic import BaseModel


class PokeApiClient:

    def __init__(self, api_url: str):
        self._api_url = api_url

    @functools.lru_cache
    def raw_get(self, url: str):
        return json.loads(requests.get(url).content)

    def get(self, route: str, base_class: type(BaseModel)):
        return base_class(**self.raw_get(f"{self._api_url}/{route}"))

    def assert_get(self, route: str):
        assert self.raw_get(route) is not None, f"Failed to fetch from route '{route}'"


class LinkWalker:

    def __init__(self, api_client: PokeApiClient):
        self._api_client = api_client

    def assert_links_exist(self, fields: dict):
        for name, value in fields.items():
            if type(value) is list:
                for entry in value:
                    self.assert_links_exist(entry)
            elif type(value) is dict:
                self.assert_links_exist(value)
            elif name is "url":
                assert type(value) is str, f"Url '{value}' is not in string format!"
                self._api_client.assert_get(value)


@pytest.fixture
def api_client(api_url: str = None) -> PokeApiClient:
    if api_url is None:
        api_url = os.getenv("POKEAPI_URL", "https://pokeapi.co/api/v2/")
    return PokeApiClient(api_url)


@pytest.fixture
def link_walker(api_client: PokeApiClient):
    return LinkWalker(api_client)
