from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class MoveAilment(Fetchable):
    name: str
    moves: list[NamedApiResource]
    names: list[Name]
