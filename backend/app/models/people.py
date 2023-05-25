import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Person(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    age: str = Field(...)
    gender: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Don",
                "age": "15",
                "gender": "M"
            }
        }


class PersonUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    gender: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "Name": "Don",
                "age": "16",
                "gender": "M"
            }
        }