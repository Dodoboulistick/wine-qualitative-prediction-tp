from pydantic import BaseModel

#FIXME: Verify the class attributes for the model
class Model(BaseModel):
    name: str
    version: str
    path: str
    parameters: list
    metrics: list