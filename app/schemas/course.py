from pydantic import BaseModel
from typing import List
from datetime import datetime

class CourseCreate(BaseModel):
    route: List[List[float]]

class CourseInDB(BaseModel):
    id: str
    created_by: str
    route: List[List[float]]
    recommendation_count: int
    created_at: datetime

class CourseResponse(CourseInDB):
    pass

class CourseRecommendation(BaseModel):
    drawn_route: List[List[float]]