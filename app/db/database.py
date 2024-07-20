from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URL)
database = client.runaway_app

async def init_db():
    try:
        await client.server_info()
        print("Connected to MongoDB")
    except Exception as e:
        print(f"Unable to connect to MongoDB: {e}")