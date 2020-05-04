import difflib
import random

import chess
import keras.models

from vector_utils import *

def generate_legal_move(board, model, scale):
    fen = board.board_fen()
    fen = fen_to_vector(fen, board.turn)
    fen = fen.reshape(1,65)
    # bring datat back to original scale
    if (scale):
        move = (model.predict(fen)[0] * 8).astype('int')
    else:
        move = (model.predict(fen)[0]).astype('int')
#     print(move)
    move = vector_to_move(move)
    
    legal = [move_.uci() for move_ in board.legal_moves]
#     print(legal)
    
#     print(move)
    move = difflib.get_close_matches(move, legal, n=3, cutoff=0)
#     print(move)
    return random.sample(move, 1)[0]
#     return move[0]
