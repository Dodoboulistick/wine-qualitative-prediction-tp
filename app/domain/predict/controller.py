import pandas as pd
from domain.wine.models.Wine import Wine
from domain.wine.controller import get_all_wines
from domain.model.controller import get_serialized_model

async def predict_wine_quality(wine : Wine) -> dict:
    """ predict the quality of a wine given its attributes 

    Args:
        wine (Wine): the wine to predict

    Returns:
        dict: a dictionary containing the wine quality, e.g {'wine_quality': "good"}
    """
    model = await get_serialized_model()
    wine = wine.to_list()
    quality = model.predict(wine)[0]
    return {'wine_quality': quality}

async def predict_best_wine() -> Wine:
    """return the feature of the virtually best wine

    Returns:
        Wine: a Wine object containing the best wine features
    """
    wines = await get_all_wines()
    wines = dict(map(lambda wine: (wine.Id, wine), wines))
    wines = list(map(lambda wine: wine.to_list(extra = True), wines.values()))
    wines = pd.DataFrame(wines, columns = ['fixed_acidity', 'volatile_acidity', 
                                            'citric_acid', 'residual_sugar',
                                            'chlorides', 'free_sulfur_dioxide', 
                                            'total_sulfur_dioxide', 'density', 
                                            'pH', 'sulphates', 
                                            'alcohol', 'quality', 
                                            'Id'])
    wines.dropna(inplace = True)
    wines['quality'] = wines['quality'].astype(int)
    wines["quality"] = wines["quality"].apply(lambda x: 'good' if x >= 7 else 'bad')
    wines = wines[wines['quality'] == 'good']
    best_wine = wines[wines['alcohol'] == wines['alcohol'].max()]
    return Wine(**best_wine.to_dict('records')[0])
    