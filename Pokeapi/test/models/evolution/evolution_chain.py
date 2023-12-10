from __future__ import annotations

from pydantic import BaseModel

from models.common import NamedApiResource
from models.fetchable import Fetchable


class EvolutionDetail(BaseModel):
    needs_overworld_rain: bool
    turn_upside_down: bool
    time_of_day: str
    gender: int | None
    min_level: int | None
    min_happiness: int | None
    min_beauty: int | None
    min_affection: int | None
    relative_physical_stats: int | None
    trigger: NamedApiResource
    item: NamedApiResource | None
    held_item: NamedApiResource | None
    known_move: NamedApiResource | None
    known_move_type: NamedApiResource | None
    location: NamedApiResource | None
    party_species: NamedApiResource | None
    party_type: NamedApiResource | None
    trade_species: NamedApiResource | None


class ChainLink(BaseModel):
    is_baby: bool
    species: NamedApiResource
    evolution_details: list[EvolutionDetail]
    evolves_to: list[ChainLink]


class EvolutionChain(Fetchable):
    baby_trigger_item: NamedApiResource | None
    chain: ChainLink
