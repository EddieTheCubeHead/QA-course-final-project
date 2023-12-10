from pydantic import BaseModel

from models.common import NamedApiResource
from models.fetchable import Fetchable


class PokemonSpeciesGender(BaseModel):
    rate: int
    pokemon_species: NamedApiResource


class Gender(Fetchable):
    name: str
    pokemon_species_details: list[PokemonSpeciesGender]
    required_for_evolution: list[NamedApiResource]
