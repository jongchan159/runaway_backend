from fastapi import FastAPI
from app.api.routes import users, running_sessions, courses, stats

app = FastAPI()

# 라우터 추가
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(running_sessions.router, prefix="/running_sessions", tags=["running_sessions"])
app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(stats.router, prefix="/stats", tags=["stats"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

