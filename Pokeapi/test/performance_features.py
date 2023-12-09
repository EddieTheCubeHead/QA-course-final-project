import asyncio
import datetime
import os
import random

import pytest
import aiohttp

from conftest import Timer, FETCHABLE_TYPES, NAMELESS_TYPES
from utils.api_client import TypedPokeApiClient


async def fetch(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as request:
        return request.content


# noinspection PyMethodMayBeStatic
@pytest.mark.skipif("127.0.0.1" not in os.getenv("POKEAPI_URL", default="false"),
                    reason="Only run stress test against proxy to not overstress Pokeapi servers")
@pytest.mark.parametrize("typed_client", FETCHABLE_TYPES, indirect=True)
class PerformanceFeatures:

    @pytest.mark.skipif(os.getenv("SKIP_LONG", default=None) is not None, reason="Skipped long test")
    async def should_handle_thousand_requests_for_type_instance_in_ten_seconds(self, typed_client: TypedPokeApiClient,
                                                                               timer: Timer):
        async with aiohttp.ClientSession() as session:
            with timer:
                async with asyncio.TaskGroup() as task_group:
                    [task_group.create_task(typed_client.get_typed_async(session, typed_client.get_random_name()))
                     for _ in range(1000)]
        assert timer < datetime.timedelta(seconds=10)

    async def should_get_all_resources_of_type_in_five_seconds(self, typed_client: TypedPokeApiClient, timer: Timer):
        typed_client.reset_all_instances_cache()
        with timer:
            typed_client.get_all()
        assert timer < datetime.timedelta(seconds=5)


# noinspection PyMethodMayBeStatic
@pytest.mark.skipif("127.0.0.1" not in os.getenv("POKEAPI_URL", default="false"),
                    reason="Only run stress test against proxy to not overstress Pokeapi servers")
@pytest.mark.parametrize("nameless_client", NAMELESS_TYPES, indirect=True)
class NamelessTypePerformanceFeatures:

    @pytest.mark.skipif(os.getenv("SKIP_LONG", default=None) is not None, reason="Skipped long test")
    async def should_handle_thousand_requests_for_type_instance_in_ten_seconds(self, nameless_client: TypedPokeApiClient,
                                                                               timer: Timer):
        async with aiohttp.ClientSession() as session:
            with timer:
                async with asyncio.TaskGroup() as task_group:
                    [task_group.create_task(nameless_client.get_typed_async(session, nameless_client.get_random_id()))
                     for _ in range(1000)]
        assert timer < datetime.timedelta(seconds=10)

    async def should_get_all_resources_of_type_in_five_seconds(self, nameless_client: TypedPokeApiClient, timer: Timer):
        nameless_client.reset_all_instances_cache()
        with timer:
            nameless_client.get_all()
        assert timer < datetime.timedelta(seconds=5)
