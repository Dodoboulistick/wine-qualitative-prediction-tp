from fastapi import FastAPI
from routes import models, predicts, wines

app = FastAPI(
    title="WineApp",
    description="WineApp is a simple API to predict wine quality 🍷",
    version="0.1",
    contact=
    {
        "name": "Alexandre Lagarrue, Dorian Mailhé",
        "url": "https://dorian-mailhe.fr",
        "email": "lagarrueal@cy-tech.fr",
    }
)

app.include_router(models.router)
app.include_router(predicts.router)
app.include_router(wines.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}