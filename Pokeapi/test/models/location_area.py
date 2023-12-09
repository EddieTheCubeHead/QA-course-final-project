from pydantic import BaseModel

from models.common import NamedApiResource, Name, VersionEncounterDetail
from models.fetchable import Fetchable


class EncounterVersionDetails(BaseModel):
    rate: int
    version: NamedApiResource


class EncounterMethodRate(BaseModel):
    encounter_method: NamedApiResource
    version_details: list[EncounterVersionDetails]


class PokemonEncounter(BaseModel):
    pokemon: NamedApiResource
    version_details: list[VersionEncounterDetail]


class LocationArea(Fetchable):
    name: str
    game_index: int
    encounter_method_rates: list[EncounterMethodRate]
    location: NamedApiResource
    names: list[Name]
    pokemon_encounters: list[PokemonEncounter]
