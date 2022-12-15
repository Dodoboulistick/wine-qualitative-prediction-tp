from fastapi import APIRouter
from domain.model.models.Model import Model
from domain.wine.models.Wine import Wine
from domain.model.controller import get_serialized_model, get_attributes, add_wine_to_model, retrain


router = APIRouter(
    prefix="/api/model"
)

@router.get("/")
async def get_model() -> dict:
    await get_serialized_model()

@router.get("/description")
async def get_model_info() -> dict:
    return {"Model_informations" : await get_attributes()}

@router.put("/")
async def update_model(wine : Wine) -> None:
    return await add_wine_to_model(wine)

@router.post("/retrain")
async def retrain_model() -> None:
    return await retrain()
