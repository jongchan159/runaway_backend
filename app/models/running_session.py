from pydantic import BaseModel, Field
from datetime import datetime
from typing import List
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class RunningSessionModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId
    start_time: datetime = Field(default_factory=datetime.utcnow)
    end_time: datetime = None
    distance: float = 0
    duration: int = 0  # in seconds
    average_pace: float = 0
    route: List[List[float]] = []
    strength: int = 5

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}