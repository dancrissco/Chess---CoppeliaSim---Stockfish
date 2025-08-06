# Chess---CoppeliaSim---Stockfish
Simulation of a Chess Game in Coppeliasim with Stockfish
# CoppeliaSim Chess with Stockfish Integration ♟️

This project is an interactive chess simulation that combines the power of the **Stockfish** chess engine with **CoppeliaSim** for real-time visualization of chess piece movements. It supports human vs. AI play using UCI-formatted moves and displays each move visually on a virtual 3D chessboard.

---

## ✨ Features

- 🧠 **Stockfish Integration** – powerful chess engine that responds to your moves.
- ♟️ **Real-Time Chess Simulation** – each move updates the board in CoppeliaSim.
- 🖥️ **Tkinter GUI** – simple and effective interface to enter moves and view logs.
- 👁️ **Visual Feedback** – clear move logs to follow game progress.
- 🧪 **Tested Functionality** – supports pawn promotion, capture, and error handling.

---

## 📁 Folder Structure

chess_project/
│
├── chess_stockfish_gui.py # Main Python script with GUI and CoppeliaSim logic
├── README.md # Project documentation
└── ...

markdown
Copy
Edit

---

## 🧰 Requirements

- **Python 3.8+**
- **CoppeliaSim** installed and running (with Remote API enabled)
- **Stockfish Engine** (ensure the `stockfish` binary is in your system PATH)
- **Required Python libraries**:
  - `python-chess`
  - `tkinter` (usually comes with Python)
  - `zmq` for CoppeliaSim remote API

Install Python dependencies with:

```bash
pip install python-chess pyzmq
▶️ How to Run
Start CoppeliaSim and load the chess scene.

Ensure the chess pieces are named according to the script (e.g., pawn_white_0, rook_black_1, etc.).

Run the Python script:

bash
Copy
Edit
python chess_stockfish_gui.py
The GUI will open. Enter your move using UCI format (e.g., e2e4) and click Make Move.

Watch the move update in CoppeliaSim. The AI will automatically respond.

♖ Piece Naming Convention in CoppeliaSim
Make sure the pieces in CoppeliaSim follow the expected naming format:

White pawns: pawn_white_0 to pawn_white_7

Black pawns: pawn_black_0 to pawn_black_7

Rooks: rook_white_0, rook_white_1, rook_black_0, rook_black_1

Knights, Bishops, King, Queen: Named similarly (e.g., queen_white, king_black, etc.)

📌 Notes
Captured piece handling will be implemented in a future version.

Voice input and drone-based interaction are part of future expansions.

For troubleshooting, check for errors like:

object does not exist – check piece names in CoppeliaSim

stockfish not found – ensure it's in system PATH

📸 Screenshots


🧠 Future Enhancements
Piece capture animations

Voice command input (e.g., "move knight to F3")

Drone-assisted piece movement

🤝 Contributors
Daniel Christadoss – Project Lead & Developer

📜 License
MIT License – feel free to use and adapt!

♟️ Enjoy the game!
Start playing and watch your moves come to life in a 3D simulation!
