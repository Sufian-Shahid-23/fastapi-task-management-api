from pydantic import BaseModel
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str = "medium"

class UserCreate(BaseModel):
    username: str
    email: str
    password: str = Field(min_length=6, max_length=72)

    
class UserLogin(BaseModel):
    email: str
    password: str

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    completed: bool

    class Config:
        from_attributes = True