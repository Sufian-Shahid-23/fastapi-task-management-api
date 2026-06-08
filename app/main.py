from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models
from app.auth import hash_password, verify_password, create_access_token
from app.schemas import UserCreate, UserLogin
from app import models
from app.database import engine, SessionLocal
from app.schemas import TaskCreate
from app.deps import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

# create tables
models.Base.metadata.create_all(bind=engine)


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Task Manager API running"}

@app.get("/tasks")
def get_tasks(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return db.query(models.Task).filter(
        models.Task.user_id == user_id
    ).all()

@app.post("/tasks")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
    
):

    new_task = models.Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        user_id=user_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    db_user = models.User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User created successfully"}

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = db.query(models.User).filter(models.User.email == form_data.username).first()

    if not db_user:
        return {"error": "Invalid credentials"}

    if not verify_password(form_data.password, db_user.password):
        return {"error": "Invalid credentials"}

    token = create_access_token({"user_id": db_user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@app.put("/tasks/{task_id}/complete")
def complete_task(
    task_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == user_id
    ).first()

    if not task:
        return {"error": "Task not found"}

    task.completed = True

    db.commit()

    return {"message": "Task completed"}

@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == user_id
    ).first()

    if not task:
        return {"error": "Task not found"}

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}

@app.get("/stats")
def task_stats(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    tasks = db.query(models.Task).filter(
        models.Task.user_id == user_id
    ).all()

    total = len(tasks)
    completed = sum(1 for task in tasks if task.completed)

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": total - completed
    }