from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title = "Task API Auth",
    description = "Week 4 - Authentication with Supabase",
    version = "4.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Week 4 authentication API is running successfully!"
    }