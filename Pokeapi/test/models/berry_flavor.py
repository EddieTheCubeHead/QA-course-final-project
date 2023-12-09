from pydantic import BaseModel

from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class FlavorBerryMap(BaseModel):
    potency: int
    berry: NamedApiResource


class BerryFlavor(Fetchable):
    name: str
    berries: list[FlavorBerryMap]
    names: list[Name]
