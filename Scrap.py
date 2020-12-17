# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:22:25 2020

@author: jackp
"""
import numpy as np
a = np.zeros((4,4),dtype ='int') # base layer
b = np.zeros((3,3),dtype ='int') # second layer
c = np.zeros((2,2),dtype ='int') # third layer
d = np.zeros(1,dtype ='int') # fourth layer

a2 = np.zeros((4,4),dtype ='int') # base layer
b2 = np.zeros((3,3),dtype ='int') # second layer
c2 = np.zeros((2,2),dtype ='int') # third layer
d2 = np.zeros(1,dtype ='int') # fourth layer

board1 = [a,b,c,d]
board2 = [a2,b2,c2,d2]

def print_board(a):
    
    '''Function to print the board off.'''
    
    print (a[0])
    print (a[1])
    print (a[2])
    print (a[3])
    return 


board1 [0][0][1] = 1

print("Board1:")
print_board(board1)
print("Board2:")
print_board(board2)

if board1 == board2:
    print ("Boards still match")