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
from models.evolution_chain import EvolutionChain
from models.evolution_trigger import EvolutionTrigger
from models.generation import Generation
from models.item import Item
from models.item_attribute import ItemAttribute
from models.item_category import ItemCategory
from models.item_fling_effect import ItemFlingEffect
from models.item_pocket import ItemPocket
from models.location import Location
from models.location_area import LocationArea
from models.machine import Machine
from models.move import Move
from models.move_ailment import MoveAilment
from models.move_category import MoveCategory
from models.move_damage_class import MoveDamageClass
from models.move_learn_method import MoveLearnMethod
from models.pal_park_area import PalParkArea
from models.pokedex import Pokedex
from models.pokemon import Pokemon
from models.region import Region
from models.super_contest_effect import SuperContestEffect
from models.version import Version
from models.version_group import VersionGroup
from utils.api_client import PokeApiClient, TypedPokeApiClient, TypedNamelessPokeApiClient
from utils.link_walker import LinkWalker
from utils.timer import Timer


FETCHABLE_TYPES = (Berry, BerryFirmness, BerryFlavor, ContestType, EncounterMethod, EncounterCondition,
                   EncounterConditionValue, EvolutionTrigger, Generation, Pokedex, Version, VersionGroup, Item,
                   ItemAttribute, ItemCategory, ItemFlingEffect, ItemPocket, Location, LocationArea, PalParkArea,
                   Region, Move, MoveAilment, MoveCategory, MoveDamageClass, MoveLearnMethod, Ability, Pokemon)
NAMELESS_TYPES = (ContestEffect, SuperContestEffect, EvolutionChain, Machine)


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
