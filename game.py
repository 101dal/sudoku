import copy
import tkinter as tk
from SudokuGame import SudokuGame

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.root.geometry("600x600")

        self.window_width = 600
        self.window_height = 600

        self.root.bind('<Configure>', self.get_window_size)
        self.root.resizable(False, False)


        self.difficulty_levels = {"Easy": 1, "Medium": 2, "Hard": 3, "Impossible": 4}

        self.game = SudokuGame()

        self.create_widgets()
        self.update_board()

        # Set the weights of the rows and columns to make the Sudoku board take up more space
        for i in range(11):
            self.root.grid_rowconfigure(i, weight=1 if i < 9 else 0)
            self.root.grid_columnconfigure(i, weight=1 if i < 9 else 0)

        self.new_game()
        return

    def get_window_size(self, event=None):
        self.window_width = self.root.winfo_width()
        self.window_height = self.root.winfo_height()

    def reset_entries(self) -> None:
        # Create the StringVars for the Sudoku board
        self.vars = []
        for i in range(9):
            row = []
            for j in range(9):
                var = tk.StringVar()
                row.append(var)
            self.vars.append(row)

        # Create the entries for the Sudoku board
        self.entries = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = tk.Entry(self.root, width=2, font=("Arial", 35), justify="center", bg="white", textvariable=self.vars[i][j])
                entry.grid(row=i, column=j)
                self.vars[i][j].trace("w", lambda *args, e=entry, x=j, y=i: self.on_entry_change(e, x, y, *args))
                row.append(entry)
            self.entries.append(row)
        
        return
    
    def create_widgets(self):
        self.reset_entries()

        # Create the buttons
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_game)
        solve_button.grid(row=9, column=0, columnspan=3, pady=(10, 0))

        reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        reset_button.grid(row=9, column=3, columnspan=3, pady=(10, 0))

        new_game_button = tk.Button(self.root, text="New Game", command=self.new_game)
        new_game_button.grid(row=9, column=6, columnspan=3, pady=(10, 0))

        # Create the difficulty dropdown
        self.difficulty_var = tk.StringVar(self.root)
        self.difficulty_var.set("Easy")
        difficulty_options = list(self.difficulty_levels)
        difficulty_dropdown = tk.OptionMenu(self.root, self.difficulty_var, *difficulty_options)
        difficulty_dropdown.grid(row=10, column=0, columnspan=9, pady=(10, 0))

    def update_board(self):
        for i in range(9):
            for j in range(9):
                value = self.game.plateau[i][j].value
                if value == 0:
                    self.entries[i][j].delete(0, "end")
                else:
                    self.entries[i][j].delete(0, "end")
                    self.entries[i][j].insert(0, value)

                # Set the background color of the entry based on whether it's a static tile or not
                if self.game.plateau[i][j].isStatic:
                    self.entries[i][j].configure(state='readonly', fg='black')
                elif not self.game.plateau[i][j].isValid:
                    self.entries[i][j].configure(fg='red')
                else:
                    self.entries[i][j].config(bg="white", fg='black')

    def solve_game(self):
        # Solve the Sudoku game
        self.game.plateau = copy.deepcopy(self.solved_board)
        self.update_board()

    def reset_game(self):
        # Reset the Sudoku game to its initial state
        self.reset_entries()
        self.game.plateau = copy.deepcopy(self.original_board)
        self.update_board()




    def new_game(self):
        # Generate a new Sudoku game based on the selected difficulty
        difficulty_level = self.difficulty_levels[self.difficulty_var.get()]

        self.reset_entries()

        self.game = SudokuGame()

        # Generate the game
        self.game.generate_game(difficulty_level)
        
        self.original_board = copy.deepcopy(self.game.plateau)
        self.solved_board = copy.deepcopy(self.game.solved_board)
        
        self.update_board()


    def on_entry_change(self, entry, x, y, *args):
        value = entry.get()
        if self.game.set_element(x, y, value):  # Only update the entry if the value is valid
            entry.configure(fg='black')
        else:
            entry.configure(fg='red')
        return

root = tk.Tk()
gui = SudokuGUI(root)
root.mainloop()
