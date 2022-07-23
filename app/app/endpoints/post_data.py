from get_data import get_complexes, get_houses_and_commercials
from fastapi import APIRouter, Depends

from repositories.post_data import PostDataRepository
from .depends import get_commercial_repository, \
    get_house_repository, \
    get_complex_repository, \
    get_post_repository

router = APIRouter()


@router.post("/complexes")
async def create_complexes(
        complexes: PostDataRepository = Depends(get_post_repository)):
    compls = get_complexes()

    return await complexes.create_complexes(compls=compls)


@router.post("/houses_and_commercials")
async def create_houses_and_commercials(
        houses: PostDataRepository = Depends(get_post_repository),
        commercials: PostDataRepository = Depends(get_post_repository)):
    homes, commers = get_houses_and_commercials()

    await houses.create_houses(homes=homes)

    await commercials.create_commercials(commers=commers)

    return {'status': 200}

