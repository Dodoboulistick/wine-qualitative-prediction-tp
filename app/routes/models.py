from fastapi import APIRouter
from domain.model.models.Model import Model
from domain.model.controller import get_serialized_model, get_attributes, add_wine_to_model, retrain

router = APIRouter(
    prefix="/api/model"
)

@router.get("/")
async def get_model() -> dict:
    return {"model": await get_serialized_model()}

@router.get("/description")
async def get_model_info() -> dict:
    return {"Model_informations" : await get_attributes()}

@router.put("/")
async def update_model(id: int) -> None:
    return await add_wine_to_model(id)

@router.post("/retrain")
async def retrain_model() -> None:
    return await retrain()
