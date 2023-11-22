import random


def easy_level(board, computer, cases):
    move = random.choice(cases)
    print("I shall take square number", move)

    row = int(move / 3)
    col = int(move - (row * 3))
    board[row][col] = computer
    return board
