class Matrix:
    def __init__(self):
        self.matrix = [
            [' ', '|', ' ', '|', ' '],
            [' ', '|', ' ', '|', ' '],
            [' ', '|', ' ', '|', ' ']
        ]
        self.position_map = {
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
        self.winning_combinations = [
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

    def print_game_board(self):
        for row in self.matrix:
            print("".join(row))

    def is_board_full(self):
        for row, col in [(0, 0), (0, 2), (0, 4),
                        (1, 0), (1, 2), (1, 4),
                        (2, 0), (2, 2), (2, 4)]:
            if self.matrix[row][col] == ' ':
                return False
        return True