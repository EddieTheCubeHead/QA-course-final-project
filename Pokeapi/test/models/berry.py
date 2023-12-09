from pydantic import BaseModel

from models.common import NamedApiResource
from models.fetchable import Fetchable


class BerryFlavorMap(BaseModel):
    potency: int
    flavor: NamedApiResource


class Berry(Fetchable):
    name: str
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    size: int
    smoothness: int
    soil_dryness: int
    firmness: NamedApiResource
    flavors: list[BerryFlavorMap]
    item: NamedApiResource
    natural_gift_type: NamedApiResource
