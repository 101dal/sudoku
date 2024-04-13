from Tile import Tile
import random

class SudokuGame:
    def __init__(self) -> None:
        self.plateau: list[list[Tile]] = [[Tile() for _ in range(9)] for _ in range(9)]
        self.possible_values: list[list[list[int]]] = [[[j for j in range(1, 10)] for _ in range(9)] for _ in range(9)]
        
        return
        

        
    def check_array(self, array: list[Tile]) -> bool:
        """Check if an array of Tiles is valid for checking the validity of the board

        Args:
            array (list[Tile]): The list of Tile

        Returns:
            bool: Return True is valid and False otherwise
        """
        s = 0
        elements_list = []
        # Calculate the sum
        for element in array:
            v = element.value
            t = type(v)
            # Verify if it is an integer
            if t != int:
                if t == float:
                    return False
                else:
                    try:
                        v = int(v)
                    except:
                        v = 0
            s += v
            # Ignore if it is 0 or a string
            if v != 0:
                if v in elements_list:
                    return False
                else:
                    elements_list.append(v)
        
        return True
            
    
        
    
    def check_board(self) -> bool:
        """Check if the current board position is valid or not.
        The validity is checked in two ways : first it checks if the sum is greater than 45 then it checks if there are any doubles

        Returns:
            bool: True if yes and False if no
        """
        # Check the lines
        for l in self.plateau:
            if not self.check_array(l):
                return False
        
        # Check the columns
        for i in range(9):
            if not self.check_array([row[i] for row in self.plateau]):
                return False

        # Check the squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [self.plateau[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.check_array(square):
                    return False
        
        return True
    
    def set_not_valid(self, x: int, y: int) -> bool:
        self.plateau[y][x].isValid = False
        
        return False
    
    
    def set_element(self, x, y, value: int) -> bool:
        """Set the value of the Tile at x and y coords to value

        Args:
            x (_type_): X Coord
            y (_type_): Y Coord
            value (int): Value (between 1 and 9 included)

        Returns:
            bool: True if the value has been correctly changed and False otherwise
        """
        self.plateau[y][x].value = value
        try:
            value = int(value)
        except:
            return self.set_not_valid(x, y)
        # Check basic conditions concerning the sizes and the value:
        if not ((0 <= x < 9 ) and (0 <= y < 9) and (1 <= value <= 9)):
            return self.set_not_valid(x, y)
        
        # Check if the value can be modified
        if self.plateau[y][x].isStatic:
            return self.set_not_valid(x, y)
        
        # Try to change to the new value if possible      
        self.plateau[y][x].value = value
        
        if not self.check_board():
            return self.set_not_valid(x, y)
        else:
            self.plateau[y][x].isValid = True
        
        return True
    
    def solve_board(self) -> bool:
        """Solve the Sudoku board using a fill by missing algorithm (I dunno the name so whatever) using the get_legal_values function

        Args:
            row (int, optional): The starting row. Defaults to 0.
            col (int, optional): The starting column. Defaults to 0.

        Returns:
            bool: True if the board is successfully filled, False otherwise.
        """
        
        for i in range(9):
            for j in range(9):
                values = self.possible_values[i][j]
                value = random.choice(values)
                self.plateau[i][j].value = value
                self.remove_legal_value(i, j, value)  # Remove the value from the row, column, and 3x3 square
                self.possible_values[i][j] = []  # Clear the possible values for this cell

        
        return True
        

    def generate_game(self, difficulty: float) -> bool:
        """Function to select generate a game using the difficulty

        Args:
            difficulty (float): Difficulty (float number ranging from 1 to 4 included)

        Returns:
            bool: True if the game has been correctly generated and False otherwise
        """
        # Check the difficulty
        if not (1 <= difficulty <=4):
            return False
        
        self.solve_board()

        # # Then, remove cells to create a puzzle
        # cells_to_remove = int(81 - 20 - (difficulty ** 2.7))
        # removed_cells = 0

        # while removed_cells < cells_to_remove:
        #     row = random.randint(0, 8)
        #     col = random.randint(0, 8)
        #     if self.plateau[row][col].value != 0:
        #         self.plateau[row][col].value = 0
        #         self.plateau[row][col].isStatic = False 
        #         removed_cells += 1
        
        return True
    
    def get_legal_values(self, row, col):
        """Get a list of legal values for the given cell."""
        legal_values = list(range(1, 10))
        for i in range(9):
            # Remove values already present in the same row or column
            if self.plateau[row][i].value in legal_values:
                legal_values.remove(self.plateau[row][i].value)
            if self.plateau[i][col].value in legal_values:
                legal_values.remove(self.plateau[i][col].value)

        # Remove values already present in the same 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.plateau[i][j].value in legal_values:
                    legal_values.remove(self.plateau[i][j].value)

        return legal_values
    
    def get_legal_values(self, row, col):
        """Get a list of legal values for the given cell."""
        return self.possible_values[row][col]
    
    def remove_legal_value(self, row, col, value):
        """Remove all the values from the row, column and 3x3 square of the given cell"""
        print(self.possible_values[row][col])
        # Rows
        for i in range(9):
            try:
                self.possible_values[row][i].remove(value)
            except:
                continue
        
        # Columns
        for e in range(9):
            try:
                self.possible_values[e][col].remove(value)
            except:
                continue
        
        # 3x3 square
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                try:
                    self.possible_values[i][j].remove(value)
                except:
                    continue