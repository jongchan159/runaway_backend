from fastapi import APIRouter, Depends, HTTPException
from app.schemas.course import CourseCreate, CourseResponse, CourseRecommendation
from app.services.course_service import CourseService
from app.api.dependencies import get_current_user
from typing import List

router = APIRouter()
course_service = CourseService()

@router.post("/create", response_model=CourseResponse)
async def create_course(
    course: CourseCreate,
    current_user: dict = Depends(get_current_user)
):
    return await course_service.create_course(current_user["id"], course)

@router.get("/popular", response_model=List[CourseResponse])
async def get_popular_courses(limit: int = 5):
    return await course_service.get_popular_courses(limit)

@router.post("/recommend", response_model=CourseResponse)
async def recommend_course(
    recommendation: CourseRecommendation,
    current_user: dict = Depends(get_current_user)
):
    recommended_course = await course_service.recommend_course(recommendation.drawn_route)
    if not recommended_course:
        raise HTTPException(status_code=404, detail="No suitable course found")
    return recommended_course