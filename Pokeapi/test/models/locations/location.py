from models.common import NamedApiResource, Name, GenerationGameIndex
from models.fetchable import Fetchable


class Location(Fetchable):
    name: str
    region: NamedApiResource | None
    names: list[Name]
    game_indices: list[GenerationGameIndex]
    areas: list[NamedApiResource]
