from pydantic import BaseModel


class BaseHouse(BaseModel):
    liter: int
    parking: str
    finished: str


class House(BaseHouse):
    id: int
    complex_id: int


class HouseIn(BaseHouse):
    pass
