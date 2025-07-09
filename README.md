# Secured Fullstack Auth App
# 🔐 SecureAuth — Encrypted User Authentication System

SecureAuth is a **full-stack web application** designed to provide **robust and secure user authentication** using **Angular** (frontend), **Django & PostgreSQL** (backend), and **Blowfish encryption** for password protection.

## 🚀 Features

- 🌐 **Angular 19 frontend** with a modern and responsive UI
- 🐍 **Django 5.1.7 REST API** backend with PostgreSQL integration
- 🔒 **Blowfish algorithm** used to encrypt user passwords before storing in the database
- ✅ Custom user registration and login system
- 🚨 **Suspicious login tracking**:
  - If a user fails to log in more than twice (wrong email or password), their **email and attempted password** are recorded.
  - These entries are marked as **"suspected fraud"** and monitored by a backend admin.
- 🛡️ Admin dashboard to monitor suspicious login attempts

## 🏗️ Tech Stack

| Layer       | Technology         |
|-------------|--------------------|
| Frontend    | Angular 19         |
| Backend     | Django 5.1.7       |
| Database    | PostgreSQL         |
| Encryption  | Blowfish Algorithm |

backend-1/
├── .gitignore
├── Dockerfile              
├── docker-compose.yml      
├── render.yaml             
├── Procfile                
├── requirements.txt
├── .env.example            
├── manage.py
├── backend/                
└── app/                    

 Author
Stephen Ekeh
LinkedIn:www.linkedin.com/in/stephen-ekeh-0b7897127
stevenadibee@yahoo.com.com