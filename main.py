from SudokuGame import SudokuGame

jeu = SudokuGame()

def printGame():
    # Print the game board
    for l in jeu.plateau:
        for c in l:
            print(c.value, end=" ")
        print()
    print()

printGame()

jeu.generate_game(1)
jeu.generate_game(2)
jeu.generate_game(3)
jeu.generate_game(4)