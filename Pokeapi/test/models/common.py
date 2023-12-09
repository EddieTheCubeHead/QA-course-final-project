from typing import TypeVar, Generic

from pydantic import BaseModel

from models.fetchable import Fetchable


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


class ListResult(BaseModel):
    count: int
    next: str | None
    previous: str | None
    results: list[NamedApiResource]
