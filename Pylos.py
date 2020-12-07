# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:21:17 2020

@author: jackp
"""



import numpy as np

def random_move():
    
    '''Function to make a random move (it won't check if the move is legal). Will
    return a height, an x coordinate, and a y coordinate.'''
    
    height = np.random.randint(0,4) # draw a random number to select which layer (3 being top)
    x = np.random.randint(0,4-height) # select x position
    y = np.random.randint(0,4-height) # select y position
    
    return height,x,y

def ask_move():
    level = int(input("Please enter an integer value for the level you wish to move into. 0 being the base and 3 being the top."))
    row = int(input("Please enter an integer value for the row you wish to move into. Starting from 0."))
    column = int(input("Please enter an integer value for the column you wish to move into. Starting from 0."))
    return (level,row,column)


def get_move():
    
    ''' Function to ask user for move in proper format ie P 0,0,0 and convert to usable move. '''
    
    takein = input("Please enter the move in string format (ie P 0,0,0).")
    return takein


def print_board(a):
    
    '''Function to print the board off.'''
    
    print (a[0])
    print (a[1])
    print (a[2])
    print (a[3])
    return 

def change_board(move,board,player):
    
    '''Function to change the board (DOESN'T check if move is legal)'''
    
    if move[0] == 3:
        board [3][0] = player
    else:
        board [move[0]][move[1]][move[2]] = player
    return board

def availability_check(move,board):
    
    '''Function to check whether the space being moved into is empty and supported beneath.'''
    
    # special search for top piece
    if move [0] == 3:
        if board [3][0] != 0:
            return 0
        else:
            if 0 in (board [2][0][0],board [2][0][1],board [2][1][0],board [2][1][1]):
                return 0
            return 1
    
    elif board [move[0]][move[1]][move[2]] != 0: # is the space itself empty?
        return 0
    
    # now check for the third layer if the piece is supported
    elif move == (2,0,0):
        if 0 in (board [1][0][0],board [1][1][0],board [1][0][1],board [1][1][1]):
            return 0
    elif move == (2,1,0):
        if 0 in (board [1][2][0],board [1][1][0],board [1][2][1],board [1][1][1]):
            return 0
    elif move == (2,0,1):
        if 0 in (board [1][0][1],board [1][1][1],board [1][0][2],board [1][1][2]):
            return 0
    elif move == (2,1,1):
        if 0 in (board [1][1][1],board [1][2][1],board [1][1][2],board [1][2][2]):
            return 0
    
    # now check for the second layer if the piece is supported
    elif move == (1,0,0):
        if 0 in (board [0][0][0],board [0][1][0],board [0][0][1],board [0][1][1]):
            return 0
    elif move == (1,1,0):
        if 0 in (board [0][2][0],board [0][1][0],board [0][2][1],board [0][1][1]):
            return 0
    elif move == (1,0,1):
        if 0 in (board [0][0][1],board [0][1][1],board [0][0][2],board [0][1][2]):
            return 0
    elif move == (1,1,1):
        if 0 in (board [0][1][1],board [0][2][1],board [0][1][2],board [0][2][2]):
            return 0
    elif move == (1,2,0):
        if 0 in (board [0][2][0],board [0][3][0],board [0][2][1],board [0][3][1]):
            return 0
    elif move == (1,2,1):
        if 0 in (board [0][2][2],board [0][3][2],board [0][2][1],board [0][3][1]):
            return 0
    elif move == (1,2,2):
        if 0 in (board [0][2][2],board [0][3][2],board [0][2][3],board [0][3][3]):
            return 0
    elif move == (1,1,2):
        if 0 in (board [0][2][2],board [0][1][2],board [0][2][3],board [0][1][3]):
            return 0
    elif move == (1,0,2):
        if 0 in (board [0][0][2],board [0][1][2],board [0][0][3],board [0][1][3]):
            return 0
    
    # if has passed these then must be an available position
    else:
        return 1

def Loader(savefile):
    
    ''' A function to read a string of format "WB2EBW7EB2EW13E" and convert it into
        a playable board.'''
    
    a = np.zeros((4,4),dtype ='int') # base layer
    b = np.zeros((3,3),dtype ='int') # second layer
    c = np.zeros((2,2),dtype ='int') # third layer
    d = np.zeros(1,dtype ='int') # fourth layer
    
    board = [a,b,c,d]
    
    ia = [] # input as an array of strings and integers
    for i in range(len(savefile)):
        if savefile [i] != "W" and savefile [i] != "B" and savefile [i] != "E":
            ia.append (int(savefile[i]))
        else:
            ia.append (savefile[i])
    
    full_length_array = []
    
    
    position = 0
    
    while position < len(ia):
        ws = 0
        bs = 0
        es = 0
        
        if type(ia[position]) == int:
            if type(ia[position+1]) == int:
                if ia[position+2] == "W":
                    ws = 10*ia[position] + ia[position+1]
                elif ia[position+2] == "B":
                    bs = 10*ia[position] + ia[position+1]
                elif ia[position+2] == "E":
                    es = 10*ia[position] + ia[position+1]
                else:
                    print("My creator is a lazy shit and only bothered to make for a board with 4 levels")
                position = position + 3
            else:
                if ia[position+1] == "W":
                    ws = ia[position]
                elif ia[position+1] == "B":
                    bs = ia[position]
                elif ia[position+1] == "E":
                    es = ia[position]
                position = position + 2
        else:
            if ia[position] == "W":
                ws = 1
            elif ia[position] == "B":
                bs = 1
            elif ia[position] == "E":
                es = 1
            position = position + 1
        
        if ws != 0:    
            for _ in range(ws):
                full_length_array.append(1)
        elif bs != 0:    
            for _ in range(bs):
                full_length_array.append(2)
        elif es != 0:    
            for _ in range(es):
                full_length_array.append(0)
                
        
    
    print(full_length_array)
    
    board[0][0][0] = full_length_array [0]
    board[0][0][1] = full_length_array [1]
    board[0][0][2] = full_length_array [2]
    board[0][0][3] = full_length_array [3]
    board[0][1][0] = full_length_array [4]
    board[0][1][1] = full_length_array [5]
    board[0][1][2] = full_length_array [6]
    board[0][1][3] = full_length_array [7]
    board[0][2][0] = full_length_array [8]
    board[0][2][1] = full_length_array [9]
    board[0][2][2] = full_length_array [10]
    board[0][2][3] = full_length_array [11]
    board[0][3][0] = full_length_array [12]
    board[0][3][1] = full_length_array [13]
    board[0][3][2] = full_length_array [14]
    board[0][3][3] = full_length_array [15]
    board[1][0][0] = full_length_array [16]
    board[1][0][1] = full_length_array [17]
    board[1][0][2] = full_length_array [18]
    board[1][1][0] = full_length_array [19]
    board[1][1][1] = full_length_array [20]
    board[1][1][2] = full_length_array [21]
    board[1][2][0] = full_length_array [22]
    board[1][2][1] = full_length_array [23]
    board[1][2][2] = full_length_array [24]
    board[2][0][0] = full_length_array [25]
    board[2][0][1] = full_length_array [26]
    board[2][1][0] = full_length_array [27]
    board[2][1][1] = full_length_array [28]
    board[3][0] = full_length_array [29]
    
    print (board[0])
    print (board[1])
    print (board[2])
    print (board[3])

    return board

def place_interpretor(place):
    
    ''' Function to interpret an input of the format "P 0,0,0" and turn it into an array of 
        3 elements in the familiar format. '''
        
    move = (int(place[2]),int(place[4]),int(place[6]))
      
    
    return move




''' Start Board '''

a = np.zeros((4,4),dtype ='int') # base layer
b = np.zeros((3,3),dtype ='int') # second layer
c = np.zeros((2,2),dtype ='int') # third layer
d = np.zeros(1,dtype ='int') # fourth layer

board = [a,b,c,d]
print_board(board)

''' '''

print ("Human player goes first")
print()

legality = 0
while legality == 0:
    move = place_interpretor(get_move())
    print (move)
    print (type(move))
    legality = availability_check(move,board)
    if legality == 0:
        print ("Move illegal, please make another.")
board = change_board(move,board,1)
print_board (board)

legality = 0
while legality == 0:   
    move = random_move()
    legality = availability_check(move,board)
    

board = change_board(move,board,2)
print_board (board)

