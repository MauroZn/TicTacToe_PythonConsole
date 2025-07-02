import random
from classes.matrix import Matrix

matrixClass = Matrix()

game = True
pc_caught_player_winning = False

def check_win(player_symbol):
    for combination in matrixClass.winning_combinations:
        if all(matrixClass.matrix[row][col] == player_symbol for row, col in combination):
            print("Game Over! Player", player_symbol, "wins!")
            return True
    return False

def player_move():
    if not hasattr(player_move, "has_run"):
        print("Position of the board:\n1-2-3\n4-5-6\n7-8-9")
        print("-----")
        matrixClass.print_game_board()
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

def pc_check_player_winning_condition():
    global pc_caught_player_winning
    for combination in matrixClass.winning_combinations:
        player_count = 0
        empty_count = 0
        empty_spot = None

        for row, col in combination:
            if matrixClass.matrix[row][col] == "X":
                player_count += 1
            elif matrixClass.matrix[row][col] == " ":
                empty_count += 1
                empty_spot = (row, col)

        if player_count == 2 and empty_count == 1:
            row, col = empty_spot
            matrixClass.matrix[row][col] = "O"
            pc_caught_player_winning = True
            return

    pc_caught_player_winning = False

def pc_move():
    global pc_caught_player_winning
    x_position = str(random.randint(1, 9))
    row, col = matrixClass.position_map[x_position]
    pc_check_player_winning_condition()

    if not pc_caught_player_winning:
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

