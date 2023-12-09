from typing import TypeVar, Generic

from pydantic import BaseModel

from models.fetchable import Fetchable


class ApiResource(BaseModel):
    url: str


class NamedApiResource(ApiResource):
    name: str


class Name(BaseModel):
    name: str
    language: NamedApiResource


class Effect(BaseModel):
    effect: str
    language: NamedApiResource


class VerboseEffect(Effect):
    short_effect: str


class ListResult(BaseModel):
    count: int
    next: str | None
    previous: str | None
    results: list[ApiResource]


class NamedListResult(BaseModel):
    count: int
    next: str | None
    previous: str | None
    results: list[NamedApiResource]


class FlavorText(BaseModel):
    flavor_text: str
    language: NamedApiResource


class Description(BaseModel):
    description: str
    language: NamedApiResource


class VersionGroupFlavorText(BaseModel):
    text: str
    language: NamedApiResource
    version_group: NamedApiResource


class GenerationGameIndex(BaseModel):
    game_index: int
    generation: NamedApiResource


class MachineVersionDetail(BaseModel):
    machine: ApiResource
    version_group: NamedApiResource


class Encounter(BaseModel):
    min_level: int
    max_level: int
    condition_values: list[NamedApiResource]
    chance: int
    method: NamedApiResource


class VersionEncounterDetail(BaseModel):
    version: NamedApiResource
    max_chance: int
    encounter_details: list[Encounter]
