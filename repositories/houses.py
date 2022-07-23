from typing import List, Optional
from models.houses import House, HouseIn
from db.houses import houses
from .base import BaseRepository


class HouseRepository(BaseRepository):

    async def create(self, complex_id: int, home: HouseIn) -> House:
        house = House(
            id=0,
            complex_id=complex_id,
            liter=home.liter,
            parking=home.parking,
            finished=home.finished,
        )
        values = {**house.dict()}
        values.pop("id", None)
        query = houses.insert().values(**values)
        house.id = await self.database.execute(query=query)
        return house

    async def update(self, id: int, complex_id: int, home: HouseIn) -> House:
        house = House(
            id=id,
            complex_id=complex_id,
            liter=home.liter,
            parking=home.parking,
            finished=home.finished,
        )
        values = {**house.dict()}
        values.pop("id", None)
        query = houses.update().where(houses.c.id == id).values(**values)
        await self.database.execute(query=query)
        return house

    async def get_all(self, limit: int = 20, offset: int = 0) -> List[House]:
        query = houses.select().limit(limit).offset(offset)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int):
        query = houses.delete().where(houses.c.id == id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Optional[House]:
        query = houses.select().where(houses.c.id == id)
        house = await self.database.fetch_one(query=query)
        if house is None:
            return None
        return House.parse_obj(house)
