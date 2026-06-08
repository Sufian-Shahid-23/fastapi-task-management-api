from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="A task management API built with FastAPI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Task Manager API is running"}