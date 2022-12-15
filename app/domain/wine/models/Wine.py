from pydantic import BaseModel
from typing import Union

class Wine(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float
    quality: Union[str,None]
    Id: int

    def to_list(self) -> list:
        return [self.fixed_acidity, 
                self.volatile_acidity, 
                self.citric_acid, 
                self.residual_sugar, 
                self.chlorides, 
                self.free_sulfur_dioxide, 
                self.total_sulfur_dioxide, 
                self.density, 
                self.pH, 
                self.sulphates, 
                self.alcohol]