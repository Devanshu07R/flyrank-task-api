from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.models import Task
from app.routes import router

Base.metadata.create_all(bind=engine)



def seed_database():
    db: Session = SessionLocal()
    
    try:
        if db.query(Task).count() == 0:
            sample_tasks = [
                Task(title="Learn FastAPI", done=False),
                Task(title="Build CRUD API", done=False),
                Task(title="Practice SQLite", done=False)
            ]
            
            db.add_all(sample_tasks)
            db.commit()
    finally:
        db.close()
        
seed_database()


app = FastAPI(
    title = "Task API",
    description = "Week 3 A2 Connecting CRUD to SQLite database",
    version = "3.0"
)
app.include_router(router)