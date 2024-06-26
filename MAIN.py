import copy
import tkinter as tk
from SudokuGame import SudokuGame

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")

        self.difficulty_levels = {"Easy": 1, "Medium": 2, "Hard": 3, "Impossible": 4}

        self.game = SudokuGame()

        self.create_widgets()
        self.update_board()

        self.root.update_idletasks()
        width = self.root.winfo_reqwidth()
        height = self.root.winfo_reqheight()
        x = (self.root.winfo_screenwidth() - width) // 2
        y = (self.root.winfo_screenheight() - height) // 2
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        self.new_game()
        
        return

    def create_widgets(self):
        self.font = ("Arial", 20)

        self.board_frame = tk.Frame(self.root, bg="gray", padx=10, pady=10)
        self.board_frame.pack(padx=10, pady=10)

        self.reset_entries()

        self.button_frame = tk.Frame(self.root, bg="gray", padx=10, pady=10)
        self.button_frame.pack(padx=10, pady=10)

        solve_button = tk.Button(self.button_frame, text="Solve", command=self.solve_game, font=self.font, bg="green", fg="white")
        solve_button.pack(side=tk.LEFT, padx=5, pady=5)

        reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_game, font=self.font, bg="blue", fg="white")
        reset_button.pack(side=tk.LEFT, padx=5, pady=5)

        new_game_button = tk.Button(self.button_frame, text="New Game", command=self.new_game, font=self.font, bg="orange", fg="white")
        new_game_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        check_button = tk.Button(self.button_frame, text="Check", command=self.check_game, font=self.font, bg="purple", fg="white")
        check_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the difficulty dropdown
        self.difficulty_var = tk.StringVar(self.root)
        self.difficulty_var.set("Easy")
        difficulty_options = list(self.difficulty_levels)
        difficulty_dropdown = tk.OptionMenu(self.button_frame, self.difficulty_var, *difficulty_options)
        difficulty_dropdown.pack(side=tk.LEFT, padx=5, pady=5)

    def check_game(self):
        current_board = [[self.vars[i][j].get() for j in range(9)] for i in range(9)]
        solved_board = [[str(self.solved_board[i][j].value) for j in range(9)] for i in range(9)]

        if current_board == solved_board:
            popup = tk.Toplevel(self.root)
            popup.title("Congratulations!")
            label = tk.Label(popup, text="Vous avez résolu le sudoku", font=("Arial", 20))
            label.pack(padx=10, pady=10)
        else:
            popup = tk.Toplevel(self.root)
            popup.title("Try Again!")
            label = tk.Label(popup, text="Vous n'avez pas résolu le sudoku", font=("Arial", 20))
            label.pack(padx=10, pady=10)
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
                entry = tk.Entry(self.board_frame, width=2, font=("Arial", 35), justify="center", bg="white", textvariable=self.vars[i][j])
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.vars[i][j].trace("w", lambda *args, e=entry, x=j, y=i: self.on_entry_change(e, x, y, *args))
                row.append(entry)
            self.entries.append(row)
        
        return

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