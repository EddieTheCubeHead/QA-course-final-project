from models.common import FlavorText, NamedApiResource
from models.fetchable import Fetchable


class SuperContestEffect(Fetchable):
    appeal: int
    flavor_text_entries: list[FlavorText]
    moves: list[NamedApiResource]
