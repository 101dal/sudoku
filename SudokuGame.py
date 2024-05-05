import copy
from Tile import Tile
import random

class SudokuGame:
    def __init__(self):
        self.plateau = [[Tile() for _ in range(9)] for _ in range(9)]
        
        return
        

        
    def check_array(self, array):
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
            
    
        
    
    def check_board(self):
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
    
    def set_not_valid(self, x, y):
        self.plateau[y][x].isValid = False
        
        return False
    
    
    def set_element(self, x, y, value):
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
    
    def solve_board(self, row=0, col=0):
        """Solve the Sudoku board using a backtracking algorithm.

        This function uses a recursive backtracking algorithm to fill the Sudoku board.
        It tries placing numbers from 1 to 9 in each cell, and if it finds a valid number,
        it recursively tries to fill the next cell. If it can't find a valid number, it
        backtracks and tries a different number.

        Args:
            row (int, optional): The starting row. Defaults to 0.
            col (int, optional): The starting column. Defaults to 0.

        Returns:
            bool: True if the board is successfully filled, False otherwise.
        """
        
        if row == 9:
            return True

        if col == 9:
            return self.solve_board(row + 1, 0)

        if self.plateau[row][col].value != 0:
            return self.solve_board(row, col + 1)
        
        
        random_sequence = list(range(1,10))
        
        for _ in range(1, 10):
            rn = random.randint(0, len(random_sequence) - 1)
            num = random_sequence[rn]
            del random_sequence[rn]
            if self.plateau[row][col].can_place_num(num, row, col, self.plateau):
                self.plateau[row][col].value = num
                self.plateau[row][col].isStatic = True
                if self.solve_board(row, col + 1):
                    return True
            
            self.plateau[row][col].value = 0
            

        # for num in range(1, 10):
        #     if self.plateau[row][col].can_place_num(num, row, col, self.plateau):
        #         self.plateau[row][col].value = num
        #         self.plateau[row][col].isStatic = True
        #         if self.solve_board(row, col + 1):
        #             return True
        #         self.plateau[row][col].value = 0
        


        return False

    def generate_game(self, difficulty):
        """Function to select generate a game using the difficulty

        Args:
            difficulty (float): Difficulty (float number ranging from 1 to 4 included)

        Returns:
            bool: True if the game has been correctly generated and False otherwise
        """
        # Check the difficulty
        if not (1 <= difficulty <=4):
            return False
        
        # Create a pseudo random board from the start with a random value for the first element
        for _ in range(5):
            random_x = random.randint(0,8)
            random_y = random.randint(0,8)
            v = random.randint(1,9)
            if self.plateau[random_y][random_x].can_place_num(v, random_y, random_x, self.plateau):
                self.plateau[random_y][random_x].value = 0
                self.plateau[random_y][random_x].isStatic = True
        
        # First, fill the board
        self.solve_board()
        
        self.solved_board = copy.deepcopy(self.plateau)

        # Then, remove cells to create a puzzle
        diff_range = {1: [20, 30], 2:[35,45], 3: [45,55], 4: [55,60]}[difficulty]
        cells_to_remove = random.randint(diff_range[0], diff_range[1])
        removed_cells = 0

        while removed_cells < cells_to_remove:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.plateau[row][col].value != 0:
                self.plateau[row][col].value = 0
                self.plateau[row][col].isStatic = False 
                removed_cells += 1
        
        return True