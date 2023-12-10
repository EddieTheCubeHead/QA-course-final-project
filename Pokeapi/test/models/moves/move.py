from pydantic import BaseModel

from models.pokemon.ability import AbilityEffectChange
from models.common import NamedApiResource, ApiResource, VerboseEffect, Name, MachineVersionDetail
from models.fetchable import Fetchable


class ContestComboDetail(BaseModel):
    use_before: list[NamedApiResource] | None
    use_after: list[NamedApiResource] | None


class ContestComboSets(BaseModel):
    normal: ContestComboDetail
    super: ContestComboDetail


class MoveFlavorText(BaseModel):
    flavor_text: str
    language: NamedApiResource
    version_group: NamedApiResource


class MoveMetaData(BaseModel):
    ailment: NamedApiResource
    category: NamedApiResource
    min_hits: int | None
    max_hits: int | None
    min_turns: int | None
    max_turns: int | None
    drain: int
    healing: int
    crit_rate: int
    ailment_chance: int
    flinch_chance: int
    stat_chance: int


class MoveStatChange(BaseModel):
    change: int
    stat: NamedApiResource


class PastMoveStatValues(BaseModel):
    accuracy: int | None
    effect_chance: int | None
    power: int | None
    pp: int | None
    effect_entries: list[VerboseEffect]
    type: NamedApiResource | None
    version_group: NamedApiResource


class Move(Fetchable):
    name: str
    accuracy: int | None
    effect_chance: int | None
    pp: int | None
    priority: int
    power: int | None
    contest_combos: ContestComboSets | None
    contest_type: NamedApiResource | None
    contest_effect: ApiResource | None
    damage_class: NamedApiResource
    effect_entries: list[VerboseEffect]
    effect_changes: list[AbilityEffectChange]
    learned_by_pokemon: list[NamedApiResource]
    flavor_text_entries: list[MoveFlavorText]
    generation: NamedApiResource
    machines: list[MachineVersionDetail]
    meta: MoveMetaData | None
    names: list[Name]
    past_values: list[PastMoveStatValues]
    stat_changes: list[MoveStatChange]
    super_contest_effect: ApiResource | None
    target: NamedApiResource
    type: NamedApiResource
