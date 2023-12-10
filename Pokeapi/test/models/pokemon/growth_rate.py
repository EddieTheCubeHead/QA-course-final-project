from pydantic import BaseModel

from models.common import NamedApiResource, Description
from models.fetchable import Fetchable


class GrowthRateExperienceLevel(BaseModel):
    level: int
    experience: int


class GrowthRate(Fetchable):
    name: str
    formula: str
    descriptions: list[Description]
    levels: list[GrowthRateExperienceLevel]
    pokemon_species: list[NamedApiResource]
