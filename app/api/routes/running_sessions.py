from fastapi import APIRouter, Depends, HTTPException
from app.schemas.running_session import RunningSessionCreate, RunningSessionUpdate, RunningSessionResponse
from app.services.running_session_service import RunningSessionService
from app.api.dependencies import get_current_user
from typing import List

router = APIRouter()
running_session_service = RunningSessionService()

@router.post("/start", response_model=RunningSessionResponse)
async def start_running_session(
    session: RunningSessionCreate,
    current_user: dict = Depends(get_current_user)
):
    return await running_session_service.create_session(current_user["id"], session)

@router.put("/{session_id}", response_model=RunningSessionResponse)
async def update_running_session(
    session_id: str,
    session_update: RunningSessionUpdate,
    current_user: dict = Depends(get_current_user)
):
    updated_session = await running_session_service.update_session(session_id, session_update)
    if not updated_session:
        raise HTTPException(status_code=404, detail="Running session not found")
    return updated_session

@router.get("/user", response_model=List[RunningSessionResponse])
async def get_user_running_sessions(
    limit: int = 10,
    current_user: dict = Depends(get_current_user)
):
    return await running_session_service.get_user_sessions(current_user["id"], limit)