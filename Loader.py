# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:28:30 2020

@author: jackp
"""

import numpy as np

savefile = "WB2EBW7EB2EW13E"






'''
Reader
'''
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
board = Loader(savefile)




























