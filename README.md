# Sid-chess - deep learning-base chess bot

Sid-chess is a telegram bot/chess engine trained with lichess' gama database. You can play the bot on the @sidchess_bot user on telegram. **It's not very good, but it's learning, don't preassure it!**

All users need to do is to reply with the board picture with theis move in Standard Algebraic Notation (SAN).

### SAN examples:

* e5 -- move the e-pawn to the e5 square
* Rd1 -- Rook to the d1 square
* Be7 -- Bishop to e7
* Nf6 -- Knight to f6
* Kd1 -- King d1
* Qf6 -- Queen to f6
* exd5 -- e-pawn capture piece on the d5 square

Sid-chess uses a NN model trained on keras using the games from string players (>2000 rating) on lichess' database. Currently the model is trained over 1.000.000 games, and counting. The game logic (i.e. the legal moves evaluation), and rendering use the python-chess library.

# Using 

Install dependencies with:

`pip3 install -t requirements`

You can run sid-chess on your own by executing:

`python3 main.py --token='your_bot_token' --train=False --scale=False --iterative=True`

The parameters `train`, `scale`, and `iterative` aren't really useful if you just need to run the bot, you can ommit them.

# Contributing

Pull requests are welcomed, a guide on how to contribute with games and CPU-time will be available soon.