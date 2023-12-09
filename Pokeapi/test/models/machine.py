from models.common import NamedApiResource
from models.fetchable import Fetchable


class Machine(Fetchable):
    item: NamedApiResource
    move: NamedApiResource
    version_group: NamedApiResource
