from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class Version(Fetchable):
    name: str
    names: list[Name]
    version_group: NamedApiResource
