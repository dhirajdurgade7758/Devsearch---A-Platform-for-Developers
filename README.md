# Devsearch  
*A Platform for Developers to Showcase Their Profiles and Projects*

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-yellow.svg)](CONTRIBUTING.md)

## 🌟 Project Description  
Devsearch is a platform for developers to showcase their profiles and projects, connect with others, and foster collaboration.  
This full-stack Django application includes features like messaging, project ratings, comments, search, and much more.  

## 🌐 Live Demo  
Check out the live application: [Devsearch](https://devsearch-ubps.onrender.com/)  

## ✨ Features  
- User Authentication (Login, Registration)  
- Profile Creation and Management  
- Project Rating and Commenting  
- Messaging Between Users  
- Search and Pagination  
- REST API Integration  
- Email Notifications  
- Responsive Design  
- Hosted on Render

## 🛠️ Tech Stack  
- **Frontend**: HTML, CSS, JavaScript, Bootstrap  
- **Backend**: Python, Django  
- **Database**: SQLite  
- **API**: Django REST Framework (DRF)  
- **Hosting**: [Hosting Platform]  

## ⚙️ Installation  

### Clone the Repository  
```bash
git clone https://github.com/dhirajdurgade7758/Devsearch---A-Platform-for-Developers
cd devsearch
```

### Install Dependencies  
```bash
pip install -r requirements.txt
```

### Run Migrations  
```bash
python manage.py makemigrations  
python manage.py migrate  
```

### Start the Server  
```bash
python manage.py runserver
```

### Access the Application  
Open your browser and go to `http://127.0.0.1:8000/`.  

## 🔗 REST API  
The application includes a fully functional REST API for data integration.  

### Base URL  
`http://127.0.0.1:8000/api/`  

### Endpoints  
- `/projects/` - Get all projects  
- `/projects/<id>/` - Get a single project by ID  
- `/users/` - Get all users  
- `/users/<id>/` - Get a single user by ID  

## 🖼️ Screenshots  
### Home Page  
![Home Page](screenshots/home%20page.png)  

### Projects Page
![Projects Page](screenshots/projects%20page.png) 

### User Profile  
![User Profile](screenshots/profile%20page.png)  

### User Project  
![User Project](screenshots/project%20page.png)  

### Account Page  
![Account Page ](screenshots/account%20page.png)  

## 📜 License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

## 🤝 Contributing  
Contributions are welcome!  
- Fork the repository  
- Create a new branch  
- Make your changes  
- Submit a pull request  

## 🙏 Acknowledgments  
Special thanks to [Dennis Ivy](https://www.udemy.com/course/python-django-2021-complete-course/?couponCode=NEWYEARCAREER) for the amazing Django course that inspired this project.
