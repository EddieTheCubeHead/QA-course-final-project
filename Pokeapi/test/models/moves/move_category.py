from models.common import NamedApiResource, Description
from models.fetchable import Fetchable


class MoveCategory(Fetchable):
    name: str
    moves: list[NamedApiResource]
    descriptions: list[Description]
