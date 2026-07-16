from fastapi import FastAPI, HTTPException, Response
from fastapi import Response
from pydantic import BaseModel

app = FastAPI(
    title="Task API",
    description="A simple CRUD Task API built with FastAPI for the FlyRank Backend AI Engineering Internship.",
    version="1.0.0"
)

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

class TaskCreate(BaseModel):
    title:str

class TaskUpdate(BaseModel):
    title: str
    done: bool

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
    
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task

@app.put("/tasks/{id}")
def update_task(id: int, updated_task: TaskUpdate):

    if not updated_task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    for task in tasks:

        if task["id"] == id:

            task["title"] = updated_task.title
            task["done"] = updated_task.done

            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {id} not found"
    )
    

@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int):
    
    for task in tasks:
        
        if task["id"] == id:
            tasks.remove(task)
            return Response(status_code=204)
        
    raise HTTPException(
        status_code = 404,
        detail=f"Task {id} not found."
        )
    