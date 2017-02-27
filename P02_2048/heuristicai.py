import random
import game
import sys

# Author:				chrn (original by nneonneo)
# Date:				11.11.2016
# Description:			The logic of the AI to beat the game.

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

def find_best_move(board):
    bestmove = find_best_move_heuristic_agent(board)
    # bestmove = find_best_move_random_agent()
    return bestmove

def find_best_move_random_agent():
    return random.choice([UP,DOWN,LEFT,RIGHT])

def find_best_move_heuristic_agent(board):
    moves = [UP, DOWN, LEFT, RIGHT]
    boards = [execute_move(move, board) for move in moves]
    scores = [max(score_board(new_board)) if not board_equals(board, new_board) else 0 for new_board in boards]
    best_score = max(scores)
    return random.choice(moves) if best_score == 0 else moves[scores.index(best_score)]

def score_board(board):
    vertical_score = 0
    horizontal_score = 0

    vertical_searchee = 0
    horizontal_searchee = 0

    for y in range(0, 3):
        for x in range(0, 3):
            horizontal_n = board[y][x]
            if 0 == horizontal_n:
                continue
            elif horizontal_searchee == horizontal_n:
                horizontal_score += 1
                horizontal_searchee = 0
            else:
                horizontal_searchee = horizontal_n

            vertical_n = board[x][y]
            if 0 == vertical_n:
                continue
            elif vertical_searchee == vertical_n:
                vertical_score += 1
                vertical_searchee = 0
            else:
                vertical_searchee = vertical_n

        horizontal_searchee = 0
        vertical_searchee = 0

    return horizontal_score, vertical_score

def execute_move(move, board):
    """
    move and return the grid without a new random tile 
	It won't affect the state of the game in the browser.
    """

    if move == UP:
        return game.merge_up(board)
    elif move == DOWN:
        return game.merge_down(board)
    elif move == LEFT:
        return game.merge_left(board)
    elif move == RIGHT:
        return game.merge_right(board)
    else:
        sys.exit("No valid move")
		
def board_equals(board, newboard):
    """
    Check if two boards are equal
    """
    return  (newboard == board).all()  