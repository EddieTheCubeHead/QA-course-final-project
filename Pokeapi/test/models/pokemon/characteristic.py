from models.common import NamedApiResource, Description
from models.fetchable import Fetchable


class Characteristic(Fetchable):
    gene_modulo: int
    possible_values: list[int]
    highest_stat: NamedApiResource
    descriptions: list[Description]
