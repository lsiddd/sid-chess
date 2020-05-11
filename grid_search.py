from sklearn.model_selection import GridSearchCV
# from keras.models import Sequential
# from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor

from neural_network import create_model
from data_utils import *

model = KerasRegressor(build_fn=create_model, verbose=0)

p, m = extract_data("data/lichess_db_standard_rated_2016-06.pgn", True)
# print("scaling the data...")
p = p/6
m = m/8
print(p.shape)
print(m.shape)

# batch_size = [10, 20, 100]
epochs = [10]
dropout_rate = [0.1, 0.2, 0.3]
n_neurons = [20, 50, 100, 300]
n_layers = [1, 3, 5, 10, 20]
lr = [0.01, 0.1, 0.8]
param_grid = dict(epochs=epochs, n_layers=n_layers, n_neurons=n_neurons, lr=lr, dropout=dropout_rate, )

grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=1, cv=3)

grid_result = grid.fit(p, m)

# summarize results
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))
