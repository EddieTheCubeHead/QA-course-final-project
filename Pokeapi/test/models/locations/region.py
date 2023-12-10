from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class Region(Fetchable):
    name: str
    locations: list[NamedApiResource]
    names: list[Name]
    main_generation: NamedApiResource | None
    pokedexes: list[NamedApiResource]
    version_groups: list[NamedApiResource]
