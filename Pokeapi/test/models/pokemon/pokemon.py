from pydantic import BaseModel

from models.common import NamedApiResource
from models.fetchable import Fetchable


class PokemonAbility(BaseModel):
    is_hidden: bool
    slot: int
    ability: NamedApiResource


class VersionGameIndex(BaseModel):
    version: NamedApiResource
    game_index: int


class PokemonHeldItemVersion(BaseModel):
    version: NamedApiResource
    rarity: int


class PokemonHeldItem(BaseModel):
    item: NamedApiResource
    version_details: list[PokemonHeldItemVersion]


class PokemonMoveVersion(BaseModel):
    move_learn_method: NamedApiResource
    version_group: NamedApiResource
    level_learned_at: int


class PokemonMove(BaseModel):
    move: NamedApiResource
    version_group_details: list[PokemonMoveVersion]


class PokemonSprites(BaseModel):
    front_default: str | None
    front_shiny: str | None
    front_female: str | None
    front_shiny_female: str | None
    back_default: str | None
    back_shiny: str | None
    back_female: str | None
    back_shiny_female: str | None


class PokemonStat(BaseModel):
    stat: NamedApiResource
    effort: int
    base_stat: int


class PokemonType(BaseModel):
    slot: int
    type: NamedApiResource


class PokemonTypePast(BaseModel):
    generation: NamedApiResource
    types: list[PokemonType]


class Pokemon(Fetchable):
    name: str
    base_experience: int | None
    height: int
    is_default: bool
    order: int
    weight: int
    location_area_encounters: str
    sprites: PokemonSprites
    species: NamedApiResource
    stats: list[PokemonStat]
    types: list[PokemonType]
    abilities: list[PokemonAbility]
    forms: list[NamedApiResource]
    game_indices: list[VersionGameIndex]
    held_items: list[PokemonHeldItem]
    moves: list[PokemonMove]
    past_types: list[PokemonTypePast]
