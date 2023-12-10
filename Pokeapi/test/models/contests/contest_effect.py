from models.common import Effect, FlavorText
from models.fetchable import Fetchable


class ContestEffect(Fetchable):
    appeal: int
    jam: int
    effect_entries: list[Effect]
    flavor_text_entries: list[FlavorText]
