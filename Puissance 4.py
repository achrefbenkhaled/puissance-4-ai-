import math
import random

ROWS, COLS = 6, 7
PLAYER, BOT, EMPTY = 1, 2, 0
WIN_COUNT = 4
DEPTH = 3

def create_board():
    return [[EMPTY] * COLS for _ in range(ROWS)]

def print_board(board):
    print("\n  " + " ".join(map(str, range(COLS))))
    for row in board:
        print(" |" + "|".join(' ' if c == EMPTY else 'X' if c == PLAYER else 'O' for c in row) + "|")
    print("-" * (2 * COLS + 3))

def is_valid_col(board, col):
    return board[0][col] == EMPTY

def get_next_row(board, col):
    for r in reversed(range(ROWS)):
        if board[r][col] == EMPTY:
            return r
    return None

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def check_win(board, piece):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == piece for i in range(4)):
                return True
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True
    return False

def get_valid_cols(board):
    return [c for c in range(COLS) if is_valid_col(board, c)]

def evaluate_window(window, piece):
    opp = PLAYER if piece == BOT else BOT
    score = 0
    if window.count(piece) == 4: score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1: score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2: score += 2
    if window.count(opp) == 3 and window.count(EMPTY) == 1: score -= 4
    return score

def score_board(board, piece):
    score = 0
    center = [board[r][COLS // 2] for r in range(ROWS)]
    score += center.count(piece) * 3
    for row in board:
        for c in range(COLS - 3):
            score += evaluate_window(row[c:c + 4], piece)
    for c in range(COLS):
        col = [board[r][c] for r in range(ROWS)]
        for r in range(ROWS - 3):
            score += evaluate_window(col[r:r + 4], piece)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            diag = [board[r + i][c + i] for i in range(4)]
            score += evaluate_window(diag, piece)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            anti_diag = [board[r - i][c + i] for i in range(4)]
            score += evaluate_window(anti_diag, piece)
    return score

def is_terminal(board):
    return check_win(board, PLAYER) or check_win(board, BOT) or not get_valid_cols(board)

def is_tie(board):
    return not get_valid_cols(board) and not check_win(board, PLAYER) and not check_win(board, BOT)

# Minimax without alpha-beta
def minimax_score(board, depth, maximizing):
    if check_win(board, BOT):
        return 100000
    if check_win(board, PLAYER):
        return -100000
    if is_tie(board):
        return 0
    if depth == 0:
        return score_board(board, BOT)
    if maximizing:
        max_eval = -math.inf
        for col in get_valid_cols(board):
            row = get_next_row(board, col)
            temp = [r[:] for r in board]
            drop_piece(temp, row, col, BOT)
            eval = minimax_score(temp, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for col in get_valid_cols(board):
            row = get_next_row(board, col)
            temp = [r[:] for r in board]
            drop_piece(temp, row, col, PLAYER)
            eval = minimax_score(temp, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def best_move_simple(board):
    for col in get_valid_cols(board):
        row = get_next_row(board, col)
        temp = [r[:] for r in board]
        drop_piece(temp, row, col, BOT)
        if check_win(temp, BOT):
            return col
    best_score = -math.inf
    move = None
    for col in get_valid_cols(board):
        row = get_next_row(board, col)
        temp = [r[:] for r in board]
        drop_piece(temp, row, col, BOT)
        score = minimax_score(temp, DEPTH, False)
        if score > best_score:
            best_score = score
            move = col
    return move

# Alpha-beta pruning
def alpha_beta_score(board, depth, alpha, beta, maximizing):
    if check_win(board, BOT):
        return 100000
    if check_win(board, PLAYER):
        return -100000
    if is_tie(board):
        return 0
    if depth == 0:
        return score_board(board, BOT)
    if maximizing:
        max_eval = -math.inf
        for col in get_valid_cols(board):
            row = get_next_row(board, col)
            temp = [r[:] for r in board]
            drop_piece(temp, row, col, BOT)
            eval = alpha_beta_score(temp, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for col in get_valid_cols(board):
            row = get_next_row(board, col)
            temp = [r[:] for r in board]
            drop_piece(temp, row, col, PLAYER)
            eval = alpha_beta_score(temp, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move_alpha_beta(board):
    for col in get_valid_cols(board):
        row = get_next_row(board, col)
        temp = [r[:] for r in board]
        drop_piece(temp, row, col, BOT)
        if check_win(temp, BOT):
            return col
    best_score = -math.inf
    move = None
    for col in get_valid_cols(board):
        row = get_next_row(board, col)
        temp = [r[:] for r in board]
        drop_piece(temp, row, col, BOT)
        score = alpha_beta_score(temp, DEPTH, -math.inf, math.inf, False)
        if score > best_score:
            best_score = score
            move = col
    return move

# Main game loop
def play():
    board = create_board()
    print_board(board)
    turn = random.choice([PLAYER, BOT])
    algo = input("Choose bot: 1) Alpha-Beta 2) Simple Minimax: ")
    use_simple = algo.strip() == '2'
    while True:
        if turn == PLAYER:
            col = input("Your move (0–6): ")
            if not col.isdigit() or int(col) not in range(COLS):
                print("Invalid.")
                continue
            col = int(col)
            if not is_valid_col(board, col):
                print("Column full.")
                continue
            row = get_next_row(board, col)
            drop_piece(board, row, col, PLAYER)
            if check_win(board, PLAYER):
                print_board(board)
                print("You win!")
                break
            turn = BOT
        else:
            print("Bot is thinking...")
            if use_simple:
                col = best_move_simple(board)
            else:
                col = best_move_alpha_beta(board)
            print(f"Bot chooses column: {col}")
            row = get_next_row(board, col)
            drop_piece(board, row, col, BOT)
            if check_win(board, BOT):
                print_board(board)
                print("Bot wins!")
                break
            turn = PLAYER
        print_board(board)
        if not get_valid_cols(board):
            print("It's a draw!")
            break

play()
