from .models.Model import Model

#TODO: Generate a MEGA/Onedrive link to download the model?
async def get_serialized_model() -> str:
    return "url"

async def get_attributes() -> Model:
    return Model(
        name="",
        version="",
        path="",
        parameters=[],
        metrics=[],
    )

async def add_whine_to_model(id: int):
    pass

async def retrain():
    pass
