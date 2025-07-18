# 📬 Django Contact Form Project

Welcome to the **Django Contact Form** project!  
This project allows users to submit messages via a web interface or public API. Messages are stored in the database and optionally sent to admin via email. It’s built using Django and Django REST Framework (DRF). ✨

---

## 🚀 Features

- 📝 Contact form with `name`, `email`, `subject`, and `message`
- ✅ Form validation (both MVT and API)
- 📩 Optional email sending on form submit
- 📊 Admin panel to view messages
- 🔐 Rate limiting and error handling for API
- 🧪 Unit tests (MVT + API)
- 🌍 Swagger API documentation
- 🐳 Docker support
- 🔁 CI/CD pipeline with GitHub Actions

---

## 📂 Project Structure

```
Contact Form
├─ config
│  ├─ asgi.py
│  ├─ settings
│  │  ├─ base.py
│  │  ├─ dev.py
│  │  ├─ prod.py
│  │  └─ __init__.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ core
│  ├─ admin.py
│  ├─ api
│  │  ├─ serializers.py
│  │  ├─ test_api.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ ...
│  ├─ models.py
│  ├─ templates
│  │  ├─ base.html
│  │  └─ contact
│  │     └─ contact_form.html
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ docker-compose.yml
├─ Dockerfile
├─ manage.py
├─ poetry.lock
├─ pyproject.toml
├─ pytest.ini
├─ r.md
├─ src
│  └─ project
│     └─ __init__.py
├─ static
│  ├─ css
│  │  └─ style.css
│  └─ js
└─ tests
   ├─ conftest.py
   └─ __init__.py

```

---

## 🌐 Usage

### 🔧 Setup (Poetry or pipenv)

```bash
git clone https://github.com/your-username/contact-form.git
cd contact-form
poetry install
poetry shell
````

### ⚙️ Migrate and run server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## ✉️ Form Access (HTML)

Visit:

```
http://localhost:8000/contact/
```

---

## 📡 API Access (REST)

### 📮 Submit Contact Message

```
POST /api/contact/
Content-Type: application/json
```

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "subject": "Hello!",
  "message": "This is a test message."
}
```

### ✅ Example Response (201 Created)

```json
{
  "status": "success",
  "detail": "Message successfully received."
}
```

### ❌ Example Error (400 Bad Request)

```json
{
  "status": "error",
  "errors": {
    "email": ["Enter a valid email address."]
  }
}
```

---

## 📘 API Documentation (Swagger)

After running the server, open:

```
http://localhost:8000/api/schema/swagger/
```

Powered by `drf-yasg`.

---

## 🔒 Security & Best Practices

* ✅ CSRF exempt for public API
* ✅ Throttling (rate limiting) to avoid spam
* ✅ Environment variables (`.env`) for secret management
* ✅ Structured API responses: `status`, `detail`, `errors`

---

## 🧪 Tests

Run tests:

```bash
python manage.py test
```

Includes tests for:

* ✅ Form validation
* ✅ API status codes (`201`, `400`, `429`)
* ✅ Email sending (mocked)
* ✅ Throttling behavior

---

## 🐳 Docker (Optional)

```bash
docker-compose up --build
```

App will be available at:

```
http://localhost:8000
```

---

## 🛠️ CI/CD (GitHub Actions)

`.github/workflows/django.yml` includes:

* ✅ Code format checks
* ✅ MVT & API test execution
* ✅ Dependency installation
* ✅ Test result output

---

## 🙌 Contributing

Pull requests and issues are welcome! Let's make it better together. 🚀

---

## 📄 License

MIT License

---

Made with ❤️ and Django 🐍
By [Mehman Mammadov](https://github.com/mammadov115)
