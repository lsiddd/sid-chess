#!/usr/bin/env python3
# coding: utf-8

import os
from time import sleep
import random
import argparse

from cairosvg import svg2png
# import chess.pgn
import numpy as np
import chess
import chess.pgn
import chess.svg

from telegram.error import NetworkError, Unauthorized

from telegram_bot import TelegramBot
from vector_utils import *
from move_generation import generate_legal_move
from neural_network import create_model

parser = argparse.ArgumentParser(description='Builds animation')
parser.add_argument('--scale',     type=bool, help='(bool) date like 2019-08-30',
  default=False)
parser.add_argument('--train',     type=bool, help='(bool) date like 2019-08-30',
  default=False)
parser.add_argument('--iterative',     type=bool, help='(bool) date like 2019-08-30',
  default=True)
parser.add_argument('--token',     type=str, help='(bool) date like 2019-08-30',
  default="")
parser.add_argument('--grid', type=str, default=False)
args = parser.parse_args()

scale = args.scale # scale the data between -1 and 1 or not
train = args.train #train new model, if false use saved one
iterative = args.iterative # play the user or itself
token = args.token

bot = TelegramBot(token)
chat_id = bot.chat_id

def game_loop(board, user_turn, model, mate=False):

    # check if game still exists
    if(not board.is_game_over()):
        # computer turn
        if( not user_turn):
            # gen move
            move = generate_legal_move(board, model, scale)
            # convert to Move() object
            move = chess.Move.from_uci(move)
            board.push(move)
            # switch user input
            if(iterative):
                user_turn = not user_turn
            
            generate_board_photo(board)
            bot.send_board()

        else:
            bot.send_message("Send your move in chess notation...")
            valid = False
    #         repeat until user plays a valid move
            while(not valid):
                try:
                    user_move = bot.get_user_move()
                    print(f"User {chat_id} move {user_move}")
                    board.push_san(user_move)
                    # node = node.add_variation(move)
                    user_turn = not user_turn
                    valid = True
                except ValueError:
                    bot.send_message("send a valid notation move")
    else:
        if not bot.notified_game_over:
            generate_board_photo(board)
            bot.send_board()
            bot.send_message("game over")
            bot.notified_game_over = True

    return user_turn

def generate_board_photo(board):
    svg_code = chess.svg.board(board=board)
    svg2png(bytestring=svg_code,write_to=f'boards/{chat_id}.png')

def create_game():

    board = chess.Board()
    user_turn = bool(random.getrandbits(1)) # random starting turn

    generate_board_photo(board)
    bot.send_board()

    bot.send_message("New game created")
    return board, user_turn

def main():
    # get the NN model
    model = create_model("data/lichess_db_standard_rated_2016-06.pgn", scale, train)

    board, user_turn = create_game()

    while True:
        try:
            # if user requests a new game
            if (bot.listen_for_command() == "/new"):
                bot.notified_game_over = False
                board, user_turn = create_game()
            user_turn =  game_loop(board, user_turn, model)
            sleep(1)
        except NetworkError:
            sleep(1)
            pass
        except Unauthorized:
            # The user has removed or blocked the bot.
            bot.update_id += 1

main()