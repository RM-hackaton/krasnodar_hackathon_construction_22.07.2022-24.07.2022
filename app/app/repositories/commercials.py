from typing import List, Optional
from ..models.commercials import Commercial, CommercialIn
from ..db.commercials import commercials
from .base import BaseRepository


class CommercialsRepository(BaseRepository):

    async def create(self, house_id: int, owner_id: int, commerce: CommercialIn) -> Commercial:
        commercial = Commercial(
            id=0,
            house_id=house_id,
            owner_id=owner_id,
            name=commerce.name,
            floor=commerce.floor,
            square=commerce.square,
            price=commerce.price,
            price_meter=commerce.price_meter,
            plan=commerce.plan,
            status='Свободно',
        )
        values = {**commercial.dict()}
        values.pop("id", None)
        query = commercials.insert().values(**values)
        commercial.id = await self.database.execute(query=query)
        return commercial

    async def update(self, id: int, house_id: int, owner_id: int, commerce: CommercialIn) -> Commercial:
        commercial = Commercial(
            id=id,
            house_id=house_id,
            owner_id=owner_id,
            name=commerce.name,
            floor=commerce.floor,
            square=commerce.square,
            price=commerce.price,
            price_meter=commerce.price_meter,
            plan=commerce.plan,
            status=commerce.status,
        )
        values = {**commercial.dict()}
        values.pop("id", None)
        query = commercials.update().where(commercials.c.id == id).values(**values)
        await self.database.execute(query=query)
        return commercial

    async def update_owner(self, id: int, owner_id: int, commerce_status: str, commerce) -> Commercial:
        this_commerce = commerce
        commercial = Commercial(
            id=id,
            owner_id=owner_id,
            house_id=this_commerce.house_id,
            status=commerce_status,
            name=this_commerce.name,
            floor=this_commerce.floor,
            square=this_commerce.square,
            price=this_commerce.price,
            price_meter=this_commerce.price_meter,
            plan=this_commerce.plan,
        )
        values = {**commercial.dict()}
        values.pop("id", None)
        query = commercials.update().where(commercials.c.id == id).values(**values)
        await self.database.execute(query=query)
        return commercial

    async def get_all(self, limit: int = 20, offset: int = 0) -> List[Commercial]:
        query = commercials.select().limit(limit).offset(offset)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int):
        query = commercials.delete().where(commercials.c.id == id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Optional[Commercial]:
        query = commercials.select().where(commercials.c.id == id)
        commercial = await self.database.fetch_one(query=query)
        if commercial is None:
            return None
        return Commercial.parse_obj(commercial)
