from pydantic import BaseModel

from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class PalParkEncounterSpecies(BaseModel):
    base_score: int
    rate: int
    pokemon_species: NamedApiResource


class PalParkArea(Fetchable):
    name: str
    names: list[Name]
    pokemon_encounters: list[PalParkEncounterSpecies]
