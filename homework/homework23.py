# Создайте программу для игры в ""Крестики-нолики"".

board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

winner_position = [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8],
                   [0, 3, 6],
                   [1, 4, 7],
                   [2, 5, 8],
                   [0, 4, 8],
                   [2, 4, 6]]


def print_board():
    print(board[0], end=" ")
    print(board[1], end=" ")
    print(board[2])

    print(board[3], end=" ")
    print(board[4], end=" ")
    print(board[5])

    print(board[6], end=" ")
    print(board[7], end=" ")
    print(board[8])


def print_step_board(step, symbol):
    ind = board.index(step)
    board[ind] = symbol


def is_winner():
    winner = ""

    for i in winner_position:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            winner = "Крестики Победили"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            winner = "Нолики победили"

    return winner


game = True
player = True
while game:
    print_board()

    if player:
        symbol = "X"
        step = int(input("Ходит Player 1: "))
        player = False
    else:
        symbol = "O"
        step = int(input("Ходит Player 2: "))
        player = True

    print_step_board(step, symbol)
    winner = is_winner()
    if winner != "":
        game = False
    else:
        game = True

print_board()
print(winner)
