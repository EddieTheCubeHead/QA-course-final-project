from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class BerryFirmness(Fetchable):
    name: str
    berries: list[NamedApiResource]
    names: list[Name]
