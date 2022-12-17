from fastapi import APIRouter
from domain.wine.models.Wine import Wine
from domain.wine.controller import get_wine, get_all_wines, add_wine, remove_wine
from typing import Union

router = APIRouter(
    prefix="/api/wines"
)

@router.get("/")
async def read_wines() -> list:
    """Read wines from csv datasource

    Returns:
        list: wines from datasource
    """
    return await get_all_wines()

@router.post("/")
async def create_wine(wine: Wine) -> dict:
    """Add wine to csv datasource

    Args:
        wine (Wine): a Wine object (see domain.wine.models.Wine)

    Returns:
        dict: a message indicating success or failure
    """
    return await add_wine(wine)

@router.get("/{id}")
async def read_wine(id: int) -> Union[Wine,None]:
    """Read a wine from csv datasource

    Args:
        id (int): the id of the wine to read

    Returns:
        Union[Wine,None]: a Wine object with the given Id or None if not found
    """
    return await get_wine(id)

@router.delete("/{id}")
async def delete_wine(id: int) -> dict:
    """Delete a wine from csv datasource
    
    Args:
        id (int): the id of the wine to delete
        
    Returns:
        dict: a message indicating success or failure
    """
    return await remove_wine(id)
