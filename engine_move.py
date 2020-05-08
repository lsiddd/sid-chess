import chess
import chess.engine
from datetime import datetime

class Engine:

    engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

    def get_move(self, board):

        result = self.engine.play(board, chess.engine.Limit(time=0.1))
        return result.move.uci()

