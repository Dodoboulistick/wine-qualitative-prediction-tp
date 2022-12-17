from domain.wine.models.Wine import Wine
from domain.wine.controller import get_all_wines
from domain.model.controller import get_serialized_model

async def predict_wine_quality(wine : Wine) -> dict:
    model = await get_serialized_model()
    wine = wine.to_list()
    quality = model.predict(wine)[0]
    return {'wine_quality': quality}

async def predict_best_wine() -> Wine:
    wines = await get_all_wines()
    ranked_wines = sorted(wines, key=lambda wine: int(wine.quality), reverse=True)
    return ranked_wines[0]
    