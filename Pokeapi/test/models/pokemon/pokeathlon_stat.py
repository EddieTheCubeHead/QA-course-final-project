from pydantic import BaseModel

from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class NaturePokeathlonStatAffect(BaseModel):
    max_change: int
    nature: NamedApiResource


class NaturePokeathlonStatAffectSets(BaseModel):
    increase: list[NaturePokeathlonStatAffect]
    decrease: list[NaturePokeathlonStatAffect]


class PokeathlonStat(Fetchable):
    name: str
    names: list[Name]
    affecting_natures: NaturePokeathlonStatAffectSets
