from pydantic import BaseModel

from models.common import NamedApiResource
from models.fetchable import Fetchable


class ContestName(BaseModel):
    name: str
    color: str
    language: NamedApiResource


class ContestType(Fetchable):
    name: str
    berry_flavor: NamedApiResource
    names: list[ContestName]
