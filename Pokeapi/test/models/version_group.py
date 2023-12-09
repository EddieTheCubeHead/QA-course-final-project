from models.common import NamedApiResource
from models.fetchable import Fetchable


class VersionGroup(Fetchable):
    name: str
    order: int
    generation: NamedApiResource
    move_learn_methods: list[NamedApiResource]
    pokedexes: list[NamedApiResource]
    regions: list[NamedApiResource]
    versions: list[NamedApiResource]
