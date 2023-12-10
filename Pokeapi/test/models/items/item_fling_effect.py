from models.common import NamedApiResource, Effect
from models.fetchable import Fetchable


class ItemFlingEffect(Fetchable):
    name: str
    effect_entries: list[Effect]
    items: list[NamedApiResource]
