# AUTOGENERATED! DO NOT EDIT! File to edit: 02_engine_analysis.ipynb (unless otherwise specified).

__all__ = ['stockfish', 'evaluate_game']

# Cell
import chess.engine
import chess.pgn
import pandas as pd

# Cell
stockfish = "stockfish" # location of stockfish executable or alias

# Cell
def evaluate_game(game, engine, limit=chess.engine.Limit(time=.1)):
    board = game.board()
    moves = game.mainline_moves()
    evals = []
    for move in moves:
        board.push(move)
        info = engine.analyse(board, limit=limit)
        score = info["score"].pov(chess.WHITE).score()
        evals.append(score)
    return evals