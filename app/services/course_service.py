from app.models.course import CourseModel
from app.schemas.course import CourseCreate, CourseRecommendation
from app.db.database import database
from bson import ObjectId

class CourseService:
    async def create_course(self, user_id: str, course: CourseCreate):
        course_data = course.dict()
        course_data["created_by"] = ObjectId(user_id)
        new_course = CourseModel(**course_data)
        result = await database.courses.insert_one(new_course.dict(by_alias=True))
        return await self.get_course(result.inserted_id)

    async def get_course(self, course_id: str):
        course = await database.courses.find_one({"_id": ObjectId(course_id)})
        if course:
            return CourseModel(**course)

    async def get_popular_courses(self, limit: int = 5):
        cursor = database.courses.find().sort("recommendation_count", -1).limit(limit)
        courses = await cursor.to_list(length=limit)
        return [CourseModel(**course) for course in courses]

    async def recommend_course(self, drawn_route: List[List[float]]):
        # 여기에 코스 추천 알고리즘을 구현해야 합니다.
        # 이 예제에서는 간단히 가장 인기 있는 코스를 반환합니다.
        popular_courses = await self.get_popular_courses(1)
        if popular_courses:
            return popular_courses[0]
        return None