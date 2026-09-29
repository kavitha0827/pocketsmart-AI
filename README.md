# 🤖 PocketSmart AI

### AI-Powered Budget & Recommendation Assistant

PocketSmart AI is an AI-powered budget and recommendation assistant built with **Python, FastAPI, Google Gemini AI, HTML, CSS, JavaScript, SQLite, and SQLAlchemy**.

It helps users make smarter decisions based on their budget through AI-powered recommendations and specialized planning tools.

---

## ✨ Features

* 🔐 **User Authentication**

  * User registration
  * User login
  * Authentication management

* 💰 **AI-Powered Recommendations**

  * Generate personalized recommendations based on user requirements and budget
  * Uses Google Gemini AI for intelligent responses

* 🏠 **Home Planner**

  * Plan home-related purchases and requirements within a specified budget

* 🎉 **Party Planner**

  * Get recommendations for party planning based on budget and requirements

* 💎 **Jewelry Planner**

  * Explore jewelry recommendations according to budget and preferences

* 📜 **Recommendation History**

  * Store and retrieve previous recommendations

* 📱 **Responsive Web Interface**

  * Clean HTML/CSS interface
  * JavaScript-based frontend interactions

* 🗄️ **Database Support**

  * SQLite database
  * SQLAlchemy ORM

---

## 🛠️ Technologies Used

| Technology          | Purpose                           |
| ------------------- | --------------------------------- |
| 🐍 Python           | Backend programming               |
| ⚡ FastAPI           | Web framework and API development |
| 🤖 Google Gemini AI | AI-powered recommendations        |
| 🌐 HTML             | Web page structure                |
| 🎨 CSS              | User interface styling            |
| ⚙️ JavaScript       | Frontend interactions             |
| 🗄️ SQLite          | Database                          |
| 🔗 SQLAlchemy       | Database ORM                      |
| 🧪 Pytest           | Testing                           |

---

## 📁 Project Structure

```text
PocketSmart_AI/
│
├── App/
│   ├── __init__.py
│   ├── auth.py
│   ├── config.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── recommandation.py
│   ├── schemas.py
│   │
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       ├── pages.py
│       └── recommendations.py
│
├── services/
│   ├── __init__.py
│   ├── catalog.py
│   ├── gemini_service.py
│   └── prompts.py
│
├── static/
│   ├── css/
│   │   ├── prompt
│   │   └── style.css
│   └── js/
│       └── app.js
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── home_planner.html
│   ├── index.html
│   ├── jewelry_planner.html
│   ├── login.html
│   ├── party_planner.html
│   ├── register.html
│   └── ...
│
├── tests/
│   ├── __init__.py
│   └── test_app.py
│
├── env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/kavitha0827/pocketsmart-AI.git
```

### 2. Navigate to the project

```bash
cd pocketsmart-AI
```

### 3. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

Install the required Python packages used by the project:

```powershell
pip install fastapi uvicorn google-genai python-multipart jinja2 sqlalchemy python-dotenv pytest
```

---

## 🔑 Environment Configuration

PocketSmart AI uses environment variables for private configuration such as the Gemini API key.

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

**Never upload your real `.env` file or API key to GitHub.**

The project uses `.gitignore` to prevent `.env` from being committed.

You can use `env.example` as a template for the required environment variables.

---

## ▶️ Running the Application

Start the FastAPI server with:

```powershell
python -m uvicorn App.main:app --host 127.0.0.1 --port 8001
```

Then open your browser and visit:

```text
http://127.0.0.1:8001/
```

---

## 🧪 Running Tests

Run the test suite with:

```powershell
pytest
```

---

## 🔐 Security

For security reasons:

* Do not commit `.env`
* Do not expose your Gemini API key
* Do not commit local database files
* Keep credentials and secrets in environment variables
* Use `env.example` for non-secret configuration examples

---

## 🚀 Git Workflow

After making changes to the project:

```powershell
git add .
git commit -m "Updated PocketSmart AI"
git push
```

This updates the existing GitHub repository.

---

## 🎯 Project Goals

PocketSmart AI aims to make budget-based decision-making easier by combining:

**User Budget + Preferences + AI → Personalized Recommendations**

The project demonstrates how modern AI services can be integrated into a web application to create practical recommendation and planning tools.

---

## 🔮 Future Improvements

Possible future development areas include:

* 📊 Advanced budget analytics
* 💡 More recommendation categories
* 👤 Improved user profiles
* 📈 Personalized spending insights
* 🧠 More advanced AI interactions
* 📱 Improved mobile responsiveness
* ☁️ Cloud deployment
* 🔔 Notifications and reminders

---

## 👨‍💻 Developer

**M.K. Prabu**

PocketSmart AI — AI-powered budget and recommendation assistant.

---

## 📄 License

This project is intended for educational and development purposes.
