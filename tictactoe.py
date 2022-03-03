"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    S = board
    x_count = 0
    o_count = 0
    for row in S:
        x_count += row.count("X")
        o_count += row.count("O")

    if x_count == o_count:
        return X
    else:
        return O
    """
    Returns player who has the next turn on a board.
    """
    #raise NotImplementedError


def actions(board):
    S = board
    actions_array = []

    for i in range(3):
        for j in range(3):
            if S[i][j] == None:
                actions_array.append((i,j))

    return actions_array
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError


def result(board, action):

    S2 = []
    for row in board:
        S2.append(row.copy())
    i,j = action
    S2[i][j] = player(S2)
    return S2
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    result = utility(board)
    if result == -1:
        return "O"
    elif result == 1:
        return "X"
    else:
        return None
    #raise NotImplementedError


def terminal(board):
    S = board
    blank_count = 0
    for i in range(len(S)):
        blank_count += S[i].count(None)

        if S[i] == ["X","X","X"] or [S[0][i],S[1][i],S[2][i]] == ["X","X","X"] or [S[0][0],S[1][1],S[2][2]] == ["X","X","X"] or [S[2][0],S[1][1],S[0][2]] == ["X","X","X"]:
            return True
        elif S[i] == ["O","O","O"] or [S[0][i],S[1][i],S[2][i]] == ["O","O","O"]  or [S[0][0],S[1][1],S[2][2]] == ["O","O","O"] or [S[2][0],S[1][1],S[0][2]] == ["O","O","O"]:
            return True

    if blank_count == 0:
        return True
    else:
        return False
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError


def utility(board):
    S = board
    blank_count = 0
    for i in range(len(S)):
        blank_count += S[i].count(None)

        if S[i] == ["X","X","X"] or [S[0][i],S[1][i],S[2][i]] == ["X","X","X"] or [S[0][0],S[1][1],S[2][2]] == ["X","X","X"] or [S[2][0],S[1][1],S[0][2]] == ["X","X","X"]:
            return 1
        elif S[i] == ["O","O","O"] or [S[0][i],S[1][i],S[2][i]] == ["O","O","O"]  or [S[0][0],S[1][1],S[2][2]] == ["O","O","O"] or [S[2][0],S[1][1],S[0][2]] == ["O","O","O"]:
            return -1

    if blank_count == 0:
        return 0
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """


def minimax(board):
    S = board

    def max_val(S,V):
        if terminal(S):
            return utility(S),(0,0)
        v = float("-inf")
        #V = float("-inf")
        for action in actions(S):
            val,temp = min_val(result(S,action),float("-inf"))
            if val > v:
                v = val
                result_action = action

            if v > V:
                return v,result_action
            else:
                V = v


        #result_action is only relevant when the max_val is the first function called
        return v,result_action

    def min_val(S,V):
        if terminal(S):
            return utility(S),(0,0)
        v = float("inf")

        for action in actions(S):
            val,temp = max_val(result(S,action),float("inf"))
            if val < v:
                v = val
                result_action = action

            if v < V:
                return v,result_action
            else:
                V = v

        #result_action is only relevant when the min_val is the first function called
        return v,result_action


    if player(S) == "O":
        val,ai_action = min_val(S,float("-inf"))
    else:
        val,ai_action = max_val(S,float("inf"))

    return ai_action
