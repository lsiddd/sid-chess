import chess
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, LeakyReLU
from keras.callbacks import EarlyStopping
from keras import optimizers

from data_utils import *
from vector_utils import *

def create_model(data_filename, scale, train=True):
    if (train):
        p, m = extract_data(data_filename)
        if (scale):
            # print("scaling the data...")
            p = p/6
            m = m/8
            print(p.shape)
            print(m.shape)

        model = keras.models.Sequential()
        # model.add(keras.layers.LeakyReLU(alpha=0.3))
        # input layer
        model.add(Dense(65,activation='tanh', input_shape=(65,)))
        model.add(Dropout(0.2))

        #20 hidden layers
        for i in range(4):
            model.add(Dense(1000,activation='tanh'))
            model.add(Dropout(0.2))
        # output layer
        if(scale):
            model.add(Dense(4,activation='sigmoid'))
        else:
            model.add(Dense(4,activation='relu'))

        # optimizer
        opt_adam = optimizers.SGD(lr=0.1)
        model.compile(loss='mean_squared_error',optimizer=opt_adam,metrics=['accuracy'])
        model.summary()
        # early stoppping at local minimums
        es = EarlyStopping(monitor='val_loss', mode='min')

        model.fit(p, m, epochs=30, batch_size=128, callbacks=[es], validation_split=0.1)

        # save the weights to file
        model.save("chess_weights.h5")
    else:
        print("Loading weights")
        model = load_model("chess_weights.h5")
    return model