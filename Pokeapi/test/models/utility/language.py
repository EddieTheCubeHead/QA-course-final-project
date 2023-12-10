from models.common import Name
from models.fetchable import Fetchable


class Language(Fetchable):
    name: str
    official: bool
    iso639: str
    iso3166: str
    names: list[Name]
