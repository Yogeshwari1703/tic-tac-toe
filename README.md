


**Implement Alpha-Beta Tree Search for Tic-Tac-Toe**

---

## 📝 Problem Statement

The task is to implement **Tic-Tac-Toe** as a two-player game (Human vs AI) using:

* **Non-AI Technique:** Human vs Human play (baseline).
* **AI Technique:** Human vs Computer using **Minimax Algorithm with Alpha-Beta Pruning**.

The goal is to analyze how **AI-based search improves decision-making**, optimizes moves, and ensures the AI plays optimally.

---

## 🎯 Objective

* Understand **Game Tree Search** techniques.
* Implement the **Minimax algorithm** for two-player games.
* Use **Alpha-Beta pruning** to optimize the Minimax search.
* Compare **AI vs non-AI techniques** in gameplay.

---

## 🚀 Features

* **Human vs AI gameplay** (AI is unbeatable on hard mode).
* **Difficulty levels** (Easy, Medium, Hard).

  * Easy → limited depth search (AI makes mistakes).
  * Medium → moderate depth search.
  * Hard → full Minimax (optimal play).
* **Alpha-Beta pruning** reduces the number of explored states.
* **Replay option** without restarting the program.
* **Text-based board** with 1–9 keypad layout for intuitive play.

---

## ⚙️ How It Works

* **Minimax Algorithm:**

  * Explores all possible future moves.
  * Chooses the move that maximizes AI’s chances and minimizes the human’s chances.

* **Alpha-Beta Pruning:**

  * Skips exploring branches that cannot affect the final decision.
  * Makes the AI run **faster** without losing optimality.

* **Scoring Function:**

  * AI win = +10 − depth (faster wins are better).
  * Human win = −10 + depth (slower losses are better).
  * Draw = 0.

---

## 🎮 How to Play

1. Run the game:

   ```bash
   python tictactoe_alpha_beta.py
   ```

2. Choose **difficulty level** (1 = Easy, 2 = Medium, 3 = Hard).

3. Choose whether you want to start first.

4. Play by entering numbers (1–9) as per the grid layout:

   ```
    1 | 2 | 3
   -----------
    4 | 5 | 6
   -----------
    7 | 8 | 9
   ```

5. AI plays automatically after your move.

6. Game ends with a **Win / Loss / Draw** message.

---

## 📊 Example Run

```
=== Tic-Tac-Toe — Minimax with Alpha-Beta ===
You are X. AI is O.

Choose difficulty (1=Easy, 2=Medium, 3=Hard): 3
Do you want to start? (Y/N): Y

 X | 2 | 3
-----------
 4 | O | 6
-----------
 7 | 8 | 9

Your move (1-9): 3
```

🤖 AI blocks, takes optimal moves, and game continues until win/draw.

---

## 🧮 Complexity Analysis

* **Minimax without pruning:** O(b^d)

  * b = branching factor (≈ 9 at start, decreases as game progresses).
  * d = depth of game tree (≤ 9).
* **With Alpha-Beta pruning:** \~O(b^(d/2)) in best case.

  * Cuts down unnecessary states, making it much faster.

---

## ✅ Outcome


* Understand **AI vs Non-AI** approaches in game playing.
* Gain practical experience with **Minimax & Alpha-Beta pruning**.
* See how pruning improves efficiency while maintaining **optimality**.
* Explore decision-making in adversarial search problems.
