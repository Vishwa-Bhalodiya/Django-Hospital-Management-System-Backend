# Django Hospital Management System (Backend)

A backend REST API built using **Django** for managing hospital operations such as **patients, doctors, and pastient-doctor mappings**, with authentication support.

---

## Features:

- User Registration & Login
- Patient Management (CURD)
- Doctor Management (CURD)
- Patient-Doctor Mapping
- Secure API access
- Clean REST-style endpoints

---

## Project Structure

```bash
Django-Hospital-Management-System-Backend/
├── accounts/ # Authentication & user accounts
├── doctors/ # Doctors app (models, views, serializers, etc.)
├── healthcare/ # Main healthcare logic (appointments, medical info)
├── mappings/ # Supporting mappings (specializations, lookups)
├── patients/ # Patients app
├── manage.py # Django CLI entrypoint
├── requirements.txt # Python dependencies
└── .gitignore
```

---

## Tech Stack

- **Backend:** Django
- **API Style:** REST
- **Authentication:** Django Auth / JWT
- **Tools:** Postman for API testing

---

## Setup Instructions

Follow these steps to run the project on your machine:

### 1. Clone the repository

```bash
git clone https://github.com/Vishwa-Bhalodiya/Django-Hospital-Management-System-Backend.git
cd Django-Hospital-Management-System-Backend
```

### 2. Create & Activate Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirement.txt
```

---

### 4. Environment Variables

Create a .env file in the project root:

```bash
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=hospital_db
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

---

### 7. Run the Server

```bash
python manage.py runserver
```

## API Endpoints

### 1. Authentication APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   |/api/auth/register/|Register a new user with name, email, and password.|
| POST   |/api/auth/login/   |Log in a user and return a JWT token.|

### 2. Doctor Management APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   |/api/doctors/|Add a new doctor (Authenticated users only.)|
| GET   |/api/doctors/|Retrieve all doctors.|
| GET   |/api/doctors/<id>|Get details of a specific doctor.|
| PUT   |/api/doctors/<id>|Update doctor details.|
| DELETE|/api/doctors/<id>|Delete a doctor records.|  

### 3. Patient APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   |/api/patients/|Add a new patient (Authenticated users only.)|
| GET   |/api/patients/|Retrieve all patients.|
| GET   |/api/patients/<id>|Get details of a specific patients.|
| PUT   |/api/patients/<id>|Update patients details.|
| DELETE|/api/patients/<id>|Delete a patients records.|

### 4. Patient-Doctor Mapping APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   |/api/mappings/|Assign a doctor to a patient. (Authenticated users only.)|
| GET   |/api/mappings/|Retrieve all patient-doctor mappings.|
| GET   |/api/mappings/<patient_id>|Get all doctors assigned to a specific patients.|
| DELETE|/api/mappings/<id>|Remove a doctor from a patient.|





