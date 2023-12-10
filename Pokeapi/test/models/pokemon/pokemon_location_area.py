from pydantic import RootModel, BaseModel

from models.common import NamedApiResource, VersionEncounterDetail


class PokemonLocationArea(BaseModel):
    location_area: NamedApiResource
    version_details: list[VersionEncounterDetail]


class PokemonLocationAreaList(RootModel):
    root: list[PokemonLocationArea]
