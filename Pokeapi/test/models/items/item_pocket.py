from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class ItemPocket(Fetchable):
    name: str
    categories: list[NamedApiResource]
    names: list[Name]
