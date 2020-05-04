import chess

from vector_utils import *

def extract_data(filename):
    positions = []
    moves = []
    with open(filename) as pgn:
        print("Oppened png...")
        print("Vectorizing")
        counter = 0
        while (game := chess.pgn.read_game(pgn)):
#             let's not use unfinished games
#             this messes with the endgame performance later on
            if (game.headers["Termination"] == "Time forfeit" or
                int(game.headers["WhiteElo"]) < 2000 or int(game.headers["WhiteElo"]) < 2000):
                continue
            # Iterate through all moves and play them on a board.
            board = game.board()
            for move in game.mainline_moves():
                positions.append(fen_to_vector(board.board_fen(), board.turn))
#                 positions.append(board.turn)
                board.push(move)                
                moves.append(move_to_vector(board))
                counter += 1
        print(f"Scanned {counter} games")
    return np.array(positions), np.array(moves)
