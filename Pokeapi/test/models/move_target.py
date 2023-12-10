from models.common import NamedApiResource, Description, Name
from models.fetchable import Fetchable


class MoveTarget(Fetchable):
    name: str
    descriptions: list[Description]
    moves: list[NamedApiResource]
    names: list[Name]
