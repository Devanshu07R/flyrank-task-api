from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Complete Flyrank task",
        "done": False
    },
    {
        "id": 3,
        "title": "Push project to github",
        "done": True
    }
]

@app.get("/")
def root():
    return {
        "name": "TaskAPI",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }
    
@app.get("/health")
def health():
    return {
        "status": "ok"
    }
    
@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task(id:int):
    for task in tasks:
        if task["id"] == id:
            return task
        
    raise HTTPException(
            status_code = 404,
            detail=f"Task {id} not found"
        )