from SudokuGame import SudokuGame

jeu = SudokuGame()

def printGame():
    # Print the game board
    for l in jeu.plateau:
        for c in l:
            print(c.value, end=" ")
        print()
    print()

try:
    jeu.generate_game(1)
except:
    printGame()