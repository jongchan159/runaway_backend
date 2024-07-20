from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class RunningSessionCreate(BaseModel):
    start_time: datetime

class RunningSessionUpdate(BaseModel):
    end_time: Optional[datetime]
    distance: Optional[float]
    duration: Optional[int]
    average_pace: Optional[float]
    route: Optional[List[List[float]]]
    strength: Optional[int]

class RunningSessionInDB(BaseModel):
    id: str
    user_id: str
    start_time: datetime
    end_time: Optional[datetime]
    distance: float
    duration: int
    average_pace: float
    route: List[List[float]]
    strength: int

class RunningSessionResponse(RunningSessionInDB):
    pass