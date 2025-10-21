# 🃏 Family UNO (Web App)

A web-based version of the classic UNO score tracker, built with **Flask**, **SQLite**, and **HTML/CSS**.  
It lets families or friends track UNO games, keep persistent score history, and view top winners.

---

## 🎥 Demo
[🎬 Watch the Final Project Demo on YouTube](https://youtu.be/4Ym6EKDC_C8)

---

## 💡 Overview

The Family UNO web app allows players to:

- ➕ Add players dynamically  
- 🧮 Record points per round  
- 🏁 End the game automatically when someone reaches 200 points  
- 🏆 View Top Winners across all sessions  
- 📜 See UNO rules and instructions  

It replaces paper scorekeeping with a clean, easy-to-use digital interface.

---

## 🧭 Project Structure
```
web/
├── app.py
├── helpers.py
├── schema.sql
├── requirements.txt
├── .env.example
├── static/
│   └── styles.css
└── templates/
    ├── layout.html
    ├── index.html
    ├── add_players.html
    ├── new_game.html
    ├── top_winners.html
    ├── rules.html
    └── apology.html
```

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask, Flask-Session)  
- **Frontend:** HTML + CSS (Jinja2 templates)  
- **Database:** SQLite (via CS50’s SQL helper)  

---

## ⚙️ Setup & Run Locally

### 1️⃣ Clone or download the repository
```bash
git clone https://github.com/Poln4/final-project.git
cd web
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure environment variables
Copy the example file and edit it:
```bash
cp .env.example .env
```

Example `.env`
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
```

### 4️⃣ Initialize the database
```bash
sqlite3 uno.db < schema.sql
```

### 5️⃣ Run the application
```bash
flask run
```

Then open ➡️ [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🧩 Core Features

| Feature | Description |
|----------|--------------|
| **Add Players** | Create a new player list for each session |
| **Add Points** | Input round scores — totals update automatically |
| **Top Winners** | Persistent record of past winners |
| **New Game** | Resets all scores to 0 |
| **Rules** | Displays UNO rules and how to use the app |

---

## 🔒 Important Notes
- Do not commit `.env` or `uno.db` to GitHub.  
- Use `.env.example` only as a template for your local settings.

---

## 🚀 Future Improvements
- Unlimited rounds support  
- Live leaderboard that updates without refresh  
- User authentication (family logins)  
- Visual stats and round charts  

---

## 👤 Author
Developed by **Poln4** for [CS50x 2022 Final Project](https://cs50.harvard.edu/x/2022/).  
👉 **Demo Video:** [https://youtu.be/4Ym6EKDC_C8](https://youtu.be/4Ym6EKDC_C8)
