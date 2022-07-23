from typing import List
from models.houses import House, HouseIn
from repositories.houses import HouseRepository
from fastapi import APIRouter, Depends, HTTPException, status, Response
from .depends import get_house_repository

router = APIRouter()


@router.get("/", response_model=List[House])
async def read_houses(
        response: Response,
        limit: int = 20,
        offset: int = 0,
        houses: HouseRepository = Depends(get_house_repository),):
    response.headers["Content-type"] = "application/json; charset=utf-8"
    return await houses.get_all(limit=limit, offset=offset)


@router.post("/", response_model=House)
async def create_house(
        complex_id: int,
        home: HouseIn,
        houses: HouseRepository = Depends(get_house_repository)):
    return await houses.create(complex_id=complex_id, home=home)


@router.put("/", response_model=House)
async def update_house(
        id: int,
        complex_id: int,
        home: HouseIn,
        houses: HouseRepository = Depends(get_house_repository)):
    house = await houses.get_by_id(id=id)
    if house is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
    return await houses.update(id=id, complex_id=complex_id, home=home)


@router.delete("/")
async def delete_house(id: int,
                       houses: HouseRepository = Depends(get_house_repository)):
    house = await houses.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
    if house is None:
        raise not_found_exception
    await houses.delete(id=id)
    return {"status": True}
