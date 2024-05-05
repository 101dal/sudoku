class Tile:
    def __init__(self):
        self.value = 0
        self.isStatic = False
        self.isValid = True

    def set_validity(self, validity):
        self.isValid = validity

    def set_value(self, value):
        if self.isStatic:
            return
        self.value = value
        return True

    def can_place_num(self, num, row, col, board):
        # Check the row
        for i in range(9):
            if board[row][i].value == num:
                return False

        # Check the column
        for i in range(9):
            if board[i][col].value == num:
                return False

        # Check the 3x3 grid
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col].value == num:
                    return False

        return True