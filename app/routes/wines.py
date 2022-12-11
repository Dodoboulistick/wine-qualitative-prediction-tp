from fastapi import APIRouter
from domain.wine.models.Wine import Wine
from domain.wine.controller import get_wine, get_all_wines, add_wine, remove_wine
from typing import Union

router = APIRouter(
    prefix="/wines"
)

@router.get("/")
async def read_wines() -> list:
    return await get_all_wines()

@router.post("/")
async def create_wine(wine: Wine) -> dict:
    return await add_wine(wine)

@router.get("/{id}")
async def read_wine(id: int) -> Union[Wine,None]:
    return await get_wine(id)

@router.delete("/{id}")
async def delete_wine(id: int) -> dict:
    return await remove_wine(id)
