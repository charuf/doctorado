import numpy as np
import random 

def create_board():
    board = np.zeros((3,3), dtype=int)
    print(board)

#Function to place the player number (1 or 2) in the dired position)
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    print(board)

def possibilities(board):
    pos = list(zip(*np.where(board == 0)))
    print(pos)
    return pos

def random_place(board,possibilities,player):
    x = ()
    x = random.choice(possibilities(board))
    board[x] = player

def row_win(board,player):
    player_places = np.where(board == player)
    oc = 0
    for i in range(0,3):
        for n in player_places[0]:
            if n == i:
                oc +=1
        if oc == 3:
            return True
        oc = 0
    return False

def col_win(board,player):
    player_places = np.where(board == player)
    oc = 0
    for i in range(0,3):
        for n in player_places[1]:
            if n == i:
                oc +=1
        if oc == 3:
            return True
        oc = 0
    return False

def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        return True
        else: return False

def main():
    random.seed(1)
    player1 = 1
    player2 = 2
    possibilities = ()
    current_player = 0
    position = ()
    board = create_board()

    while (row_win(board,current_player) == False or col_win(board,current_player) == False or len(possibilities)!=0):
        if current_player == 1: current_player =2
        else: current_player == 1
        print(current_player)
        possibilities = possibilities(board)
        random_place(board,possibilities,current_player)
        print(board)

main()
