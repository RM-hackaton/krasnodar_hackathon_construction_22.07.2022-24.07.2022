from typing import List
from ..models.commercials import Commercial, CommercialIn
from ..repositories.commercials import CommercialsRepository
from fastapi import APIRouter, Depends, HTTPException, status, Response
from .depends import get_commercial_repository

router = APIRouter()


@router.get("/", response_model=List[Commercial])
async def read_commercials(
        response: Response,
        limit: int = 20,
        offset: int = 0,
        commercials: CommercialsRepository = Depends(get_commercial_repository),):
    response.headers["Content-type"] = "application/json; charset=utf-8"
    return await commercials.get_all(limit=limit, offset=offset)


@router.post("/", response_model=Commercial)
async def create_commercial(
        house_id: int,
        owner_id: int,
        commerce: CommercialIn,
        commercials: CommercialsRepository = Depends(get_commercial_repository)):
    return await commercials.create(house_id=house_id, owner_id=owner_id, commerce=commerce)


@router.put("/", response_model=Commercial)
async def update_commercial(
        id: int,
        house_id: int,
        owner_id: int,
        commerce: CommercialIn,
        commercials: CommercialsRepository = Depends(get_commercial_repository)):
    commercial = await commercials.get_by_id(id=id)
    if commercial is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
    return await commercials.update(id=id, house_id=house_id, owner_id=owner_id, commerce=commerce)


@router.delete("/")
async def delete_commercial(id: int,
                            commercials: CommercialsRepository = Depends(get_commercial_repository)):
    commercial = await commercials.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
    if commercial is None:
        raise not_found_exception
    await commercials.delete(id=id)
    return {"status": True}


@router.put("/update_owner", response_model=Commercial)
async def update_owner(
        id: int,
        owner_id: int,
        commerce_status: str,
        commercials: CommercialsRepository = Depends(get_commercial_repository)):
    commercial = await commercials.get_by_id(id=id)
    if commercial is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
    return await commercials.update_owner(id=id, owner_id=owner_id, commerce_status=commerce_status, commerce=commercial)
