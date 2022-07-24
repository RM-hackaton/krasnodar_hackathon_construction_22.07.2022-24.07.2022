from typing import List
from ..models.housing_complexes import Complex, ComplexIn
from ..repositories.housing_complexes import HousingComplexRepository
from fastapi import APIRouter, Depends, HTTPException, status, Response
from .depends import get_complex_repository

router = APIRouter()


@router.get("/", response_model=List[Complex])
async def read_complexes(
        response: Response,
        limit: int = 20,
        offset: int = 0,
        complexes: HousingComplexRepository = Depends(get_complex_repository),):
    response.headers["Content-type"] = "application/json; charset=utf-8"
    return await complexes.get_all(limit=limit, offset=offset)


@router.post("/", response_model=Complex)
async def create_complex(
        compl: ComplexIn,
        complexes: HousingComplexRepository = Depends(get_complex_repository)):
    return await complexes.create(compl=compl)


@router.put("/", response_model=Complex)
async def update_complex(
        id: int,
        compl: ComplexIn,
        complexes: HousingComplexRepository = Depends(get_complex_repository)):
    complex = await complexes.get_by_id(id=id)
    if complex is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
    return await complexes.update(id=id, compl=compl)


@router.delete("/")
async def delete_complex(id: int,
                         complexes: HousingComplexRepository = Depends(get_complex_repository)):
    complex = await complexes.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
    if complex is None:
        raise not_found_exception
    await complexes.delete(id=id)
    return {"status": True}
