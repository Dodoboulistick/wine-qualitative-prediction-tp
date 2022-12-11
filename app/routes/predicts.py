from fastapi import APIRouter
from domain.predict.controller import predict_quality, predict_best_wine
from domain.wine.models.Wine import Wine

router = APIRouter(
    prefix="/predict"
)


@router.get("/")
async def get_best_wine() -> Wine:
    return await predict_best_wine()


@router.post("/")
async def get_quality(wine: Wine) -> int:
    return await predict_quality(wine)
