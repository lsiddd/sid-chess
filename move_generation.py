import difflib
import random

import chess
import keras.models

from vector_utils import *

def generate_legal_move(board, model, scale):
    # fen = board.board_fen()
    # fen = fen_to_vector(fen, board.turn)
    # fen = fen_to_vector(fen)
    # fen = fen.reshape(1,64)
    # receive the fen and mirror it for the prediction
    fen_mirror = fen_to_vector(board.mirror().board_fen())
    fen_mirror = fen_mirror.reshape(1,64)
    # bring datat back to original scale
    if (scale):
        move = np.round(model.predict(fen_mirror)[0] * 8).astype("int")
    else:
        move = np.round(model.predict(fen_mirror)[0]).astype("int")
#     print(move)

    # remove mirroring and convert to uci
    move = vector_mirror(move)
    move = vector_to_move(move)
    
    # get legal closest move to prediction
    legal = [move_.uci() for move_ in board.legal_moves]
#     print(legal)
    
#     print(move)
    move = difflib.get_close_matches(move, legal, n=3, cutoff=0)
#     print(move)
    # return random.sample(move, 1)[0]
    return move[0]
