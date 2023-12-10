from models.common import NamedApiResource, Description, Name
from models.fetchable import Fetchable


class MoveLearnMethod(Fetchable):
    name: str
    descriptions: list[Description]
    names: list[Name]
    version_groups: list[NamedApiResource]
