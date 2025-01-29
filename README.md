# Public API - HNG12 Backend Stage 0 Task

## 📌 Project Description
This is a simple public API built for the **HNG12 Backend Stage 0 Task**. It provides basic information in JSON format, including:
- My registered email address (used in HNG12 Slack workspace)
- The current date and time (ISO 8601 format, UTC)
- The GitHub URL of this project's codebase

This API is built using **FastAPI (Python)** and deployed to a publicly accessible endpoint.

---

## 🚀 Setup Instructions

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the API Locally**
```sh
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Your API will be accessible at:
```
http://127.0.0.1:8000
```

---

## 🌍 Deployed API URL
🔗 **Live API Endpoint:**  
`https://hng12-backend-stage-0.onrender.com/`

---

## 📖 API Documentation

### **📌 Endpoint:**
```
GET /
```

### **📌 Sample Response (200 OK)**
```json
{
  "email": "easykelchimdikejohn@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/cdJohnEl/HNG12_Backend_Stage_0.git"
}
```

### **📌 Example Usage**
#### **Using `curl`**
```sh
curl -X GET https://hng12-backend-stage-0.onrender.com/
```
#### **Using Python**
```python
import requests
response = requests.get("https://hng12-backend-stage-0.onrender.com/")
print(response.json())
```

---

## 🔗 Useful Links
- [Hire Python Developers](https://hng.tech/hire/python-developers)
- [Hire C# Developers](https://hng.tech/hire/csharp-developers)
- [Hire Golang Developers](https://hng.tech/hire/golang-developers)
- [Hire PHP Developers](https://hng.tech/hire/php-developers)
- [Hire Java Developers](https://hng.tech/hire/java-developers)
- [Hire Node.js Developers](https://hng.tech/hire/nodejs-developers)

---

## 📜 License
This project is open-source and free to use.

## 👨‍💻 Author
- **John Chimdike Ezekiel**
- GitHub: [cdJohnEL](hhttps://github.com/cdJohnEl)
- Email: easykelchimdikejohn@gmail.com

