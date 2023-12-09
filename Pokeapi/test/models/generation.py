from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class Generation(Fetchable):
    name: str
    abilities: list[NamedApiResource]
    names: list[Name]
    main_region: NamedApiResource
    moves: list[NamedApiResource]
    pokemon_species: list[NamedApiResource]
    types: list[NamedApiResource]
    version_groups: list[NamedApiResource]
