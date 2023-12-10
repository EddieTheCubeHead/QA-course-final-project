from pydantic import BaseModel

from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class NatureStatChange(BaseModel):
    max_change: int
    pokeathlon_stat: NamedApiResource


class MoveBattleStylePreference(BaseModel):
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: NamedApiResource


class Nature(Fetchable):
    name: str
    decreased_stat: NamedApiResource | None
    increased_stat: NamedApiResource | None
    hates_flavor: NamedApiResource | None
    likes_flavor: NamedApiResource | None
    pokeathlon_stat_changes: list[NatureStatChange]
    move_battle_style_preferences: list[MoveBattleStylePreference]
    names: list[Name]
