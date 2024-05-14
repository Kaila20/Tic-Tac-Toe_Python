import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        # GUI window
        self.root = root
        self.root.title("Tic Tac Toe")
        # current player as 'X'
        self.current_player = 'X'
        # game board as a 3x3 grid of empty cells
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        #  2D array to hold the GUI buttons representing the game board
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        # Create the game board
        self.create_board()

    def create_board(self):
        # Create the GUI buttons for each cell in the game board
        for i in range(3):
            for j in range(3):
                # Define a button with a command that triggers handle_click when clicked
                button = tk.Button(self.root, text='', font=('Arial', 24), width=4, height=2,
                                   command=lambda row=i, col=j: self.handle_click(row, col))
                # Position the button in the GUI grid
                button.grid(row=i, column=j, padx=5, pady=5)
                # Add the button to the 2D array of buttons
                self.buttons[i][j] = button

    def handle_click(self, row, col):
        # Handle the click event on a button representing a cell in the game board
        if self.board[row][col] == ' ':
            # Update the game board and GUI with the current player's symbol ('X' or 'O')
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            # Check for win or tie conditions
            if self.check_for_win(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_for_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                # Switch to the next player's turn
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_for_win(self, row, col):
        # Check if the current player has won after making a move
        symbol = self.board[row][col]
        # Check row
        if all(cell == symbol for cell in self.board[row]):
            return True
        # Check column
        if all(self.board[i][col] == symbol for i in range(3)):
            return True
        # Check diagonals
        if (row == col and all(self.board[i][i] == symbol for i in range(3))) or \
           (row + col == 2 and all(self.board[i][2-i] == symbol for i in range(3))):
            return True
        return False

    def check_for_tie(self):
        # Check if the game is tied
        return all(cell != ' ' for row in self.board for cell in row)

    def reset_game(self):
        # Reset the game board and GUI to start a new game
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                # Reset the text of all buttons to empty
                self.buttons[i][j].config(text='')

# Create the Tkinter GUI window and start the game
root = tk.Tk()
app = TicTacToeGUI(root)
root.mainloop()
