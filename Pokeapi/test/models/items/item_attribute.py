from models.common import NamedApiResource, Name, Description
from models.fetchable import Fetchable


class ItemAttribute(Fetchable):
    name: str
    items: list[NamedApiResource]
    names: list[Name]
    descriptions: list[Description]
