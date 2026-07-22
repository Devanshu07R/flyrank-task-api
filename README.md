# 🚀 Task API (W2 · A1 — Build your first CRUD API)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688)
![Status](https://img.shields.io/badge/Project-Completed-success)
![Backend](https://img.shields.io/badge/Backend-REST_API-orange)

A **RESTful CRUD API** built with **FastAPI** as part of the **FlyRank AI Backend AI Engineering Internship**.

This project demonstrates the fundamentals of backend development by implementing CRUD operations, request validation, proper HTTP status codes, exception handling, and interactive API documentation using **Swagger UI (OpenAPI)**.

---

# 📌 Features

* ✅ RESTful CRUD API
* ✅ Create, Read, Update & Delete Tasks
* ✅ Request Validation with Pydantic
* ✅ Proper HTTP Status Codes
* ✅ Exception Handling
* ✅ Interactive Swagger UI Documentation
* ✅ In-Memory Data Storage
* ✅ Clean & Beginner-Friendly Code

---

# 🛠️ Tech Stack

* **Python 3.10+**
* **FastAPI**
* **Pydantic**
* **Uvicorn**
* **Swagger UI (OpenAPI)**

---

# 📂 Project Structure

```text
task-api/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── images/
    └── swagger-ui.png
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Devanshu07R/flyrank-task-api.git
```

## 2. Navigate to the Project

```bash
cd flyrank-task-api
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the Server

```bash
uvicorn main:app --reload
```

The API will start at:

```text
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🏗️ Project Architecture

```text
                Client
                   │
                   ▼
            FastAPI Server
                   │
         ┌─────────┴─────────┐
         │                   │
         ▼                   ▼
   CRUD Endpoints      Pydantic Validation
                   │
                   ▼
          In-Memory Task List
```

---

# 📌 API Endpoints

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| GET    | `/`           | API Information         |
| GET    | `/health`     | Health Check            |
| GET    | `/tasks`      | Retrieve All Tasks      |
| GET    | `/tasks/{id}` | Retrieve Task by ID     |
| POST   | `/tasks`      | Create a New Task       |
| PUT    | `/tasks/{id}` | Update an Existing Task |
| DELETE | `/tasks/{id}` | Delete a Task           |

---

# 📥 Example Request

### Create a Task

**POST** `/tasks`

Request Body

```json
{
    "title": "Learn FastAPI"
}
```

Response

```json
{
    "id": 4,
    "title": "Learn FastAPI",
    "done": false
}
```

---

# 📤 Example Response

### Get All Tasks

**GET** `/tasks`

```json
[
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": false
    },
    {
        "id": 2,
        "title": "Complete FlyRank Assignment",
        "done": false
    },
    {
        "id": 3,
        "title": "Push Project to GitHub",
        "done": true
    }
]
```

---

## 📸 Swagger UI

The API includes interactive documentation powered by FastAPI's built-in Swagger UI.

![Swagger UI](images/swagger-ui.png)

---

# 📚 What I Learned

Through this project, I gained hands-on experience with:

* Designing RESTful APIs
* CRUD Operations
* FastAPI Routing
* Request Validation using Pydantic
* Exception Handling
* HTTP Status Codes
* Interactive API Documentation
* Git & GitHub Workflow
* Backend Development Fundamentals

---

# 🚀 Future Improvements

* Connect with a SQL Database
* User Authentication (JWT)
* Search & Filtering
* Pagination
* Docker Support
* Unit Testing with Pytest
* Deploy using Render or Railway

---

# 👨‍💻 Author

**Devanshu Dasgupta**

**Backend AI Engineering Intern @ FlyRank AI**

* GitHub: https://github.com/Devanshu07R
* LinkedIn: https://www.linkedin.com/in/devanshudasgupta

---

## ⭐ If you found this project helpful, consider giving it a star!
