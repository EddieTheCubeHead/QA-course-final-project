from models.common import NamedApiResource, Name
from models.fetchable import Fetchable


class EvolutionTrigger(Fetchable):
    name: str
    names: list[Name]
    pokemon_species: list[NamedApiResource]
