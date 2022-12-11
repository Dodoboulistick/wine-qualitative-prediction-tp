from domain.wine.models.Wine import Wine

#TODO: Use the model to predict the quality of the wine
async def predict_quality(wine: Wine) -> int:
    print(wine)
    return 0

#TODO: Use the model to predict the best wine
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
        quality=6,
    )