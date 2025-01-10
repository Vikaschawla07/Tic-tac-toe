# Tic-tac-toe

# Tic-Tac-Toe with Undo and Redo Functionality

A simple Python implementation of the classic Tic-Tac-Toe game with added **Undo** and **Redo** functionality using stack data structures. This project demonstrates how data structures like stacks can be applied to manage game states effectively.

---

## Features

- **Two-player gameplay**: Players alternate turns to place their mark (`X` or `O`) on a 3x3 grid.
- **Undo functionality**: Players can undo their last move.
- **Redo functionality**: Players can redo a previously undone move.
- **Winner detection**: Automatically checks for a winner after every move.
- **Draw detection**: Identifies when the game ends in a draw.
- **Interactive command-line interface**: Allows players to input moves, undo, and redo actions easily.

---

## Technologies Used

- **Programming Language**: Python
- **Data Structures**: Stacks for managing undo/redo functionality

---

## How to Run

### Prerequisites

- Python 3.6 or later installed on your machine.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe.git
   ```

2. Navigate to the project directory:
   ```bash
   cd tic-tac-toe
   ```

3. Run the game:
   ```bash
   python tic_tac_toe.py
   ```

---

## How to Play

1. The game starts with an empty 3x3 board.
2. Players take turns entering their moves by specifying the row and column indices (0, 1, or 2).
   - Example: `1 2` places the current player's mark in row 1, column 2.
3. Enter `undo` to undo the last move.
4. Enter `redo` to redo a previously undone move.
5. The game ends when:
   - A player gets three of their marks in a row (horizontally, vertically, or diagonally).
   - All cells are filled without a winner (resulting in a draw).

---

## Example Gameplay

```text
 | | 
-----
 | | 
-----
 | | 
Player X's turn.
Your move: 0 0

X| | 
-----
 | | 
-----
 | | 
Player O's turn.
Your move: 1 1

X| | 
-----
 |O| 
-----
 | | 
Player X's turn.
Your move: undo

Undo successful.

X| | 
-----
 | | 
-----
 | | 
Player O's turn.
```

---

## Project Structure

```text
.
├── tic_tac_toe.py      # Main game script
├── README.md           # Project documentation
```

---

## Future Improvements

- Add a graphical user interface (GUI) using libraries like Tkinter or Pygame.
- Implement AI for single-player mode using the Minimax algorithm.
- Support larger board sizes (e.g., 4x4 or 5x5).
- Save and load game states.

---

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

Inspired by the classic game of Tic-Tac-Toe and the practical applications of stack data structures.
