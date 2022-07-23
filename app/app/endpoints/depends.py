from repositories.housing_complexes import HousingComplexRepository
from repositories.houses import HouseRepository
from repositories.commercials import CommercialsRepository
from repositories.post_data import PostDataRepository
from db.base import database


def get_complex_repository() -> HousingComplexRepository:
    return HousingComplexRepository(database)


def get_house_repository() -> HouseRepository:
    return HouseRepository(database)


def get_commercial_repository() -> CommercialsRepository:
    return CommercialsRepository(database)


def get_post_repository() -> PostDataRepository:
    return PostDataRepository(database)
