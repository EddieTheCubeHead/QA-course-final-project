import asyncio
import datetime
import os
import random

import pytest
import aiohttp

from conftest import Timer


async def fetch(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as request:
        return request.content


@pytest.mark.skipif(os.getenv("SKIP_LONG", default=None) is not None, reason="Skipped long test")
@pytest.mark.skipif("127.0.0.1" not in os.getenv("POKEAPI_URL", default="false"),
                    reason="Only run stress test against proxy to not overstress Pokeapi servers")
async def should_handle_thousand_pokemon_requests_in_ten_seconds(timer: Timer):
    pokeapi_url = os.getenv("POKEAPI_URL")
    async with aiohttp.ClientSession() as session:
        with timer:
            async with asyncio.TaskGroup() as task_group:
                [task_group.create_task(fetch(session, f"{pokeapi_url}/pokemon/{random.randint(1, 800)}"))
                 for _ in range(1000)]
    assert timer < datetime.timedelta(seconds=10)
