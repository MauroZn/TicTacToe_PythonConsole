import random
from matrix import Matrix

matrixClass = Matrix()

game = True

def check_win(player_symbol):
    for combination in matrixClass.winning_combinations:
        if all(matrixClass.matrix[row][col] == player_symbol for row, col in combination):
            print("Game Over! Player", player_symbol, "wins!")
            return True
    return False

def player_move():
    if not hasattr(player_move, "has_run"):
        print("Position of the board:\n1-2-3\n4-5-6\n7-8-9")
        player_move.has_run = True
    x_position = input("Where do you wanna put the X? (1-9): ")

    if x_position in matrixClass.position_map:
        row, col = matrixClass.position_map[x_position]
        if matrixClass.matrix[row][col] == " ":
            matrixClass.matrix[row][col] = "X"
        else:
            print("That spot is already taken!")
            matrixClass.print_game_board()
            player_move()

    else:
        print("Invalid input! Please choose a number from 1 to 9.")
        matrixClass.print_game_board()
        player_move()


def pc_move():
    x_position = str(random.randint(1, 9))
    row, col = matrixClass.position_map[x_position]
    if matrixClass.matrix[row][col] == " ":
        matrixClass.matrix[row][col] = "O"
    elif matrixClass.is_board_full():
        return False
    else:
        pc_move()

while game:
    player_move()
    pc_move()
    matrixClass.print_game_board()
    if check_win('X') is False:
        if check_win('O') is True:
            game = False
        elif matrixClass.is_board_full():
            print("It's a draw! No more moves left.")
            game = False
    else:
        game = False

