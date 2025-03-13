MLOps Task 2
============

This project is an MLOps pipeline featuring a FastAPI backend, PostgreSQL database, and a Streamlit frontend.
It is containerized using Docker and orchestrated with Docker Compose.

Project Structure
-----------------
mlops-task-2/

│── backend/              # FastAPI backend

│   ├── main.py          # FastAPI entry point

│   ├── database.py      # SQLAlchemy database connection

│   ├── models.py        # Database models

│   ├── routes.py        # API routes

│   ├── requirements.txt # Backend dependencies

│── frontend/             # Streamlit frontend

│   ├── src/             # Streamlit application

│   ├── app.py           # Streamlit entry point

│── docker-compose.yml    # Docker Compose configuration

│── Dockerfile            # Docker build file

│── README.md             # Project documentation

Technologies Used
-----------------
- FastAPI - Backend API
- PostgreSQL - Database
- Streamlit - Frontend
- SQLAlchemy - ORM for database interaction
- Docker & Docker Compose - Containerization
- GitHub Actions (for CI/CD in future updates)

Setup and Installation
----------------------
1. Clone the Repository
   git clone https://github.com/hammad-sarfraz-1/mlops-task-2.git
   

2. Set Up Environment Variables
   Update database.py and docker-compose.yml if needed to match your credentials.

3. Build and Run with Docker Compose
   docker-compose up --build

   This will start:
   - PostgreSQL database (db)
   - FastAPI backend (backend)
   - Streamlit frontend (frontend)

4. Access the Application
   - Backend API: http://localhost:8000/docs
   - Frontend: http://localhost:8501

Database Setup
--------------
Your FastAPI app is connected to PostgreSQL using SQLAlchemy.
To manually access the database:

   docker exec -it postgres_db psql -U admin -d mydatabase

View existing tables:
   \dt

Check data inside a table (e.g., users):
   SELECT * FROM users;

Endpoints (FastAPI)
-------------------
The backend provides REST API endpoints. Access the Swagger UI at:
   http://localhost:8000/docs

Example:
- GET /users/ - Get all users
- POST /users/ - Add a new user

Troubleshooting
---------------
1. Database Connection Error
   Check docker-compose.yml and database.py to ensure:
   - POSTGRES_USER, POSTGRES_PASSWORD, and POSTGRES_DB match.

   Restart the services:
   docker-compose down
   docker-compose up --build

2. Checking Logs
   To debug, check the logs for each service:
   docker logs fastapi_backend
   docker logs streamlit_frontend
   docker logs postgres_db

