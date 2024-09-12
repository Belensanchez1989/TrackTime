
### **Backend README (Track-Time)**

# Track-Time (Backend)

The backend of the **Track-Time** app provides an API for managing user bookings. Built using **Python**, **Django**, and **PostgreSQL**,
this project handles user data, service bookings, and schedules.

## Features

- REST API for creating and managing music studio reservations.
- Stores user information, selected services, dates, and times.
- Uses Django ORM with PostgreSQL for database management.

## Technologies

- **Python**: Programming language for server-side logic.
- **Django**: Web framework for the backend API.
- **PostgreSQL**: Relational database system.

## Getting Started

### Prerequisites

Before starting, make sure you have **Python 3.x**, **pip**, and **PostgreSQL** installed.

- [Download Python](https://www.python.org/)
- [Install PostgreSQL](https://www.postgresql.org/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Belensanchez1989/TrackTime.git

2. Create a virtual environment and activate it:

3. Install dependencies:
python3 -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

pip install -r requirements.txt

## Set up the PostgreSQL database:

Create a PostgreSQL database and user.

Run migrations and start the server:

python manage.py migrate
python manage.py runserver

bash
Copiar código
python manage.py migrate
python manage.py runserver
Access the API at http://localhost:8000/api/.

## Dependencies
- Django: ^4.0
- djangorestframework: ^3.13
- psycopg2: ^2.9 (PostgreSQL adapter)
- django-cors-headers: ^3.11


Known Issues
No testing implemented.
Potential performance issues with large datasets.

