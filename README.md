# Task Manager API

A **FastAPI-based Task Management system** with user authentication and CRUD operations.

## Features

- User registration and authentication (JWT)
- Create, update, delete, and view tasks
- Task categories and priorities
- SQLite database integration
- RESTful API design

---

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Python 3.10+

---

## Project Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
```

---

### 2. Create Virtual Environment

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Environment Variables (if applicable)

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./tasks.db
```

---

### 5. Initialize Database (if needed)

```bash
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

---

## Run the Project

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## Example API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| POST   | /auth/register | Register user     |
| POST   | /auth/login    | Login & get token |
| GET    | /tasks         | Get all tasks     |
| POST   | /tasks         | Create task       |
| PUT    | /tasks/{id}    | Update task       |
| DELETE | /tasks/{id}    | Delete task       |

---

<img width="1774" height="736" alt="requests" src="https://github.com/user-attachments/assets/83c28931-ec8e-48d2-925e-af2087ffb46f" />

## Notes

- Python 3.10+ required
- Activate virtual environment before running
- Use Swagger UI for testing
