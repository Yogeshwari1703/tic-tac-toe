import math
from typing import List, Optional, Tuple

# Board is a list of 9 cells: 'X', 'O', or ' '
# Indices map to keypad layout:
#  1 | 2 | 3
# -----------
#  4 | 5 | 6
# -----------
#  7 | 8 | 9

HUMAN = 'X'
AI = 'O'
EMPTY = ' '

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),      # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),      # cols
    (0, 4, 8), (2, 4, 6)                  # diagonals
]

def print_board(board: List[str]) -> None:
    symbols = [c if c != EMPTY else str(i+1) for i,c in enumerate(board)]
    rows = [
        f" {symbols[0]} | {symbols[1]} | {symbols[2]} ",
        f" {symbols[3]} | {symbols[4]} | {symbols[5]} ",
        f" {symbols[6]} | {symbols[7]} | {symbols[8]} ",
    ]
    sep = "-" * 11
    print("\n" + rows[0] + "\n" + sep + "\n" + rows[1] + "\n" + sep + "\n" + rows[2] + "\n")

def winner(board: List[str]) -> Optional[str]:
    for a,b,c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_full(board: List[str]) -> bool:
    return all(c != EMPTY for c in board)

def available_moves(board: List[str]) -> List[int]:
    return [i for i,c in enumerate(board) if c == EMPTY]

def evaluate(board: List[str], depth: int) -> int:
    w = winner(board)
    if w == AI:    # prefer quicker wins -> bigger score for shallow depth
        return 10 - depth
    if w == HUMAN: # prefer delaying losses -> smaller negative for deeper depth
        return depth - 10
    return 0

def minimax(board: List[str], depth: int, alpha: int, beta: int, maximizing: bool, depth_limit: Optional[int]) -> Tuple[int, Optional[int]]:
    w = winner(board)
    if w or is_full(board):
        return evaluate(board, depth), None
    if depth_limit is not None and depth >= depth_limit:
        # Shallow heuristic: static evaluation = 0 (neutral) + some minor center/corner bias
        score = 0
        # slight positional heuristic
        center = 4
        corners = [0,2,6,8]
        if board[center] == AI: score += 1
        if board[center] == HUMAN: score -= 1
        score += sum(1 for i in corners if board[i] == AI) * 0.3
        score -= sum(1 for i in corners if board[i] == HUMAN) * 0.3
        return int(score), None

    if maximizing:
        best_score = -math.inf
        best_move = None
        for i in available_moves(board):
            board[i] = AI
            score, _ = minimax(board, depth+1, alpha, beta, False, depth_limit)
            board[i] = EMPTY
            if score > best_score:
                best_score, best_move = score, i
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # alpha-beta prune
        return best_score, best_move
    else:
        best_score = math.inf
        best_move = None
        for i in available_moves(board):
            board[i] = HUMAN
            score, _ = minimax(board, depth+1, alpha, beta, True, depth_limit)
            board[i] = EMPTY
            if score < best_score:
                best_score, best_move = score, i
            beta = min(beta, best_score)
            if beta <= alpha:
                break  # alpha-beta prune
        return best_score, best_move

def get_ai_move(board: List[str], depth_limit: Optional[int]) -> int:
    # Opening book: take center if free, else a corner — helps on limited depths too
    if board[4] == EMPTY:
        return 4
    for i in [0,2,6,8]:
        if board[i] == EMPTY:
            # still run minimax to remain principled; this just gives a good start
            break
    _, move = minimax(board, depth=0, alpha=-math.inf, beta=math.inf, maximizing=True, depth_limit=depth_limit)
    # fallback (shouldn't happen)
    return move if move is not None else available_moves(board)[0]

def human_turn(board: List[str]) -> None:
    while True:
        try:
            cell = int(input("Your move (1-9): "))
            if not 1 <= cell <= 9:
                print("Enter a number from 1 to 9.")
                continue
            idx = cell - 1
            if board[idx] != EMPTY:
                print("That cell is taken. Try another.")
                continue
            board[idx] = HUMAN
            return
        except ValueError:
            print("Please enter a valid number 1-9.")

def ai_turn(board: List[str], depth_limit: Optional[int]) -> None:
    print("AI thinking...")
    move = get_ai_move(board, depth_limit)
    board[move] = AI
    print(f"AI played at position {move+1}")

def play_game():
    print("\n=== Tic-Tac-Toe — Minimax with Alpha-Beta ===")
    print("You are X. AI is O.\n")
    difficulty = None
    while difficulty not in ("1","2","3"):
        difficulty = input("Choose difficulty (1=Easy, 2=Medium, 3=Hard): ").strip()
    # Depth limits: None = full search (optimal). Lower = faster/easier.
    depth_limit = {"1": 2, "2": 4, "3": None}[difficulty]

    first = None
    while first not in ("Y","N"):
        first = input("Do you want to start? (Y/N): ").strip().upper()

    board = [EMPTY]*9
    turn = HUMAN if first == "Y" else AI

    while True:
        print_board(board)
        w = winner(board)
        if w or is_full(board):
            break
        if turn == HUMAN:
            human_turn(board)
            turn = AI
        else:
            ai_turn(board, depth_limit)
            turn = HUMAN

    print_board(board)
    w = winner(board)
    if w == HUMAN:
        print("🎉 You win!")
    elif w == AI:
        print("🤖 AI wins!")
    else:
        print("🤝 It's a draw.")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (Y/N): ").strip().upper()
        if again != "Y":
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
