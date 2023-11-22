from computer_move.easy import easy_level
from computer_move.hard import hard_level


def initial_board():
    board = [[" " for x in range(3)] for y in range(3)]
    return board


def display_board(board):
    for r in range(3):
        print("\t\t", board[r][0], " | ", board[r][1], " | ", board[r][2], sep="")
        if r != 2:
            print("\t\t---------")


def player(board):
    first, last = 0, 0
    for i in board:
        for j in i:
            if j == "X":
                first += 1
            elif j == "O":
                last += 1

    if first == last:
        return "X"
    else:
        return "O"


def human_move(board, human, cases):
    while True:
        i = None
        move = int(input("Where will you move? <0 - 8>:"))
        for i in cases:
            if move == i:
                break

        if move == i:
            print("Fine..")
            break
        else:
            print("Error")

    row = int(move / 3)
    col = int(move - (row * 3))
    board[row][col] = human
    return board


def actions(board):
    cases = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                cases.append((i * 3) + j)

    return cases


def terminal(board):
    for i in range(len(board)):
        row_index = board[i][0]
        col_index = board[0][i]
        row_tmp, col_tmp = 0, 0

        for j in range(len(board[i])):
            if row_index == board[i][j]:
                row_tmp += 1
            if col_index == board[j][i]:
                col_tmp += 1

        if row_tmp == 3:
            return row_index
        if col_tmp == 3:
            return col_index

    diag = board[1][1]
    if not diag == " ":
        if (diag == board[0][0] and diag == board[2][2]) or\
                (diag == board[0][2] and diag == board[2][0]):
            return diag

    return False


def play_tic_tac_toe(human, computer, diff):
    board = initial_board()
    turn = player(board)

    if diff == 1:
        level = easy_level
    else:
        level = hard_level

    while True:
        cases = actions(board)
        if turn == human:
            board = human_move(board, human, cases)

        else:
            board = level(board, computer, cases)

        display_board(board)
        turn = player(board)
        print("\n")
        winner = terminal(board)
        if not winner:
            continue
        elif winner == human:
            print("human is win")
            break
        elif winner == computer:
            print("computer is win")
            break
