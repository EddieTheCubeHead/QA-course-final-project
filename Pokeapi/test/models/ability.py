from pydantic import BaseModel

from models.common import NamedAPIResource, Name, VerboseEffect, Effect


class AbilityEffectChange(BaseModel):
    effect_entries: list[Effect]
    version_group: NamedAPIResource


class AbilityFlavorText(BaseModel):
    flavor_text: str
    language: NamedAPIResource
    version_group: NamedAPIResource


class AbilityPokemon(BaseModel):
    is_hidden: bool
    slot: int
    pokemon: NamedAPIResource


class Ability(BaseModel):
    id: int
    name: str
    is_main_series: bool
    generation: NamedAPIResource
    names: list[Name]
    effect_entries: list[VerboseEffect]
    effect_changes: list[AbilityEffectChange]
    flavor_text_entries: list[AbilityFlavorText]
    pokemon: list[AbilityPokemon]
