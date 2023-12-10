from pydantic import BaseModel

from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class PokemonFormType(BaseModel):
    slot: int
    type: NamedApiResource


class PokemonFormSprites(BaseModel):
    front_default: str | None
    front_shiny: str | None
    back_default: str | None
    back_shiny: str | None


class PokemonForm(Fetchable):
    name: str
    order: int
    form_order: int
    is_default: bool
    is_battle_only: bool
    is_mega: bool
    form_name: str
    pokemon: NamedApiResource
    types: list[PokemonFormType]
    sprites: PokemonFormSprites
    version_group: NamedApiResource
    names: list[Name]
    form_names: list[Name]
