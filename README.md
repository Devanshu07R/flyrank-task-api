# 🚀 Task API

### Containerize Your Stack (BE-04) • Backend AI Engineering Internship — FlyRank AI

A production-ready **Task Management REST API** built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Docker Compose**.

This project demonstrates how to transition from an in-memory CRUD application to a fully containerized backend powered by PostgreSQL, while preserving clean architecture through the **Repository Pattern**. It was developed as part of **Week 3 (BE-04: Containerize Your Stack)** during the **FlyRank AI Backend AI Engineering Internship**.

---

## ✨ Highlights

* ⚡ FastAPI REST API
* 🐘 PostgreSQL Database
* 🧩 SQLAlchemy ORM
* 🏗 Repository Pattern Architecture
* 🐳 Docker & Docker Compose
* 💾 Persistent Docker Volumes
* 🔐 Environment Variables (.env)
* 📚 Interactive Swagger Documentation
* ❤️ Health Check Endpoint
* 📂 Clean Modular Project Structure

---

# 🏗 System Architecture

```mermaid
graph TD

A[Client]
B[FastAPI]
C[Routes]
D[Repository Layer]
E[SQLAlchemy ORM]
F[(PostgreSQL)]
G[(Docker Volume)]

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
```

---

# 🛠 Tech Stack

| Category         | Technologies   |
| ---------------- | -------------- |
| Language         | Python 3.10+   |
| Framework        | FastAPI        |
| Database         | PostgreSQL     |
| ORM              | SQLAlchemy     |
| Validation       | Pydantic       |
| Containerization | Docker         |
| Orchestration    | Docker Compose |
| Server           | Uvicorn        |

---

# 📁 Project Structure

```text
task-api/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── repository.py
│   ├── routes.py
│   ├── schemas.py
│   └── services.py
│
├── images/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

# 🎯 Assignment Objectives

This project successfully fulfills all Week 3 (BE-04) requirements.

| Requirement                          | Status |
| ------------------------------------ | :----: |
| PostgreSQL running in Docker         |    ✅   |
| Docker Volume for persistent storage |    ✅   |
| Docker Compose configuration         |    ✅   |
| SQLAlchemy integration               |    ✅   |
| Repository Pattern implementation    |    ✅   |
| Environment variables using `.env`   |    ✅   |
| `.env.example` included              |    ✅   |
| CRUD API with PostgreSQL             |    ✅   |
| Swagger documentation                |    ✅   |
| Persistence verified after restart   |    ✅   |

---

# ⚙️ Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Devanshu07R/flyrank-task-api.git

cd task-api
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/taskdb
```

---

## 5. Start PostgreSQL

```bash
docker compose up -d
```

Verify the running container:

```bash
docker ps
```

---

## 6. Run the API

```bash
uvicorn app.main:app --reload
```

Application

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📡 API Endpoints

| Method | Endpoint      | Description              |
| ------ | ------------- | ------------------------ |
| GET    | `/`           | API Information          |
| GET    | `/health`     | Health Check             |
| GET    | `/tasks`      | Retrieve all tasks       |
| GET    | `/tasks/{id}` | Retrieve a specific task |
| POST   | `/tasks`      | Create a new task        |
| PUT    | `/tasks/{id}` | Update an existing task  |
| DELETE | `/tasks/{id}` | Delete a task            |

---

# 💾 Persistence Verification

Database persistence was verified using a Docker Volume.

### Verification Steps

1. Launch PostgreSQL with Docker Compose.
2. Start the FastAPI application.
3. Create multiple tasks through Swagger UI.
4. Stop the FastAPI server.
5. Stop the PostgreSQL container.
6. Restart both services.
7. Retrieve all tasks.

The previously created records remained available after restarting both the application and the PostgreSQL container, confirming successful persistent storage.

---

# 📸 Screenshots

## 📚 Swagger UI

![Swagger UI](images/swagger-ui.png)

---

## 🐳 Docker Compose Running

![Docker Container](images/docker-container.png)

---

## ✅ CRUD Operations

![CRUD Demo](images/crud-demo.png)

---

## 💾 PostgreSQL Persistence

![PostgreSQL Persistence](images/postgres-persistence.png)

# 🚀 Project Progress

| Week   | Topic                            | Status |
| ------ | -------------------------------- | :----: |
| Week 2 | RESTful CRUD API                 |    ✅   |
| Week 3 | PostgreSQL + Docker + SQLAlchemy |    ✅   |
| Week 4 | Redis Integration                |   🔜   |

---

# 📈 Future Enhancements

* JWT Authentication
* User Management
* Alembic Database Migrations
* Redis Caching
* Background Tasks
* Unit & Integration Testing
* CI/CD with GitHub Actions
* Kubernetes Deployment

---

# 👨‍💻 Author

**Devanshu Dasgupta**

Backend AI Engineering Intern — FlyRank AI

- **GitHub:** [Devanshu07R](https://github.com/Devanshu07R)
- **LinkedIn:** [Devanshu Dasgupta](https://www.linkedin.com/in/devanshudasgupta/)

---

## ⭐ Support

If you found this project useful, consider giving the repository a **Star**.

Feedback and contributions are always welcome.
