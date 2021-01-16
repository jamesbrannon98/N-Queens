import math
from collections import OrderedDict

def num_placements_all(n):
    return math.factorial(n * n) / (math.factorial(n) * math.factorial((n * n) - n))

def num_placements_one_per_row(n):
    return n ** n

def n_queens_valid(board):
    if len(list(OrderedDict.fromkeys(board))) < len(board):
        return False
    for col in range(len(board)) :
        for nextCol in range(col + 1, len(board)) :
            if abs(col - nextCol) == abs(board[col] - board[nextCol]) :
                return False
    return True

def n_queens_solutions(n):
    for row in range(n):
        for solution in n_queens_helper(n, [row]):
            yield solution

def n_queens_helper(n, board):
    if len(board) == n:
        yield board
    else:
        for row in [rows for rows in range(n) if rows not in board]:
            new = board[:]
            new.append(row)
            if n_queens_valid(new):
                for solution in n_queens_helper(n, new):
                    if solution:
                        yield solution
