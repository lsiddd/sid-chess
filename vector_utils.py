import numpy as np

alph = "abcdefgh" # letters for the chess files
file_corresp = {} #letter to number correspondence in board files
for i, v in enumerate(alph):
    file_corresp[v] = i

def fen_to_vector(fen):
    """FEN notation uses decribes the rows from 8th to 1st
       pieces are shown by their abbreviated names
       with uppercase letters for white pieces, and lowercase for black
       numbers represent a sequence of empty squares
       we make a substitution p -> 1, r->2, n->3, b->4, q->5, k->6
    """
    if (type(fen) is not str):
        raise ValueError
        
    fen = fen.replace("/", "")
    vec = []
    app = vec.append
    
    # app(turn)
    
    for i in fen:
        b = 1 #is black, 1 for white, -1 for back
        if(i.islower()):
            b = -1
        i = i.lower()
            
        if (i.isdecimal()):
            [app(0) for n in range(int(i))]
        elif (i == "p"):
            app(1 * b)
        elif (i == "r"):
            app(2 * b)
        elif (i == "n"):
            app(3 * b)
        elif (i == "b"):
            app(4 * b)
        elif (i == "q"):
            app(5 * b)
        elif (i == "k"):
            app(6 * b)
    return np.array(vec).astype("int16")



def move_to_vector(board):
    vec = []
    app = vec.append
    
    if (type(board) == str):
        last_move = board
    else:
        last_move = board.peek().uci()

    app(file_corresp[last_move[0]] + 1)
    app(int(last_move[1]))
    app(file_corresp[last_move[2]] + 1)
    app(int(last_move[3]))
    
    return (np.array(vec) - 1).astype("int16")

def vector_mirror(vec):
    # takes a move vector and replaces it by the mirrorred version of the move
    vec[1] = 7 - vec[1]
    vec[3] = 7 - vec[3]
    return vec


# In[5]:


def vector_to_move(vec):
    print(vec)
    move = []
    move.append(alph[vec[0]])
    move.append(vec[1] + 1)
    move.append(alph[vec[2]])
    move.append(vec[3] + 1)
    
    return "".join([str(i) for i in move])
