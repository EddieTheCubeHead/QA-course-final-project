from pydantic import BaseModel
from typing import List

class HeaderData(BaseModel):
  title: list[str]


class RecordData(BaseModel):
  item: list[str]


class FileData(BaseModel):
  header: HeaderData
  record: list[RecordData]


class File(BaseModel):
  file: FileData
