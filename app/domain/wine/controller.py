from fastapi import FastAPI
from .models.Wine import Wine
from typing import Union
import csv

app = FastAPI()

async def get_all_wines() -> list:
    try:
        with open('datasource/Wines.csv', 'r') as f:
            wines = list(csv.DictReader(f, delimiter=','))
            return list(
                map(lambda wine:
                Wine(
                    fixed_acidity=wine['fixed_acidity'],
                    volatile_acidity=wine['volatile_acidity'],
                    citric_acid=wine['citric_acid'],
                    residual_sugar=wine['residual_sugar'],
                    chlorides=wine['chlorides'],
                    free_sulfur_dioxide=wine['free_sulfur_dioxide'],
                    total_sulfur_dioxide=wine['total_sulfur_dioxide'],
                    density=wine['density'],
                    pH=wine['pH'],
                    sulphates=wine['sulphates'],
                    alcohol=wine['alcohol'],
                    quality=wine['quality'] if wine['quality'] else None,
                    Id=wine['Id']),
                wines))
    except FileNotFoundError as e:
        print(e)
        return []


async def get_wine(id: int) -> Union[Wine,None]:
    wines = await get_all_wines()
    wine = list(filter(lambda wine: (wine.Id == id), wines))
    return wine[0] if wine else None


async def add_wine(wine: Wine) -> dict :
    if await get_wine(wine.Id):
        return {"error": "Wine with this Id already exists"}
    try:
        with open('datasource/Wines.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(wine.dict().values())
        return {"message": "Wine added"}
    except FileNotFoundError as e:
        return {"error": "Could not add wine", "message": e}


async def remove_wine(id: int) -> dict:
    wines = await get_all_wines()
    wine = await get_wine(id)
    if not wine:
        return {"error": "Wine with this Id does not exist"}
    try:
        with open('datasource/Wines.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(Wine.__fields__.keys())
            for wine in wines:
                if wine.Id != id:
                    writer.writerow(wine.dict().values())
        return {"message": "Wine deleted"}
    except FileNotFoundError as e:
        return {"error": "Could not delete wine", "message": e}