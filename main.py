import random

matrix = [
    [' ', '|', ' ', '|', ' '],
    [' ', '|', ' ', '|', ' '],
    [' ', '|', ' ', '|', ' ']
]

position_map = {
    "1": (0, 0),
    "2": (0, 2),
    "3": (0, 4),
    "4": (1, 0),
    "5": (1, 2),
    "6": (1, 4),
    "7": (2, 0),
    "8": (2, 2),
    "9": (2, 4),
}

winning_combinations = [
    #Rows
    [(0, 0), (0, 2), (0, 4)],
    [(1, 0), (1, 2), (1, 4)],
    [(2, 0), (2, 2), (2, 4)],
    #Columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 4), (1, 4), (2, 4)],
    #Diagonals
    [(0, 0), (1, 2), (2, 4)],
    [(0, 4), (1, 2), (2, 0)]
]

game = True

def check_win(player_symbol):
    for combination in winning_combinations:
        if all(matrix[row][col] == player_symbol for row, col in combination):
            print("Game Over! Player", player_symbol, "wins!")
            return True
    return False

def print_game_board(matrix):
    for row in matrix:
        print("".join(row))

def is_board_full():
    for row, col in [(0,0), (0,2), (0,4),
                     (1,0), (1,2), (1,4),
                     (2,0), (2,2), (2,4)]:
        if matrix[row][col] == ' ':
            return False
    return True

def player_move():
    if not hasattr(player_move, "has_run"):
        print("Position of the board:\n1-2-3\n4-5-6\n7-8-9")
        player_move.has_run = True
    x_position = input("Where do you wanna put the X? (1-9): ")

    if x_position in position_map:
        row, col = position_map[x_position]
        if matrix[row][col] == " ":
            matrix[row][col] = "X"
        else:
            print("That spot is already taken!")
    else:
        print("Invalid input! Please choose a number from 1 to 9.")

def pc_move():
    x_position = str(random.randint(1, 9))
    row, col = position_map[x_position]
    if matrix[row][col] == " ":
        matrix[row][col] = "O"
    elif is_board_full():
        return False
    else:
        pc_move()

while game:
    player_move()
    pc_move()
    print_game_board(matrix)
    if is_board_full():
        print("It's a draw! No more moves left.")
        game = False
    elif check_win('X') is False:
        if check_win('O') is True:
            game = False
    else:
        game = False

