# 🃏 Family UNO

### 🎥 Demo
[Watch on YouTube](https://youtu.be/4Ym6EKDC_C8)

### 💡 Description
**Family UNO** is a two-part project:
1. A **C terminal game** to play UNO offline.
2. A **dynamic Flask web app** with a database that keeps track of scores and top winners.

---

## 🎯 Motivation
My motivation comes from my family — we love playing UNO, but we used to record scores on paper.  
This project helps us automatically track rounds, points, and winners, so everyone can just focus on playing.

---

## 🧩 Project Overview

### CLI (C Version)
- Runs entirely in the terminal.  
- Allows players to enter names and input scores each round.  
- Automatically ends when someone reaches or exceeds **200 points**.  
- I tested it with my family during the summer and added improvements based on their feedback.

**Limitations:**  
Currently supports up to 10 rounds and doesn’t save history across sessions.

---

### 🌐 Web App (Flask)
The web version expands functionality with persistent storage using a database.

#### Pages
- **Main Page:** Add players and start a session.  
- **Add Players:** Input and view player list.  
- **New Game:** Resets all points to 0.  
- **Top Winners:** Displays historical winners (persistent records).  
- **Rules:** Explains UNO rules and app usage.

#### Backend
All logic is implemented in `app.py` with helper functions connected to the templates.

---

## 🛠️ Common Features
- Add any number of players.  
- Enter round scores; total is computed automatically.  
- Detects when a player reaches 200 points.  
- Announces the winner and ends the game.

---

## 🔍 Future Improvements
- Allow unlimited rounds (extend DB schema).  
- Show number of rounds played in real time.  
- Add an option to resume previous games.

---

## ⚙️ Run Locally

### C version
```bash
cd cli
make
./uno
