import chess
import keras

from data_utils import *
from vector_utils import *

def create_model(data_filename="data/lichess_db_standard_rated_2016-06.pgn", scale=False, train=True, epochs=10, n_layers=10, n_neurons=10, lr=0.1, dropout=0.2):
    # We have to create the tensorflow session in here or the grid search will hang
    from keras.models import Sequential, load_model
    from keras.layers import Dense, Dropout, Flatten, LeakyReLU
    from keras.callbacks import EarlyStopping
    from keras import optimizers

    if (train):
        model = keras.models.Sequential()
        # model.add(keras.layers.LeakyReLU(alpha=0.3))
        # input layer
        model.add(Dense(100,activation='tanh', input_shape=(64,)))
        model.add(Dropout(dropout))

        #20 hidden layers
        for i in range(n_layers):
            model.add(Dense(n_neurons,activation='tanh'))
            model.add(Dropout(dropout))
        # output layer
        if(scale):
            model.add(Dense(4,activation='sigmoid'))
        else:
            model.add(Dense(4,activation='relu'))

        # optimizer
        opt_adam = optimizers.SGD(lr=0.1)
        model.compile(loss='mean_squared_error',optimizer=opt_adam,metrics=['accuracy'])
        model.summary()
    
        # save the weights to file
        model.save("chess_weights.h5")
    else:
        print("Loading weights")
        model = load_model("chess_weights.h5")
    return model