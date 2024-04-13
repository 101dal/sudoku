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
        
    def setValidity(self, validity: bool) -> None:
        """Set the validity of that tile

        Args:
            validity (bool): True if valid and False otherwise
        """
        self.isValid = validity

        return
    
    def setValue(self, value: int) -> bool:
        if self.isStatic:
            return True
        
        if value < 0 or value > 9:
            self.isValid = False
            return False
        return True