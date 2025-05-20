## 🚀 Planetarium API

A Django REST API for managing a planetarium system.

---

## 📦 Getting Started

These instructions will help you run the project locally using Docker.

---

### 🔧 Prerequisites

Install:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

### 📥 Clone the Repository

```bash
git clone https://github.com/your-username/planetarium.git
cd planetarium
```

---

### ⚙️ Configure Environment Variables

Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=django-insecure-$t1bahlmj95k2pdkq0177648!sdex)a_d-zb61(uspt7*7fu(8)

DB_NAME=planetarium_db
DB_USER=planetarium_user
DB_PASSWORD=planetarium_pass
DB_HOST=db
DB_PORT=5432

ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
```

---

### 🐳 Run with Docker

Build and run the containers:

```bash
docker compose up --build
```

This will start:
- Django backend (`web`)
- PostgreSQL database (`db`)

The app will be available at:  
👉 `http://localhost:8000/`

---

### 🛠 Apply Migrations

In a separate terminal:

```bash
docker compose exec web python manage.py migrate
```

Create a superuser (optional):

```bash
docker compose exec web python manage.py createsuperuser
```

---

### 🧪 Run Tests

```bash
docker compose exec web python manage.py test
```

---

### 📂 Media & Static Files (optional)

```bash
docker compose exec web python manage.py collectstatic --noinput
```

---

## 📋 API Base URL

```
http://localhost:8000/
```