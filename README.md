# 🔴🔵 Puissance 4 (Connect 4) AI Master

Welcome to the **Puissance 4 AI Master**! This project is a highly optimized, terminal-based Connect 4 game built entirely in Python. Unlike your average digital board game, this project features an incredibly powerful Artificial Intelligence opponent designed using advanced Game Theory methodologies. 

Prepare to challenge an AI that actively predicts your moves and outsmarts you multiple turns in advance! 🧠🤖

## 🧠 Just How Good is the AI?
The AI in this project isn't just making random guesses; it practically "sees" the future. By fully analyzing the board state, the AI scores every possible sequence (horizontal, vertical, and diagonal) to block your winning moves and secure its own. 

This repository allows you to play against the AI and experience the difference between two classic algorithms:
*   **Simple Minimax Algorithm:** The AI maps out decision trees of the game several depths ahead, predicting the best possible moves for itself assuming the player makes the best possible moves to stop it. 
*   **Alpha-Beta Pruning Algorithm (The Genius Mode):** An incredibly advanced mathematical optimization of the Minimax algorithm. It "prunes" branches of the decision tree that mathematically don't need to be checked. The result? The AI thinks **exponentially faster** and responds ruthlessly without hesitating.

## ✨ Key Features
*   **Unbeatable Logic:** The `evaluate_window` and `score_board` functions calculate positional advantages with extreme precision. It prioritizes center columns, blocks imminent threats, and sets up multi-turn traps.
*   **Terminal Interface:** A clean, easy-to-read ASCII representation of the game board directly in your console.
*   **Algorithm Selector:** Want to see the speed difference? Choose between *Simple Minimax* or *Alpha-Beta Pruning* at the start of every game.
*   **Dynamic Tie/Win Detection:** Flawless state management that catches vertical, horizontal, and both diagonal win conditions instantly.

## 🚀 How to Play

### Prerequisites
*   You need [Python 3.x](https://www.python.org/downloads/) installed on your machine. 
*   Zero external dependencies! The game runs completely on Python's built-in libraries.

### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/achrefbenkhaled/puissance-4-ai-.git
   ```
2. **Navigate to the directory:**
   ```bash
   cd puissance-4-ai-
   ```
3. **Run the game:**
   ```bash
   python "Puissance 4.py"
   ```

### Rule of the Game
*   The board is **7 columns wide** and **6 rows high**.
*   You play as **Player 1 (X)**, and the AI plays as **Player 2 (O)**.
*   When it is your turn, type the number of the column `(0 to 6)` where you want to drop your piece.
*   The first to connect **4** pieces in a row (horizontally, vertically, or diagonally) wins!

## 🛠️ Deep Dive into the Tech
This game serves as an excellent educational showcase of recursive solving and Artificial Intelligence theory.
* `DEPTH`: Controls how many moves into the future the AI can calculate. The default depth provides a tough challenge that plays instantly!
* `minimax_score()`: A beautifully clean recursive loop mimicking mathematical game theory.
* `alpha_beta_score()`: Keeps track of `alpha` (best max score seen) and `beta` (best min score seen) to instantly cut off bad decision paths.

Good luck beating the AI! May the best analytical thinker win. 🏆
