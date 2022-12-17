from fastapi import APIRouter
from domain.predict.controller import predict_wine_quality, predict_best_wine
from domain.wine.models.Wine import Wine

router = APIRouter(
    prefix="/api/predict"
)


@router.get("/")
async def get_best_wine() -> Wine:
    """Get the best wine from csv datasource: for now, the best wine is the one with the highest quality (existing)

    Returns:
        list: the best wine from datasource
    """
    return await predict_best_wine()


@router.post("/")
async def predict_quality(wine: Wine) -> str:
    """Predict the quality of a wine
    
    Args:
        wine (Wine): a Wine object (see domain.wine.models.Wine)
        
    Returns:
        str: the predicted quality of the wine
    """
    return await predict_wine_quality(wine)
