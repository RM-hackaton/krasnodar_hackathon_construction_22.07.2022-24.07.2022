from pydantic import BaseModel


class BaseComplex(BaseModel):
    name: str
    district: str
    min_square: float
    min_price: float
    complex_class: str
    address: str
    img: str


class Complex(BaseComplex):
    id: int


class ComplexIn(BaseComplex):
    pass
