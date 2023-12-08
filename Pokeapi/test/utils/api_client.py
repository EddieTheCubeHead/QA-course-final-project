import functools
import json

import requests

from models.fetchable import Fetchable


def _get_class_route(base_class: type(Fetchable)):
    return "".join((c if c.islower() else f"-{c.lower()}" for c in base_class.__name__))[1:]


class PokeApiClient:

    def __init__(self, api_url: str):
        self._api_url = api_url

    @functools.lru_cache
    def raw_get(self, url: str):
        return json.loads(requests.get(url).content)

    def get(self, base_class: type(Fetchable), instance: str):
        url = f"{self._api_url}/{_get_class_route(base_class)}/{instance}"
        print(url)
        return base_class(**self.raw_get(url))

    def assert_get(self, route: str):
        assert self.raw_get(route) is not None, f"Failed to fetch from route '{route}'"
