from pydantic import BaseModel

from models.common import NamedApiResource, ApiResource, Name, FlavorText, Description
from models.fetchable import Fetchable


class PokemonSpeciesDexEntry(BaseModel):
    entry_number: int
    pokedex: NamedApiResource


class PalParkEncounterArea(BaseModel):
    base_score: int
    rate: int
    area: NamedApiResource


class Genus(BaseModel):
    genus: str
    language: NamedApiResource


class PokemonSpeciesVariety(BaseModel):
    is_default: bool
    pokemon: NamedApiResource


class PokemonSpecies(Fetchable):
    name: str
    order: int
    gender_rate: int
    capture_rate: int
    base_happiness: int | None
    is_baby: bool
    is_legendary: bool
    is_mythical: bool
    hatch_counter: int | None
    has_gender_differences: bool
    forms_switchable: bool
    growth_rate: NamedApiResource
    pokedex_numbers: list[PokemonSpeciesDexEntry]
    egg_groups: list[NamedApiResource]
    color: NamedApiResource
    shape: NamedApiResource | None
    evolves_from_species: NamedApiResource | None
    evolution_chain: ApiResource
    habitat: NamedApiResource | None
    generation: NamedApiResource
    names: list[Name]
    pal_park_encounters: list[PalParkEncounterArea]
    flavor_text_entries: list[FlavorText]
    form_descriptions: list[Description]
    genera: list[Genus]
    varieties: list[PokemonSpeciesVariety]
