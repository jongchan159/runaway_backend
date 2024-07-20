from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.db.database import user_collection
from bson import ObjectId

async def create_user(user: UserCreate) -> UserResponse:
    user_dict = user.dict()
    user_dict["_id"] = str(ObjectId())
    await user_collection.insert_one(user_dict)
    return UserResponse(**user_dict)

async def get_user(user_id: str) -> UserResponse:
    user = await user_collection.find_one({"_id": user_id})
    if user:
        return UserResponse(**user)
