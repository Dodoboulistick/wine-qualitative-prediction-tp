from fastapi import APIRouter
from domain.predict.controller import predict_wine_quality, predict_best_wine
from domain.wine.models.Wine import Wine

router = APIRouter(
    prefix="/api/predict"
)


@router.get("/")
async def get_best_wine() -> Wine:
    return await predict_best_wine()


@router.post("/")
async def predict_quality(wine: Wine) -> str:
    return await predict_wine_quality(wine)
