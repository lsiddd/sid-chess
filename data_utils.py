import chess

from vector_utils import *
from engine_move import Engine

engine = Engine()

def extract_data(filename, from_csv=False):
    if not from_csv:
        positions = []
        moves = []
        with open(filename) as pgn:
            print("Oppened png...")
            print("Vectorizing")
            counter = 0
            while (game := chess.pgn.read_game(pgn)):
    #             let's not use unfinished games
    #             this messes with the endgame performance later on
                # if (game.headers["Termination"] == "Time forfeit" or
                #     int(game.headers["WhiteElo"]) < 2000 or int(game.headers["WhiteElo"]) < 2000):
                #     continue
                if (counter > 10000):
                    break
                # Iterate through all moves and play them on a board.
                board = game.board()
                for move in game.mainline_moves():
                    # positions.append(fen_to_vector(board.board_fen(), board.turn))
                    positions.append(fen_to_vector(board.mirror().board_fen()))

    #                 positions.append(board.turn)
                    eng_move = engine.get_move(board)
                    board.push(move)
                    moves.append(vector_mirror(move_to_vector(eng_move)))
                counter += 1
                print(f"Scanned {counter} games")

        np.savetxt("input.csv", positions, delimiter=",")
        np.savetxt("response.csv", moves, delimiter=",")
        return np.array(positions), np.array(moves)
    else:
        return np.genfromtxt("input.csv", delimiter=","), np.genfromtxt("response.csv", delimiter=",")
