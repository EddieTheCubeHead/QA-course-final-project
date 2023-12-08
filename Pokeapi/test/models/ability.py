from pydantic import BaseModel

from models.common import NamedApiResource, Name, VerboseEffect, Effect
from models.fetchable import Fetchable


class AbilityEffectChange(BaseModel):
    effect_entries: list[Effect]
    version_group: NamedApiResource


class AbilityFlavorText(BaseModel):
    flavor_text: str
    language: NamedApiResource
    version_group: NamedApiResource


class AbilityPokemon(BaseModel):
    is_hidden: bool
    slot: int
    pokemon: NamedApiResource


class Ability(Fetchable):
    id: int
    name: str
    is_main_series: bool
    generation: NamedApiResource
    names: list[Name]
    effect_entries: list[VerboseEffect]
    effect_changes: list[AbilityEffectChange]
    flavor_text_entries: list[AbilityFlavorText]
    pokemon: list[AbilityPokemon]
