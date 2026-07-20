from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    done: bool = False


class TaskUpdate(BaseModel):
    title: str
    done: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    done: bool

    model_config = {
        "from_attributes": True
    }