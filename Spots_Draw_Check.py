class TicTacToe:
    def __init__(self):
        self.spots = {i: str(i) for i in range(1, 10)}
        self.turn = 0

    def draw_board(self):
        board = (f"|{self.spots[1]}|{self.spots[2]}|{self.spots[3]}|\n"
                 f"|{self.spots[4]}|{self.spots[5]}|{self.spots[6]}|\n"
                 f"|{self.spots[7]}|{self.spots[8]}|{self.spots[9]}|")
        print(board)

    def check_turn(self):
        if self.turn % 2 == 0:
            return 'O'
        else:
            return 'X'

    def check_for_win(self):
        # Horizontal Cases
        if (self.spots[1] == self.spots[2] == self.spots[3]) \
                or (self.spots[4] == self.spots[5] == self.spots[6]) \
                or (self.spots[7] == self.spots[8] == self.spots[9]):
            return True
        # Vertical Cases
        elif (self.spots[1] == self.spots[4] == self.spots[7]) \
                or (self.spots[2] == self.spots[5] == self.spots[8]) \
                or (self.spots[3] == self.spots[6] == self.spots[9]):
            return True
        # Diagonal Cases
        elif (self.spots[1] == self.spots[5] == self.spots[9]) \
                or (self.spots[3] == self.spots[5] == self.spots[7]):
            return True
        else:
            return False

#Player turns (X and O)
    def play(self):
        while not self.check_for_win():
            self.draw_board()
            print(f"Player {self.check_turn()}'s turn")
            choice = int(input("Choose a spot: ")) #User input for choosing spot
            if self.spots[choice] != 'X' and self.spots[choice] != 'O': #If X or O is not there, then they will appear once user input, else they cannot if already there.
                self.spots[choice] = self.check_turn()
                self.turn += 1
            else:
                print("Spot already taken. Try again.")
        print("Game over!")
        self.draw_board()


game = TicTacToe() 
game.play()
