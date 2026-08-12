# Project 2: Backend API Development

## 🎯 Goal
Develop a simple backend API to handle application logic.

A clean and beginner-friendly REST API built with **FastAPI** and **Pydantic**. This project demonstrates the fundamentals of backend API development, including GET and POST endpoints, request-body validation, Pydantic models, and in-memory data handling.

---

## ✅ Requirements Mapping

This section maps each assignment requirement directly to where it is implemented in the project.

| Key Requirement | Status | Implementation |
|---|---|---|
| Create API endpoints (GET / POST) | ✅ Done | `GET /`, `GET /users`, `POST /users` in `main.py` |
| Handle user input and responses | ✅ Done | `POST /users` accepts a JSON request body (`User` model) and returns a structured JSON response |
| Validate basic data | ✅ Done | `models.py` — Pydantic validation on `name` (min 2 characters), `age` (must be greater than 0), and `email` (valid email format) |

**Key Skills demonstrated:** Backend development, server-side logic, API concepts.

---

## 📌 Project Overview

This project is a simple **User Management API** developed using FastAPI. The main purpose of this project is to demonstrate how a backend API can:

- Create users
- Retrieve all users
- Validate incoming user data
- Handle request bodies using Pydantic
- Organize API routes
- Store data temporarily in memory

The project uses an in-memory Python list instead of a database, making it lightweight and easy to understand while learning the fundamentals of FastAPI.

---

## 🚀 Features

- ✅ FastAPI-based backend
- ✅ REST API endpoints
- ✅ GET endpoint for the home route
- ✅ GET endpoint for retrieving users
- ✅ POST endpoint for creating users
- ✅ Pydantic request validation
- ✅ Basic field validation
- ✅ In-memory user storage
- ✅ Automatic interactive API documentation (`/docs`)
- ✅ CORS enabled — accessible from any device / network / frontend origin
- ✅ Clean and minimal project structure
- ✅ Deployed live on Vercel

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming language |
| FastAPI | Web framework for building APIs |
| Pydantic | Data validation and request models |
| Uvicorn | ASGI server for running the application |
| Vercel | Serverless hosting/deployment platform |

---

## 📁 Project Structure

```
Backened API Development/
│
├── main.py            # FastAPI app, routes, CORS config
├── models.py           # Pydantic User model with validation
├── api/
│   └── index.py         # Vercel serverless entrypoint
├── vercel.json           # Vercel deployment config
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ▶️ Running Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open:
- `http://127.0.0.1:8000/` — health check
- `http://127.0.0.1:8000/docs` — interactive Swagger documentation

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check — confirms the API is running |
| GET | `/users` | Returns the list of all users |
| POST | `/users` | Creates a new user (requires `name`, `age`, `email` in request body) |

**Example request body for `POST /users`:**
```json
{
  "name": "Ali",
  "age": 22,
  "email": "ali@example.com"
}
```

---

## ⚠️ Note on Data Storage

User data is stored in an in-memory Python list (`users = []`), which is intentional for this learning project. On serverless platforms like Vercel, this data does **not persist** across requests/deployments — for permanent storage, a database (e.g. MongoDB Atlas or PostgreSQL/Supabase) would be required.
