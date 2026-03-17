# 🏥 HealthCare Management System with Insurance Premium Prediction API


A **machine learning-powered healthcare application** that predicts the **insurance premium category** based on patient attributes such as demographics and health indicators.

The system follows a **microservices architecture** where each component runs as an independent container, enabling **scalable and modular deployment**.

---

# 🚀 Project Overview

This project consists of **three independent services**:

| Service | Description |
|------|-------------|
| Frontend | Streamlit UI for user interaction |
| Prediction API | ML model service for premium prediction |
| Backend API | Handles patient data and system logic |

All services are containerized using Docker and orchestrated with Docker Compose, enabling seamless deployment locally or in the cloud.

---

# 🧠 System Architecture

```

User Browser
│
▼
Streamlit Frontend (Port 8501)
│
▼
Prediction API (Port 8001)
│
▼
Backend API (Port 8000)

```

Each component runs in its **own container**, making the system modular and scalable.

---

# 📂 Project Structure

```

HealthCare Management System with Insurance Premium Prediction API
│
├── frontend
│   ├── frontend.py
│   └── requirements.txt
│
├── prediction
│   ├── app.py
│   ├── config
│   ├── model
│   ├── schema
│   └── requirements.txt
│
├── backend
│   ├── main.py
│   ├── config
│   ├── model
│   ├── schema
│   ├── patients.json
│   └── requirements.txt
│
└── docker-compose.yml

````

---

# 🛠️ Tech Stack

### Programming
- Python

### Machine Learning
- Scikit-learn  
- Pandas  
- NumPy  

### Backend
- FastAPI

### Frontend
- Streamlit

### Containerization
- Docker  
- Docker Compose  

### Deployment
- AWS EC2  

### Container Registry
- Docker Hub  

---

# ✨ Features

✔ Predict insurance premium category  
✔ Microservices-based architecture  
✔ Dockerized deployment  
✔ RESTful APIs using FastAPI  
✔ Streamlit interactive UI  
✔ Cloud deployment ready  

---

# 💻 Running the Project Locally

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/healthcare-insurance-ml-system.git
cd healthcare-insurance-ml-system
````

---

## 2️⃣ Build Docker Images

```bash
docker build -t healthcare_backend ./backend
docker build -t healthcare_prediction ./prediction
docker build -t healthcare_frontend ./frontend
```

---

## 3️⃣ Start Services with Docker Compose

```bash
docker-compose up
```

This will start all services automatically.

---

# 🌐 Access the Application

| Service             | URL                        |
| ------------------- | -------------------------- |
| Frontend            | http://localhost:8501      |
| Backend API Docs    | http://localhost:8000/docs |
| Prediction API Docs | http://localhost:8001/docs |

---

# 🐳 Docker Deployment Workflow

Each service is packaged as a Docker container.

The containers are pushed to Docker Hub and later pulled during deployment.

## Build Images

```bash
docker build -t username/healthcare_backend ./backend
docker build -t username/healthcare_prediction ./prediction
docker build -t username/healthcare_frontend ./frontend
```

## Push Images

```bash
docker push username/healthcare_backend
docker push username/healthcare_prediction
docker push username/healthcare_frontend
```

---

# ☁️ Deployment on AWS EC2

The application is deployed on AWS EC2 using Docker Compose.

---

## Step 1 — Launch EC2 Instance

Create an Ubuntu instance and allow these inbound ports:

| Port | Purpose            |
| ---- | ------------------ |
| 22   | SSH access         |
| 8000 | Backend API        |
| 8001 | Prediction API     |
| 8501 | Streamlit Frontend |

---

## Step 2 — Install Docker

```bash
sudo apt update
sudo apt install docker.io
```

Start Docker:

```bash
sudo systemctl start docker
```

---

## Step 3 — Upload Project Files

Transfer project files to EC2 using SCP:

```bash
scp -i key.pem -r project-folder ubuntu@EC2-IP:~
```

---

## Step 4 — Start the Application

Navigate to the project directory and run:

```bash
docker-compose up -d
```

Docker will automatically pull images from Docker Hub and start the containers.

---

# 🔗 Access the Deployed Application

| Service        | URL                            |
| -------------- | ------------------------------ |
| Frontend       | http://EC2_PUBLIC_IP:8501      |
| Backend API    | http://EC2_PUBLIC_IP:8000/docs |
| Prediction API | http://EC2_PUBLIC_IP:8001/docs |

---

# 📈 Future Improvements

* CI/CD pipeline with GitHub Actions
* MLflow model tracking
* Kubernetes deployment
* Nginx reverse proxy
* HTTPS with custom domain

---

# 👨‍💻 Author

**Arunabha Pani**

Machine Learning | Data Science | MLOps

---

⭐ If you found this project useful, consider giving it a **star on GitHub**.

```
```
