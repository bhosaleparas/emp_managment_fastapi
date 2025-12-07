# Employee Management API (FastAPI)

A simple **Employee Management REST API** built using **FastAPI**.  
This project demonstrates CRUD operations (Create, Read, Update, Delete) for employee data using FastAPI, SQLAlchemy, and Pydantic.

---

## 🧰 Tech Stack

* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn
* Python 3.9+

---

## 🚀 Features

- Get all employees  
- Get a single employee by ID  
- Create a new employee  
- Update employee details  
- Delete an employee  

---

## ⚙️ Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
````

### 2. Run the FastAPI Server

```bash
uvicorn main:app --reload
```

### 3. Open API Documentation

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/employees` | Get all employees |
| GET | `/employees/{id}` | Get employee by ID |
| POST | `/employees` | Create a new employee |
| PUT | `/employees/{id}` | Update employee by ID |
| DELETE | `/employees/{id}` | Delete employee by ID |

---


## 📬 Author

**Paras Bhosale**

Feel free to contribute or open issues!

