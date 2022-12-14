from fastapi import APIRouter
from domain.model.models.Model import Model
from domain.model.controller import get_serialized_model, get_attributes, add_wine_to_model, retrain

router = APIRouter(
    prefix="/api/model"
)

model = Model(name="RF Classifier", version="1.0", model_path="datasource/wine_quality.pkl", data_path="datasource/Wines.csv", metrics_path="datasource/model_metrics.json", parameters={'n_estimators': 300})



@router.get("/")
async def get_model() -> Model:
    return {"model": "model"}

@router.get("/description")
async def get_model_info() -> dict:
    return get_attributes()

@router.put("/")
async def update_model(id: int) -> None:
    return add_wine_to_model(id)

@router.post("/retrain")
async def retrain_model() -> None:
    return retrain()