from pydantic import BaseModel


class Fetchable(BaseModel):
    id: int
