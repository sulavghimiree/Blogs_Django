# 📝 Sulav's Blog App

Welcome to my personal **Blog App** — a dynamic and fully functional blogging platform built using **Django** and the **template engine**.

> 🔗 Live at: [blogs.sulavg.com.np](https://blogs.sulavg.com.np)

---

## 🚀 Features

- 🖋️ Create, edit, and delete blog posts
- 🔍 Blog listing with full post view
- 🧭 Navigation bar with categories and search (if implemented)
- 📆 Auto timestamps on published content
- 🎨 Styled with Django's built-in template system (HTML + CSS)
- 📱 Responsive and user-friendly design

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Django Template Engine
- **Database**: SQLite (default Django DB)
- **Deployment**: Hosted on `https://blogs.sulavg.com.np` (can be adapted to any cloud platform)

---

## 🧰 Setup Instructions

To run this project locally:

1. **Clone the repository**  
   git clone https://github.com/sulavghimiree/Blogs_Django
   cd blog-app

2. **Create a virtual environment**  
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

3. **Install the dependencies**  
   pip install -r requirements.txt

4. **Apply migrations**  
   python manage.py migrate

5. **Create a superuser (for admin access)**  
   python manage.py createsuperuser

6. **Run the development server**  
   python manage.py runserver

7. **Visit http://127.0.0.1:8000 to see the app in action!**
