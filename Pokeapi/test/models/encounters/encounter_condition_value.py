from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class EncounterConditionValue(Fetchable):
    name: str
    condition: NamedApiResource
    names: list[Name]
