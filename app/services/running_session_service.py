from app.models.running_session import RunningSessionModel
from app.schemas.running_session import RunningSessionCreate, RunningSessionUpdate
from app.db.database import database
from bson import ObjectId

class RunningSessionService:
    async def create_session(self, user_id: str, session: RunningSessionCreate):
        session_data = session.dict()
        session_data["user_id"] = ObjectId(user_id)
        new_session = RunningSessionModel(**session_data)
        result = await database.running_sessions.insert_one(new_session.dict(by_alias=True))
        return await self.get_session(result.inserted_id)

    async def get_session(self, session_id: str):
        session = await database.running_sessions.find_one({"_id": ObjectId(session_id)})
        if session:
            return RunningSessionModel(**session)

    async def update_session(self, session_id: str, session_update: RunningSessionUpdate):
        update_data = session_update.dict(exclude_unset=True)
        await database.running_sessions.update_one(
            {"_id": ObjectId(session_id)},
            {"$set": update_data}
        )
        return await self.get_session(session_id)

    async def get_user_sessions(self, user_id: str, limit: int = 10):
        cursor = database.running_sessions.find({"user_id": ObjectId(user_id)}).sort("start_time", -1).limit(limit)
        sessions = await cursor.to_list(length=limit)
        return [RunningSessionModel(**session) for session in sessions]