from pydantic import BaseModel


class NamedApiResource(BaseModel):
    name: str
    url: str


class Name(BaseModel):
    name: str
    language: NamedApiResource


class Effect(BaseModel):
    effect: str
    language: NamedApiResource


class VerboseEffect(Effect):
    short_effect: str
