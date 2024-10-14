from pydantic import BaseModel
from typing import List, Any


class Ok200(BaseModel):
    status: int = 200
    message: str = "Ok"
    records: List[Any] = []


class Created201(BaseModel):
    status: int = 201
    message: str = "Created"
    records: List[Any] = []
