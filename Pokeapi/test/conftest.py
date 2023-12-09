import os

import pytest

from models.ability import Ability
from models.berry import Berry
from models.berry_firmness import BerryFirmness
from models.berry_flavor import BerryFlavor
from models.contest_effect import ContestEffect
from models.contest_type import ContestType
from models.encounter_condition import EncounterCondition
from models.encounter_condition_value import EncounterConditionValue
from models.encounter_method import EncounterMethod
from models.pokemon import Pokemon
from models.super_contest_effect import SuperContestEffect
from utils.api_client import PokeApiClient, TypedPokeApiClient, TypedNamelessPokeApiClient
from utils.link_walker import LinkWalker
from utils.timer import Timer


FETCHABLE_TYPES = (Berry, BerryFirmness, BerryFlavor, ContestType, EncounterMethod, EncounterCondition,
                   EncounterConditionValue, Ability, Pokemon)
NAMELESS_TYPES = (ContestEffect, SuperContestEffect)


@pytest.fixture
def api_client() -> PokeApiClient:
    api_url = os.getenv("POKEAPI_URL", "https://pokeapi.co/api/v2/")
    return PokeApiClient(api_url)


@pytest.fixture(scope="class")
def typed_client(request) -> TypedPokeApiClient:
    api_url = os.getenv("POKEAPI_URL", "https://pokeapi.co/api/v2/")
    return TypedPokeApiClient(api_url, request.param)


@pytest.fixture(scope="class")
def nameless_client(request) -> TypedNamelessPokeApiClient:
    api_url = os.getenv("POKEAPI_URL", "https://pokeapi.co/api/v2/")
    return TypedNamelessPokeApiClient(api_url, request.param)


@pytest.fixture
def link_walker(api_client: PokeApiClient):
    return LinkWalker(api_client)


@pytest.fixture
def timer():
    return Timer()
