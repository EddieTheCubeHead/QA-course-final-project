from typing import TypeVar, Generic

from pydantic import BaseModel

from models.fetchable import Fetchable


class ApiResource(BaseModel):
    url: str


class NamedApiResource(ApiResource):
    name: str


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
    results: list[ApiResource]


class NamedListResult(BaseModel):
    count: int
    next: str | None
    previous: str | None
    results: list[NamedApiResource]


class FlavorText(BaseModel):
    flavor_text: str
    language: NamedApiResource
