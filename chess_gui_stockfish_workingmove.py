import tkinter as tk
import chess
import chess.engine
import csv
import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# --- Initialize CoppeliaSim connection ---
client = RemoteAPIClient()
sim = client.require('sim')
sim.startSimulation()
print("Connected to CoppeliaSim Chess!")

# --- Load square coordinates from CSV ---
square_coords = {}
with open('square_coords.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) >= 3:
            uci = row[0].strip().lower()
            try:
                x = float(row[1])
                y = float(row[2])
                square_coords[uci] = (x, y)
            except ValueError:
                continue

# --- Helper to find piece by position ---
def find_piece_at(x_target, y_target, tolerance=0.05):
    all_objects = sim.getObjectsInTree(sim.handle_scene, sim.object_shape_type)
    for handle in all_objects:
        name = sim.getObjectAlias(handle)
        pos = sim.getObjectPosition(handle, -1)
        if abs(pos[0] - x_target) < tolerance and abs(pos[1] - y_target) < tolerance:
            return handle, name
    return None, None

# --- GUI and Game Setup ---
board = chess.Board()

def apply_move(move_str):
    move_str = move_str.strip().lower()
    if len(move_str) != 4 or move_str[:2] not in square_coords or move_str[2:] not in square_coords:
        print("Invalid move:", move_str)
        return

    from_sq = move_str[:2]
    to_sq = move_str[2:]
    from_x, from_y = square_coords[from_sq]
    to_x, to_y = square_coords[to_sq]

    # Find the piece on the board at source
    handle, name = find_piece_at(from_x, from_y)
    if not handle:
        print(f"No piece found at {from_sq} ({from_x}, {from_y})")
        return

    current_z = sim.getObjectPosition(handle, -1)[2]
    sim.setObjectPosition(handle, -1, [to_x, to_y, current_z])
    print(f"Moved {name} from {from_sq} to {to_sq} → ({to_x}, {to_y})")

def make_ai_move():
    with chess.engine.SimpleEngine.popen_uci(r"C:\Users\dancr\stockfish\stockfish-windows-x86-64-avx2.exe") as engine:
        result = engine.play(board, chess.engine.Limit(time=0.1))
        move = result.move
        move_str = move.uci()
        print("AI move:", move_str)
        apply_move(move_str)
        board.push(move)
        move_text.insert(tk.END, f"Stockfish: {move_str}\n")

# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("CoppeliaSim Chess GUI")

move_text = tk.Text(root, height=10, width=40)
move_text.pack()

def on_submit():
    move_str = entry.get()
    try:
        move = chess.Move.from_uci(move_str)
        if move in board.legal_moves:
            board.push(move)
            apply_move(move_str)
            move_text.insert(tk.END, f"You: {move_str}\n")
            entry.delete(0, tk.END)
            root.after(500, make_ai_move)
        else:
            move_text.insert(tk.END, "Illegal move!\n")
    except Exception:
        move_text.insert(tk.END, "Invalid input!\n")

entry = tk.Entry(root)
entry.pack()

submit_btn = tk.Button(root, text="Make Move", command=on_submit)
submit_btn.pack()

root.mainloop()
sim.stopSimulation()
