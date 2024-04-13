class Tile:
    def __init__(self) -> None:
        """Create a new tile
        Possible variables : 
        - value (int): the value (between 0 and 9) of the tile
        - isStatic (bool): if the tile's value can be modified
        - isValid (bool): if the tile is valid
        """
        self.value: int = 0
        
        self.isStatic: bool = False
        
        self.isValid: bool = True
        
    def set_validity(self, validity: bool) -> None:
        """Set the validity of that tile

        Args:
            validity (bool): True if valid and False otherwise
        """
        self.isValid = validity

        return
    
    def set_value(self, value: int) -> bool:
        """Sets the value of that Tile

        Args:
            value (int): The value to be set

        Returns:
            bool: True if the value has been changed and False otherwise
        """
        if self.isStatic:
            return True
        
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