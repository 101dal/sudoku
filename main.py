from SudokuGame import SudokuGame

jeu = SudokuGame()

def printGame():
    # Print the game board
    for l in jeu.original_game:
        for c in l:
            print(c.value, end=" ")
        print()
    print()
    
def printGame2():
    # Print the game board
    for l in jeu.plateau:
        for c in l:
            print(c.value, end=" ")
        print()
    print()

jeu.generate_game(4)
printGame()
printGame2()