import os

import pytest

from models.pokemon.ability import Ability
from models.berries.berry import Berry
from models.berries.berry_firmness import BerryFirmness
from models.berries.berry_flavor import BerryFlavor
from models.contests.contest_effect import ContestEffect
from models.contests.contest_type import ContestType
from models.encounters.encounter_condition import EncounterCondition
from models.encounters.encounter_condition_value import EncounterConditionValue
from models.encounters.encounter_method import EncounterMethod
from models.evolution.evolution_chain import EvolutionChain
from models.evolution.evolution_trigger import EvolutionTrigger
from models.games.generation import Generation
from models.items.item import Item
from models.items.item_attribute import ItemAttribute
from models.items.item_category import ItemCategory
from models.items.item_fling_effect import ItemFlingEffect
from models.items.item_pocket import ItemPocket
from models.locations.location import Location
from models.locations.location_area import LocationArea
from models.machines.machine import Machine
from models.moves.move import Move
from models.moves.move_ailment import MoveAilment
from models.moves.move_category import MoveCategory
from models.moves.move_damage_class import MoveDamageClass
from models.moves.move_learn_method import MoveLearnMethod
from models.moves.move_target import MoveTarget
from models.locations.pal_park_area import PalParkArea
from models.games.pokedex import Pokedex
from models.pokemon.characteristic import Characteristic
from models.pokemon.egg_group import EggGroup
from models.pokemon.gender import Gender
from models.pokemon.pokemon import Pokemon
from models.locations.region import Region
from models.contests.super_contest_effect import SuperContestEffect
from models.games.version import Version
from models.games.version_group import VersionGroup
from utils.api_client import PokeApiClient, TypedPokeApiClient, TypedNamelessPokeApiClient
from utils.link_walker import LinkWalker
from utils.timer import Timer


FETCHABLE_TYPES = (Berry, BerryFirmness, BerryFlavor, ContestType, EncounterMethod, EncounterCondition,
                   EncounterConditionValue, EvolutionTrigger, Generation, Pokedex, Version, VersionGroup, Item,
                   ItemAttribute, ItemCategory, ItemFlingEffect, ItemPocket, Location, LocationArea, PalParkArea,
                   Region, Move, MoveAilment, MoveCategory, MoveDamageClass, MoveLearnMethod, MoveTarget, Ability,
                   EggGroup, Gender, Pokemon)
NAMELESS_TYPES = (ContestEffect, SuperContestEffect, EvolutionChain, Machine, Characteristic)


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
