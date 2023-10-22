"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns the starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns the player who has the next turn on a board.
    """
    countX = 0
    countO = 0

    for row in board:
        for col in row:
            if col == 'X':
                countX += 1
            elif col == "O":
                countO += 1
    if countX > countO:
        return 'O'
    else:
        return 'X'


def actions(board):
    """
    Returns a set of all possible actions (i, j) available on the board.
    """
    return_Set = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return_Set.add((i, j))

    return return_Set


def result(board, action):
    """
    Returns the board that results from making the move (i, j) on the board.
    """
    duplicateBoard = copy.deepcopy(board)

    if duplicateBoard[action[0]][action[1]] == EMPTY:
        playerTurn = player(board)
        duplicateBoard[action[0]][action[1]] = playerTurn

    else:
        raise NameError('Invalid move')

    return duplicateBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    size = len(board)

    for i in range(size):
        # Check rows
        if all(board[i][j] == 'X' for j in range(size)):
            return 'X'
        elif all(board[i][j] == 'O' for j in range(size)):
            return 'O'

        # Check columns
        if all(board[j][i] == 'X' for j in range(size)):
            return 'X'
        elif all(board[j][i] == 'O' for j in range(size)):
            return 'O'

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(size)):
        return 'X'
    elif all(board[i][size - i - 1] == 'X' for i in range(size)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(size)):
        return 'O'
    elif all(board[i][size - i - 1] == 'O' for i in range(size)):
        return 'O'

    return None


def terminal(board):
    if winner(board) is not None:
        return True
    if len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    gameWinner = winner(board)
    if gameWinner == 'X':
        return 1
    if gameWinner == 'O':
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if player(board) == 'X':
        return max(actions(board), key=lambda action: min_value(result(board, action)))
    else:
        return min(actions(board), key=lambda action: max_value(result(board, action)))
