# Library Management System API

A Django REST Framework API for managing library users, books, and transactions (borrowing and returning books).

---

## Features

- User registration and JWT authentication
- Admin and member roles
- CRUD operations for users and books
- Book checkout and return
- Transaction history

---

## Setup Instructions

### 1. Clone the repository

```sh
git clone https://github.com/jackOfAllNames/library-management-system-api.git
cd library-management-system-api
```

### 2. Create and activate a virtual environment

```sh
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Apply migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for admin access)

```sh
python manage.py createsuperuser
```

### 6. Run the development server

```sh
python manage.py runserver
```

---

## Environment Variables

You can set these in a `.env` file or your shell:

- `SECRET_KEY` — Django secret key (update to yours)
- `DATABASE_URL` — Database connection string (optional, defaults to SQLite)
- `DEBUG` — Set to `False` in production

---

## API Endpoints

### User

- `POST /api/users/register/` — Register a new user
- `POST /api/users/login/` — Login (JWT token)
- `POST /api/token/` — Obtain JWT token
- `GET /api/users/` — List users (admin only)
- `GET /api/users/{id}/` — Get user details (admin only)
- `PUT /api/users/{id}/` — Update user (admin only)
- `DELETE /api/users/{id}/` — Delete user (admin only)

### Book

- `GET /api/books/` — List books
- `POST /api/books/` — Create book (admin only)
- `GET /api/books/{id}/` — Get book details
- `PUT /api/books/{id}/` — Update book (admin only)
- `DELETE /api/books/{id}/` — Delete book (admin only)

### Transaction

- `POST /api/transactions/checkout/{book_id}/` — Checkout a book
- `POST /api/transactions/return/{book_id}/` — Return a book
- `GET /api/transactions/transactions/` — List all transactions

---

## Usage Examples

### Register a User

```sh
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","username":"user1","first_name":"John","last_name":"Doe","role":"member","password":"yourpassword"}'
```

### Obtain JWT Token

```sh
curl -X POST http://localhost:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"yourpassword"}'
```

### Checkout a Book

```sh
curl -X POST http://localhost:8000/api/transactions/checkout/1/ \
  -H "Authorization: Bearer <access_token>"
```

### Return a Book

```sh
curl -X POST http://localhost:8000/api/transactions/return/1/ \
  -H "Authorization: Bearer <access_token>"
```

---

## Live URL

API is hosted on [Render](https://library-management-system-api-w7il.onrender.com/)

- Base URL: `https://library-management-system-api-w7il.onrender.com/api/`
- Render takes some time (1-30 seconds) to wake up the server when it's been idle for a while.

---
