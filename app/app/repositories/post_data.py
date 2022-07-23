from typing import List

from models.housing_complexes import Complex
from models.houses import House
from models.commercials import Commercial
from db.housing_complexes import housing_complexes
from db.houses import houses
from db.commercials import commercials
from .base import BaseRepository


class PostDataRepository(BaseRepository):

    async def create_complexes(self, compls: dict) -> dict:
        for name, compl in compls.items():
            complex = Complex(
                id=0,
                name=name,
                district=compl['district'],
                min_square=compl['min_square'],
                min_price=compl['min_price'],
                complex_class=compl['complex_class'],
                address=compl['address'],
                img=compl['img'],
            )
            values = {**complex.dict()}
            values.pop("id", None)
            query = housing_complexes.insert().values(**values)
            complex.id = await self.database.execute(query=query)
        return {'status': 200}

    async def create_houses(self, homes: dict) -> dict:
        for name, home in homes.items():
            house = House(
                id=0,
                complex_id=home['complex_id'],
                liter=home['liter'],
                parking=home['parking'],
                finished=home['finished'],
            )
            values = {**house.dict()}
            values.pop("id", None)
            query = houses.insert().values(**values)
            house.id = await self.database.execute(query=query)
        return {'status': 200}

    async def create_commercials(self, commers: dict) -> dict:
        for name, commer in commers.items():
            commercial = Commercial(
                id=0,
                house_id=commer['house_id'],
                owner_id=commer['owner_id'],
                name=name,
                floor=commer['floor'],
                square=commer['square'],
                price=commer['price'],
                price_meter=commer['price_meter'],
                status=commer['status'],
                plan=commer['plan'],
            )
            values = {**commercial.dict()}
            values.pop("id", None)
            query = commercials.insert().values(**values)
            commercial.id = await self.database.execute(query=query)
        return {'status': 200}
