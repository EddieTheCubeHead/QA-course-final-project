import functools
import json
import random

import aiohttp
import requests

from models.common import NamedApiResource, NamedListResult, ApiResource, ListResult
from models.fetchable import Fetchable


def _get_class_route(base_class: type[Fetchable]):
    return "".join((c if c.islower() else f"-{c.lower()}" for c in base_class.__name__))[1:]


class PokeApiClient:

    def __init__(self, api_url: str):
        self._api_url = api_url

    @staticmethod
    def raw_get(url: str):
        return requests.get(url).content

    def get(self, base_class: type[Fetchable], instance: str):
        return base_class.model_validate_json(
            self.raw_get(f"{self._api_url}/{_get_class_route(base_class)}/{instance}"))

    @staticmethod
    async def raw_get_async(session: aiohttp.ClientSession, url: str):
        async with session.get(url) as request:
            return await request.text()

    async def get_async(self, session: aiohttp.ClientSession, base_class: type(Fetchable), instance: str):
        json_result = await self.raw_get_async(session,
                                               f"{self._api_url}/{_get_class_route(base_class)}/{instance}")
        return base_class.model_validate_json(json_result)

    def assert_get(self, route: str):
        assert self.raw_get(route) is not None, f"Failed to fetch from route '{route}'"


class TypedNamelessPokeApiClient(PokeApiClient):
    def __init__(self, api_url: str, fetchable_resource: type[Fetchable]):
        super().__init__(api_url)
        self._fetchable = fetchable_resource
        self._all: list[ApiResource] | None = None  # cache multi-fetch to reduce load on API

    @property
    def route_name(self) -> str:
        return _get_class_route(self._fetchable)

    def _get_fetch_url(self, instance: str) -> str:
        # There's a stupid exception on the API naming scheme specifically for Pokémon encounters
        if self.route_name == "pokemon-location-area-list":
            return f"{self._api_url}/pokemon/{instance}/encounters"
        return f"{self._api_url}/{self.route_name}/{instance}"

    def _get_fetch_all_url(self) -> str:
        # There's a stupid exception on the API naming scheme specifically for Pokémon encounters
        if self.route_name == "pokemon-location-area-list":
            return f"{self._api_url}/pokemon"
        return f"{self._api_url}/{_get_class_route(self._fetchable)}"

    def get_all(self) -> list[ApiResource]:
        if self._all is None:
            self._all = self._fetch_all_of_type()
        return self._all

    def get_typed(self, instance: str):
        return self._fetchable.model_validate_json(self.raw_get(self._get_fetch_url(instance)))

    def reset_all_instances_cache(self):
        self._all = None

    def get_random_id(self) -> str:
        return random.choice([resource.url.split("/")[-2] for resource in self.get_all()])

    def _fetch_all_of_type(self) -> list[ApiResource]:
        result = ListResult.model_validate_json(self.raw_get(self._get_fetch_all_url()))
        resources = result.results.copy()
        while result.next:
            result = ListResult.model_validate_json(self.raw_get(result.next))
            resources.extend(result.results.copy())
        return resources

    async def get_typed_async(self, session: aiohttp.ClientSession, instance: str):
        json_result = await self.raw_get_async(session, self._get_fetch_url(instance))
        return self._fetchable.model_validate_json(json_result)


class TypedPokeApiClient(TypedNamelessPokeApiClient):

    def __init__(self, api_url: str, fetchable_resource: type[Fetchable]):
        super().__init__(api_url, fetchable_resource)
        self._fetchable = fetchable_resource
        self._all: list[NamedApiResource] | None = None  # cache multi-fetch to reduce load on API

    def get_random_name(self) -> str:
        return random.choice([resource.name for resource in self.get_all()])

    def get_all(self) -> list[NamedApiResource]:
        if self._all is None:
            self._all = self._fetch_all_of_type()
        return self._all

    def _fetch_all_of_type(self) -> list[NamedApiResource]:
        result = NamedListResult.model_validate_json(
            self.raw_get(self._get_fetch_all_url()))
        resources = result.results.copy()
        while result.next:
            result = NamedListResult.model_validate_json(self.raw_get(result.next))
            resources.extend(result.results.copy())
        return resources
