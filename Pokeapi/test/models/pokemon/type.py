from pydantic import BaseModel

from models.common import NamedApiResource, GenerationGameIndex, Name
from models.fetchable import Fetchable


class TypeRelations(BaseModel):
    no_damage_to: list[NamedApiResource]
    half_damage_to: list[NamedApiResource]
    double_damage_to: list[NamedApiResource]
    no_damage_from: list[NamedApiResource]
    half_damage_from: list[NamedApiResource]
    double_damage_from: list[NamedApiResource]


class TypeRelationsPast(BaseModel):
    generation: NamedApiResource
    damage_relations: TypeRelations


class TypePokemon(BaseModel):
    slot: int
    pokemon: NamedApiResource


class Type(Fetchable):
    name: str
    damage_relations: TypeRelations
    past_damage_relations: list[TypeRelationsPast]
    game_indices: list[GenerationGameIndex]
    generation: NamedApiResource
    move_damage_class: NamedApiResource | None
    names: list[Name]
    pokemon: list[TypePokemon]
    moves: list[NamedApiResource]
