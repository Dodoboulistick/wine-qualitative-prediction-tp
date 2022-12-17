from fastapi import APIRouter
from domain.model.models.Model import Model
from domain.wine.models.Wine import Wine
from domain.model.controller import get_serialized_model, get_attributes, add_wine_to_model, retrain


router = APIRouter(
    prefix="/api/model"
)

@router.get("/")
async def get_model() -> dict:
    """Get the serialized model

    Returns:
        dict: the serialized model
    """
    await get_serialized_model()

@router.get("/description")
async def get_model_info() -> dict:
    """Get the model information

    Returns:
        dict: the model information
    """
    return {"Model_information" : await get_attributes()}

@router.put("/")
async def update_model(wine : Wine) -> dict:
    """Update the model with a new wine

    Args:
        wine (Wine): a Wine object (see domain.wine.models.Wine)

    Returns:
        dict: a message indicating success or failure
    """
    return await add_wine_to_model(wine)

@router.post("/retrain")
async def retrain_model() -> None:
    """Retrain the model with the new data
    """
    return await retrain()
