from pydantic import BaseModel
from typing import List

class Room(BaseModel):
    id: int
    type: str
    area: float

class Relation(BaseModel):
    from_id: int
    to_id: int
    type: str

class Layout(BaseModel):
    rooms: List[Room]
    relations: List[Relation]