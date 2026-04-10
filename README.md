# 🌤️ Skies — Weather App (Django)

A simple and modern weather web application built with Django that allows users to check real-time weather information using a city name or their current location.

---

## 🚀 Features

* 🔍 Search weather by city name
* 📍 Get weather using current location (latitude & longitude)
* 🌡️ Displays:

  * Temperature
  * Humidity
  * Weather condition
* 🕘 Stores recent searches (last 5 cities)
* 🎨 Clean and responsive UI
* 🔗 API support using Django REST Framework (DRF)

---

## 🛠️ Tech Stack

* **Backend:** Django (Python), Django REST Framework
* **Frontend:** HTML, CSS
* **API:** OpenWeatherMap API
* **Database:** SQLite

---

## 📋 Requirements

Make sure you have:

* Python 3.8 or higher
* pip (Python package manager)

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash id="o4r9h0"
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash id="0a3mxy"
python -m venv venv
```

Activate it:

* **Windows**

```bash id="f4t2xq"
venv\Scripts\activate
```

* **Mac/Linux**

```bash id="cql21k"
source venv/bin/activate
```

---

### 3️⃣ Install Required Packages

```bash id="5qyjkm"
pip install django djangorestframework requests python-dotenv
```

---

### 4️⃣ Add DRF to Installed Apps

In `settings.py`:

```python id="swh9m6"
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

---

### 5️⃣ Setup API Key 🔐

Create a `.env` file in the root directory:

```env id="7hl9lx"
WEATHER_API_KEY=your_openweathermap_api_key
```

Get your API key from:
https://openweathermap.org/api

---

### 6️⃣ Update `views.py`

```python id="dbdylj"
import os

API_KEY = os.getenv("WEATHER_API_KEY")
```

---

### 7️⃣ Apply Migrations

```bash id="c48bjx"
python manage.py makemigrations
python manage.py migrate
```

---

### 8️⃣ Run the Server

```bash id="d0p0qn"
python manage.py runserver
```

Open in browser:

```id="9x6mti"
http://127.0.0.1:8000/
```

---

## 📁 Project Structure

```id="rjpnvi"
weather-app/
│
├── main/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── weather/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── .env
```

---

## ⚙️ How It Works

1. User enters a city name or allows location access
2. Django sends a request to OpenWeatherMap API
3. API returns weather data
4. Data is displayed on UI or API response
5. Recent searches are stored in database

---

## 🔐 Security Notes

* Store API keys in `.env` file
* Do not upload `.env` to GitHub

Add this to `.gitignore`:

```id="sbm6ah"
.env
```

---

## 🧪 Running Tests

```bash id="y64a9h"
python manage.py test
```

---

## 🚀 Deployment Notes

* Set environment variables on your hosting platform
* Use PostgreSQL in production
* Enable HTTPS

---

## 📜 License

This project is open-source and free to use.

---

## 👨‍💻 Author

Developed by **Manav D**
