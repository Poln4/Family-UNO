# 🃏 Family UNO (C Version)

A simple **C program** that lets friends or family play UNO and keep track of scores in the terminal.

---

## 💡 Description
This is the **command-line** version of *Family UNO*, created as part of my CS50 final project.  
Each player enters their name and score for every round, and the program automatically tracks totals until one player reaches the maximum limit (200 points).

---

## 🕹️ How to Play
1. Compile the program:
   ```bash
   make uno
2. Run the game with player names:
   ./uno Alice Bob Charlie
3. The program will:
Ask for the number of points each player got that round.
Display the updated total for everyone.
End the game automatically when someone reaches or exceeds 200 points.
Announce the winner (the player with the fewest points).
