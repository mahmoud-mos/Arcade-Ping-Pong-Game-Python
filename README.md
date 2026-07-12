# Arcade Ping-Pong Game 🏓

A smooth, two-player Pong clone built with Python's `turtle` graphics library. This project demonstrates core game development concepts including object-oriented design, physics logic, collision detection, and event-driven programming.

## 🚀 Features
- **Local Multiplayer:** Side-by-side competition on a single keyboard.
- **Dynamic Physics:** Precise collision detection for paddles and screen boundaries.
- **Optimized Performance:** Uses `turtle.tracer(0)` and `ontimer()` for flicker-free, smooth gameplay.
- **Refactored Structure:** Implemented using Object-Oriented Programming (OOP) with modular classes (`Game`, `Paddle`, `Ball`, `ScoreBoard`).
- **Real-Time Score Tracking:** Automatically tracks and displays scores for both players at the top of the screen.

## 📷 Game Preview
![Ping Pong Gameplay](Ping-Pong.jpg)

## 🛠️ Built With
- **Language:** Python 3.14
- **Library:** Turtle (Standard Library)

## 🎮 How to Play

### Requirements
1. Ensure you have [Python](https://www.python.org/) installed.

### Execution
Run the game from the terminal:
```bash
python pong.py
```

### Controls
- **Player A (Left Paddle - Red):**
  - Move Up: `w`
  - Move Down: `s`
- **Player B (Right Paddle - Blue):**
  - Move Up: `Up Arrow`
  - Move Down: `Down Arrow`
