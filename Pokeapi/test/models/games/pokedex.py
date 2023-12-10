from pydantic import BaseModel

from models.common import NamedApiResource, Description, Name
from models.fetchable import Fetchable


class PokemonEntry(BaseModel):
    entry_number: int
    pokemon_species: NamedApiResource


class Pokedex(Fetchable):
    name: str
    is_main_series: bool
    descriptions: list[Description]
    names: list[Name]
    pokemon_entries: list[PokemonEntry]
    region: NamedApiResource | None
    version_groups: list[NamedApiResource]
