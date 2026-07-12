# 🏥 Patient Management API

A RESTful Patient Management API built with **FastAPI** and **SQLModel**. The project provides secure CRUD operations for managing patient records, JWT-based authentication, PostgreSQL database support, and Dockerized deployment using Docker Compose.

---

## 🚀 Features

- FastAPI REST API
- JWT Authentication
- CRUD Operations for Patients
- SQLModel ORM
- PostgreSQL Database
- Docker & Docker Compose Support
- Environment Variable Configuration
- Interactive Swagger Documentation
- Persistent Database Storage using Docker Volumes

---

## 🛠️ Tech Stack

- Python 3.13
- FastAPI
- SQLModel
- PostgreSQL
- Docker
- Docker Compose
- Pydantic Settings
- Uvicorn

---

## 📁 Project Structure

```text
task4/
│
├── app/
│   ├── auth.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routers/
│   └── ...
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .env.example
└── README.md
```

---

# ⚙️ Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql+psycopg://patient:secret@db:5432/patients
```

---

# 🐳 Running with Docker

## Build and start the application

```bash
docker compose up --build
```

---

## Open Swagger Documentation

After the containers start successfully, open:

```
http://localhost:8000/docs
```

---

## Check running containers

```bash
docker compose ps
```

---

## View API logs

```bash
docker compose logs api
```

---

## Stop the application

```bash
docker compose down
```

---

## Start the application again

```bash
docker compose up
```

The PostgreSQL database data is stored in a **named Docker volume**, so your data will remain available even after stopping the containers.

---

# 🗄️ Services

The project runs three Docker containers:

| Service | Purpose |
|----------|----------|
| API | FastAPI application |
| PostgreSQL | Stores patient records |
| Redis | Ready for caching and future enhancements |

---

# 📖 API Documentation

Swagger UI

```
http://localhost:8000/docs
```

OpenAPI JSON

```
http://localhost:8000/openapi.json
```

---

# 🔐 Authentication

Protected endpoints require a valid JWT access token.

Authentication is handled using:

- JWT Tokens
- Bearer Authentication
- FastAPI Security Dependencies

---

# 📦 Docker Components

This project includes:

- Dockerfile
- Docker Compose
- PostgreSQL
- Redis
- Named Volume
- Environment Variables
- Health Checks
- Multi-container Configuration

--