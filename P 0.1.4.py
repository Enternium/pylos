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





''' Start Board '''

a = np.zeros((4,4),dtype ='int') # base layer
b = np.zeros((3,3),dtype ='int') # second layer
c = np.zeros((2,2),dtype ='int') # third layer
d = np.zeros(1,dtype ='int') # fourth layer

board = [a,b,c,d]
print_board(board)

''' '''

for i in range(5):

    legality = 0
    while legality == 0:   
        move = random_move()
        legality = availability_check(move,board)
        print (move)
    

    board = change_board(move,board,1)
    print_board (board)


'''
aa = int(input("level plz"))
bb = int(input("xplz"))
cc = int(input("yplz"))

move = (aa,bb,cc)

print (type(move[0]))

legality = availability_check(move,board)
if legality == 0:
    print ("Illegal")
elif legality == 1:
    print ("Legal")
else:
    print ("Yo you fuuuuucked up")
board = change_board(move,board)
print_board(board)
'''
