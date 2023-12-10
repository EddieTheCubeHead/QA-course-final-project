from pydantic import BaseModel

from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class AwesomeName(BaseModel):
    awesome_name: str
    language: NamedApiResource


class PokemonShape(Fetchable):
    name: str
    awesome_names: list[AwesomeName]
    names: list[Name]
    pokemon_species: list[NamedApiResource]
