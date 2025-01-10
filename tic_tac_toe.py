class TicTacToe:
    def __init__(self):
        # Initialize the board and stacks for undo/redo
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.undo_stack = []  # Stack to track moves for undo
        self.redo_stack = []  # Stack to track moves for redo
        self.current_player = 'X'

    def print_board(self):
        # Display the current board state
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    
    def make_move(self, row, col):
        # Make a move if the cell is empty
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.undo_stack.append((row, col, self.current_player))  # Save move to undo stack
            self.redo_stack.clear()  # Clear redo stack as new move invalidates redo history
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Cell is already occupied. Try again.")

    def undo(self):
        # Undo the last move
        if self.undo_stack:
            row, col, player = self.undo_stack.pop()
            self.board[row][col] = ' '  # Remove the move
            self.redo_stack.append((row, col, player))  # Save the undone move to redo stack
            self.current_player = player
        else:
            print("No moves to undo.")

    def redo(self):
        # Redo the last undone move
        if self.redo_stack:
            row, col, player = self.redo_stack.pop()
            self.board[row][col] = player  # Reapply the move
            self.undo_stack.append((row, col, player))  # Save the move back to undo stack
            self.current_player = 'O' if player == 'X' else 'X'
        else:
            print("No moves to redo.")

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None

    def is_draw(self):
        # Check if the board is full and there's no winner
        return all(cell != ' ' for row in self.board for cell in row)

    def play(self):
        # Main game loop
        while True:
            self.print_board()
            winner = self.check_winner()
            if winner:
                print(f"Player {winner} wins!")
                break
            if self.is_draw():
                print("It's a draw!")
                break

            print(f"Player {self.current_player}'s turn.")
            print("Enter 'undo' to undo, 'redo' to redo, or provide row and column (0-2) to make a move.")
            command = input("Your move: ")

            if command.lower() == 'undo':
                self.undo()
            elif command.lower() == 'redo':
                self.redo()
            else:
                try:
                    row, col = map(int, command.split())
                    self.make_move(row, col)
                except (ValueError, IndexError):
                    print("Invalid input. Enter row and column as two numbers (e.g., '1 2').")

# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()

