import functools
import json

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
