from models.common import Name
from models.fetchable import Fetchable


class EncounterMethod(Fetchable):
    name: str
    order: int
    names: list[Name]
