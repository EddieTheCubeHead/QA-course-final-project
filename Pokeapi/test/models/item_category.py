from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class ItemCategory(Fetchable):
    name: str
    items: list[NamedApiResource]
    names: list[Name]
    pocket: NamedApiResource
