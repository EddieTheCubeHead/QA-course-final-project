from pydantic import BaseModel

from models.common import NamedApiResource, VerboseEffect, VersionGroupFlavorText, GenerationGameIndex, Name, \
    ApiResource, MachineVersionDetail
from models.fetchable import Fetchable


class ItemSprites(BaseModel):
    default: str | None


class ItemHolderPokemonVersionDetails(BaseModel):
    rarity: int
    version: NamedApiResource


class ItemHolderPokemon(BaseModel):
    pokemon: NamedApiResource
    version_details: list[ItemHolderPokemonVersionDetails]


class Item(Fetchable):
    name: str
    cost: int
    fling_power: int | None
    fling_effect: NamedApiResource | None
    attributes: list[NamedApiResource]
    category: NamedApiResource
    effect_entries: list[VerboseEffect]
    flavor_text_entries: list[VersionGroupFlavorText]
    game_indices: list[GenerationGameIndex]
    names: list[Name]
    sprites: ItemSprites
    held_by_pokemon: list[ItemHolderPokemon]
    baby_trigger_for: ApiResource | None
    machines: list[MachineVersionDetail]
