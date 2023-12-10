from pydantic import BaseModel

from models.common import NamedApiResource, ApiResource, Name
from models.fetchable import Fetchable


class MoveStatAffect(BaseModel):
    change: int
    move: NamedApiResource


class MoveStatAffectSets(BaseModel):
    increase: list[MoveStatAffect]
    decrease: list[MoveStatAffect]


class NatureStatAffectSets(BaseModel):
    increase: list[NamedApiResource]
    decrease: list[NamedApiResource]


class Stat(Fetchable):
    name: str
    game_index: int
    is_battle_only: bool
    affecting_moves: MoveStatAffectSets
    affecting_natures: NatureStatAffectSets
    characteristics: list[ApiResource]
    move_damage_class: NamedApiResource | None
    names: list[Name]
