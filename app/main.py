from fastapi import FastAPI

from app.database import Base, engine
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "TaskAPI",
    description = "Week 3 Backend AI Engineering Assignment - FlyRank AI",
    version = "2.0"
)
app.include_router(router)