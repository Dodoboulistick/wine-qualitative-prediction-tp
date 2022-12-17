import pytest
from domain.wine.models.Wine import Wine
from domain.wine.controller import add_wine, get_wine

pytest_plugins = ('pytest_asyncio',)

@pytest.mark.asyncio
async def test_create_wine_without_id():
    wine_without_id = Wine(
        fixed_acidity=7.4,
        volatile_acidity=0.7,
        citric_acid=0,
        residual_sugar=1.9,
        chlorides=0.076,
        free_sulfur_dioxide=11,
        total_sulfur_dioxide=34,
        density=0.9978,
        pH=3.51,
        sulphates=0.56,
        alcohol=9.4,
        quality=None,
        Id=None,
    )
    assert await add_wine(wine_without_id) == {'message': 'Wine added'}

@pytest.mark.asyncio
async def test_create_wine_with_id():
    wine_with_id = Wine(
        fixed_acidity=7.4,
        volatile_acidity=0.7,
        citric_acid=0,
        residual_sugar=1.9,
        chlorides=0.076,
        free_sulfur_dioxide=11,
        total_sulfur_dioxide=34,
        density=0.9978,
        pH=3.51,
        sulphates=0.56,
        alcohol=9.4,
        quality=None,
        Id=987654321,
    )
    await add_wine(wine_with_id)
    assert await add_wine(wine_with_id) == {'error': 'Wine with this Id already exists'}

@pytest.mark.asyncio
async def test_get_wine():
    wine = Wine(
        fixed_acidity=7.4,
        volatile_acidity=0.7,
        citric_acid=0,
        residual_sugar=1.9,
        chlorides=0.076,
        free_sulfur_dioxide=11,
        total_sulfur_dioxide=34,
        density=0.9978,
        pH=3.51,
        sulphates=0.56,
        alcohol=9.4,
        quality=None,
        Id=999999999,
    )
    await add_wine(wine)
    assert await get_wine(wine.Id) == wine

