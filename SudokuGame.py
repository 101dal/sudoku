from Tile import Tile

class SudokuGame:
    def __init__(self) -> None:
        self.plateau: list[list[Tile]] = [[Tile() for _ in range(9)] for _ in range(9)]
        
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
            s += v
            # Ignore if it is 0
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
    
    
    def set_element(self, x, y, value: int) -> bool:
        """Set the value of the Tile at x and y coords to value

        Args:
            x (_type_): X Coord
            y (_type_): Y Coord
            value (int): Value (between 1 and 9 included)

        Returns:
            bool: True if the value has been correctly changed and False otherwise
        """
        # Check basic conditions concerning the sizes and the value:
        if not ((0 <= x < 9 ) and (0 <= y < 9) and (1 <= value <= 9)):
            return False
        
        # Check if the value can be modified
        if self.plateau[y][x].isStatic:
            return False
        
        # Try to change to the new value if possible        
        previous_value = self.plateau[y][x].value
        self.plateau[y][x].value = value
        
        if not self.check_board():
            self.plateau[y][x].value = previous_value
            return False
        
        
        return True