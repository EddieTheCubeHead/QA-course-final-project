from pydantic import BaseModel


class NamedAPIResource(BaseModel):
    name: str
    url: str


class PokemonAbility(BaseModel):
    is_hidden: bool
    slot: int
    ability: NamedAPIResource


class PokemonForm(NamedAPIResource):
    pass


class VersionGameIndex(BaseModel):
    version: NamedAPIResource
    game_index: int


class PokemonHeldItemVersion(BaseModel):
    version: NamedAPIResource
    rarity: int


class PokemonHeldItem(BaseModel):
    item: NamedAPIResource
    version_details: list[PokemonHeldItemVersion]


class PokemonMoveVersion(BaseModel):
    move_learn_method: NamedAPIResource
    version_group: NamedAPIResource
    level_learned_at: int


class PokemonMove(BaseModel):
    move: NamedAPIResource
    version_group_details: list[PokemonMoveVersion]


class PokemonSprites(BaseModel):
    front_default: str | None
    front_shiny: str | None
    front_female: str | None
    front_shiny_female: str | None
    back_default: str | None
    back_shiny: str | None
    back_female: str | None
    back_shiny_female: str | None


class PokemonStat(BaseModel):
    stat: NamedAPIResource
    effort: int
    base_stat: int


class PokemonType(BaseModel):
    slot: int
    type: NamedAPIResource


class PokemonTypePast(BaseModel):
    generation: NamedAPIResource
    types: list[PokemonType]


class Pokemon(BaseModel):
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    location_area_encounters: str
    sprites: PokemonSprites
    species: NamedAPIResource
    stats: list[PokemonStat]
    types: list[PokemonType]
    abilities: list[PokemonAbility]
    forms: list[PokemonForm]
    game_indices: list[VersionGameIndex]
    held_items: list[PokemonHeldItem]
    moves: list[PokemonMove]
    past_types: list[PokemonTypePast]
