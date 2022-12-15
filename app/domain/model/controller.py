from .models.Model import Model
from domain.wine.models.Wine import Wine
from domain.wine.controller import add_wine



async def get_serialized_model() -> Model:
    """return the serialized model
    
    Returns:
        Model: the serialized model
    """
    model = Model(name="RF Classifier", version="1.0", model_path="datasource/wine_quality.pkl", data_path="datasource/Wines.csv", metrics_path="datasource/model_metrics.json")
    return model

async def get_attributes() -> dict:
    """return the attributes of the model, e.g. name, version, parameters, metrics

    Returns:
        dict: dict with 3 keys: Global_info, parameters, metrics, each key contains a dict with the corresponding attributes
    """
    model = await get_serialized_model()
    return { "Global_info" : {"name": model.name},
            "parameters": model.parameters,
            "metrics": model.metrics,}


async def add_wine_to_model(wine : Wine)-> None:
    """add a wine to the model 
    """
    await add_wine(wine)

async def retrain():
    """get the model and retrain it with the new data
    """
    model = await get_serialized_model()
    model.train_model()