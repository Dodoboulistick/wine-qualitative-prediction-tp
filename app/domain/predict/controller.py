from domain.wine.models.Wine import Wine
from domain.model.controller import get_serialized_model

async def predict_wine_quality(wine : Wine) -> dict:
    model = await get_serialized_model()
    wine = wine.to_list()
    quality = model.predict(wine)[0]
    return {'wine_quality': quality}

#TODO: Use the model to predict the best wine ! 
async def predict_best_wine() -> Wine:
    return Wine(
        fixed_acidity=6.3,
        volatile_acidity=0.3,
        citric_acid=0.34,
        residual_sugar=1.6,
        chlorides=0.049,
        free_sulfur_dioxide=14,
        total_sulfur_dioxide=132,
        density=0.994,
        pH=3.3,
        sulphates=0.49,
        alcohol=9.5,
        quality='bad',
    )