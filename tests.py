from telegram_bot import TelegramBot
from vector_utils import *
from move_generation import generate_legal_move
from neural_network import create_model

print("testing move_to_vector: ", end='')
print("Passed" if 
	np.array_equal(move_to_vector("e2e4"), np.array([4, 1, 4, 3])) 
	else "Failed")

print("testing vector_to_move: ", end='')
print("Passed" if 
	"e2e4" == vector_to_move(np.array([4, 1, 4, 3]))
	else "Failed")

print("Test vector_mirror")
print("Passed" if 
	"e7e5" == vector_to_move(vector_mirror(move_to_vector("e2e4")))
	else "Failed")
