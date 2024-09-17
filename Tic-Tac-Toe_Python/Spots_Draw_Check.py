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
        return 'O' if self.turn % 2 == 0 else 'X'

    def check_for_win(self):
        winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical
            [1, 5, 9], [3, 5, 7]              # Diagonal
        ]
        for combo in winning_combinations:
            if self.spots[combo[0]] == self.spots[combo[1]] == self.spots[combo[2]]:
                return True
        return False

    def play(self):
        while not self.check_for_win():
            self.draw_board()
            print(f"Player {self.check_turn()}'s turn")
            choice = int(input("Choose a spot: "))
            if choice in range(1, 10) and self.spots[choice] not in ['X', 'O']:
                self.spots[choice] = self.check_turn()
                self.turn += 1
            else:
                print("Invalid choice. Try again.")
        print("Game over!")
        self.draw_board()

game = TicTacToe()
game.play()
