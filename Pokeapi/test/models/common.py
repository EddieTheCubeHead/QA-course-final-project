from pydantic import BaseModel


class NamedAPIResource(BaseModel):
    name: str
    url: str


class Name(BaseModel):
    name: str
    language: NamedAPIResource


class Effect(BaseModel):
    effect: str
    language: NamedAPIResource


class VerboseEffect(Effect):
    short_effect: str
