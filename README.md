# 📝 Django Blog Application

A full-stack blog application built using **Django**, featuring user authentication, CRUD operations, likes, comments, search, pagination, user profiles, and deployment on **Render**.

This project was built to practice and demonstrate real-world Django backend development concepts.

---

## 🚀 Live Demo

🔗 **Live Site:**  
https://django-blog-on19.onrender.com/

---

## ✨ Features

- User authentication (Signup, Login, Logout)
- Create, Read, Update, Delete (CRUD) blog posts
- Slug-based post URLs
- Like & unlike posts
- Comment system
- User profile pages
- Search functionality
- Pagination
- Responsive UI using Bootstrap
- Deployed on Render (production environment)

---

## 🛠️ Tech Stack

- **Backend:** Django 5
- **Frontend:** HTML, Bootstrap
- **Database:** SQLite (local & production)
- **Authentication:** Django built-in auth
- **Deployment:** Render
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
blogproject/
│
├── blog/ # Main blog app
├── blogproject/ # Project settings
├── templates/ # HTML templates
├── static/ # Static files
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation (Local Setup)

```bash
git clone https://github.com/UdayRajput09/Django-Blog.git
cd Django-Blog
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## 🌍 Deployment Notes

- Environment variables are used for `SECRET_KEY` and `DEBUG`
- Database migrations are run during deployment
- Static files are handled using `collectstatic`
- Render free tier used for hosting

---

## 🎯 Learning Outcomes

- Django project structure
- URL routing & views
- Model relationships
- Authentication & authorization
- Production deployment
- Debugging production issues

---

## 📌 Author

**Uday Rajput**  
Aspiring Backend / Django Developer