from pydantic import BaseModel


class BaseCommercial(BaseModel):
    name: str
    floor: int
    square: float
    price: float
    price_meter: float
    plan: str
    status: str


class Commercial(BaseCommercial):
    id: int
    house_id: int
    owner_id: int

class CommercialIn(BaseCommercial):
    pass
