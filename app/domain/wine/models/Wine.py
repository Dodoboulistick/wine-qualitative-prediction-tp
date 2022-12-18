from pydantic import BaseModel
from typing import Union

class Wine(BaseModel):
    """A wine object

    Args:
        BaseModel: a pydantic model
    """
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
    Id: Union[int,None]

    def to_list(self, extra = False) -> list:
        """Convert a wine object to a list

        Args:
            extra (bool, optional): if True, the list will contain the wine quality and Id. Defaults to False.

        Returns:
            list: a list of wine attributes
        """
        if extra == False:
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
        elif extra == True:
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
                    self.alcohol,
                    self.quality,
                    self.Id]