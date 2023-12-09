from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class EncounterCondition(Fetchable):
    name: str
    names: list[Name]
    values: list[NamedApiResource]
