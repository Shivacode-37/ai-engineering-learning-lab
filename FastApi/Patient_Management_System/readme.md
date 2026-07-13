# 🏥 Patient Management System API

A simple REST API built using **FastAPI** and **Pydantic** to understand the fundamentals of backend API development. This project demonstrates how HTTP methods work, how data validation is handled using Pydantic, and how client-server communication happens in a RESTful application.

---

## 🚀 Project Overview

This project is a basic Patient Management System where users can perform CRUD operations on patient records through REST API endpoints.

The main objective of this project was to learn:

- FastAPI fundamentals
- REST API development
- HTTP methods
- Request and Response lifecycle
- Pydantic data validation
- API documentation using Swagger UI
- JSON data handling

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON (for data storage)

---

## 📌 Features

- Create a new patient
- Get all patient records
- Get a specific patient
- Update patient information
- Delete a patient
- Automatic request validation using Pydantic
- Response serialization
- Interactive API documentation

---

## 📂 API Endpoints

| Method    | Endpoint           | Description            |
| --------- | ------------------ | ---------------------- |
| GET       | `/patients`      | Get all patients       |
| GET       | `/patients/{id}` | Get patient by ID      |
| POST      | `/create`        | Create a new patient   |
| PUT/PATCH | `/update/{id}`   | Update patient details |
| DELETE    | `/delete/{id}`   | Delete a patient       |

> *(Update the endpoint names if they are different in your project.)*

---

## 📋 Patient Model

The API validates patient information using **Pydantic**.

Example fields:

- Patient ID
- Name
- Age
- Gender
- Height
- Weight

The project also demonstrates:

- Field validation
- Type validation
- Required and optional fields
- Custom validators
- Model validators

---

## 📖 What I Learned

While building this project, I learned:

- Building REST APIs using FastAPI
- Difference between GET, POST, PUT, PATCH and DELETE
- Client → Server request flow
- Request body validation
- Path parameters
- Query parameters
- Pydantic models
- Field Validators
- Model Validators
- Response Models
- JSON serialization
- Error handling using HTTPException
- HTTP Status Codes
- Organizing API endpoints

---

## 📷 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## ▶️ Running the Project

### Clone the repository

```bash
git clone https://github.com/your-username/patient-management-system.git
```

### Navigate into the project

```bash
cd patient-management-system
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
uvicorn main:app --reload
```

---

## 📁 Project Structure

```
Patient-Management-System/
│
├── main.py
├── patient.py
├── database.json
├── requirements.txt
├── README.md
└── .gitignore
```

*(Modify the structure according to your project.)*

---

## 🎯 Future Improvements

- Database integration (SQLite/PostgreSQL)
- User authentication
- JWT authorization
- Search and filtering
- Pagination
- Docker support
- Unit testing
- Logging
- Deployment

---

## 📚 Purpose

This project was built as part of my backend and AI engineering learning journey to strengthen my understanding of FastAPI, Pydantic, and REST API development before moving on to larger AI-powered applications.

---

## ⭐ If you found this project useful, feel free to star the repository!
