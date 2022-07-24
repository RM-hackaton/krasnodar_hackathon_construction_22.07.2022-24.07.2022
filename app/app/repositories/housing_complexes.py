from typing import List, Optional
from ..models.housing_complexes import Complex, ComplexIn
from ..db.housing_complexes import housing_complexes
from .base import BaseRepository


class HousingComplexRepository(BaseRepository):

    async def create(self, compl: ComplexIn) -> Complex:
        complex = Complex(
            id=0,
            name=compl.name,
            district=compl.district,
            min_square=compl.min_square,
            min_price=compl.min_price,
            complex_class=compl.complex_class,
            address=compl.address,
            img=compl.img,
        )
        values = {**complex.dict()}
        values.pop("id", None)
        query = housing_complexes.insert().values(**values)
        complex.id = await self.database.execute(query=query)
        return complex

    async def update(self, id: int, compl: ComplexIn) -> Complex:
        complex = Complex(
            id=id,
            name=compl.name,
            district=compl.district,
            min_square=compl.min_square,
            min_price=compl.min_price,
            complex_class=compl.complex_class,
            address=compl.address,
            img=compl.img,
        )
        values = {**complex.dict()}
        values.pop("id", None)
        query = housing_complexes.update().where(housing_complexes.c.id == id).values(**values)
        await self.database.execute(query=query)
        return complex

    async def get_all(self, limit: int = 20, offset: int = 0) -> List[Complex]:
        query = housing_complexes.select().limit(limit).offset(offset)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int):
        query = housing_complexes.delete().where(housing_complexes.c.id == id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Optional[Complex]:
        query = housing_complexes.select().where(housing_complexes.c.id == id)
        complex = await self.database.fetch_one(query=query)
        if complex is None:
            return None
        return Complex.parse_obj(complex)
