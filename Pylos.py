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

def ask_move(): # REDUNDANT
    level = int(input("Please enter an integer value for the level you wish to move into. 0 being the base and 3 being the top."))
    row = int(input("Please enter an integer value for the row you wish to move into. Starting from 0."))
    column = int(input("Please enter an integer value for the column you wish to move into. Starting from 0."))
    return (level,row,column)


def get_move(): # REDUNDANT
    
    ''' Function to ask user for move in proper format ie P 0,0,0 and convert to usable move. '''
    Error = True
    while Error:
        takein = input("Please enter the move in string format (ie P 0,0,0).")
        
        if len(takein) == 7 and takein[3] == "," and takein[5] == "," and takein[0] in ("P","R"):
            Error = False
        else:
            print ()
            print ("There is something wrong with the format of your input, please try again")       
        
    
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

def implement_remove(move,board):
    
    '''Function to remove a piece from the board (DOESN'T check if move is legal)'''
    
    board [move[0]][move[1]][move[2]] = 0
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


def availability_check_remove(move,board,player):
    
    ''' Function to check whether a piece has something placed on it, and therefor whether it can physically
        be removed. '''
    
    if move == (0,0,0):
        if board [1][0][0] != 0:
            return 0
    elif move == (0,0,1):
        if board[1][0][0] == board[1][0][1] == 0:
            return 1
    elif move == (0,0,2):
        if board[1][0][2] == board[1][0][1] == 0:
            return 1
    elif move == (0,0,3):
        if board [1][0][2] != 0:
            return 0
    elif move == (0,1,0):
        if board[1][0][0] == board[1][1][0] == 0:
            return 1
    elif move == (0,2,0):
        if board[1][2][0] == board[1][1][0] == 0:
            return 1
    elif move == (0,3,0):
        if board [1][2][0] != 0:
            return 0
    elif move == (0,3,1):
        if board[1][2][0] == board[1][2][1] == 0:
            return 1
    elif move == (0,3,2):
        if board[1][2][2] == board[1][2][1] == 0:
            return 1
    elif move == (0,3,3):
        if board [1][2][2] != 0:
            return 0
    elif move == (0,1,3):
        if board[1][0][2] == board[1][1][2] == 0:
            return 1
    elif move == (0,2,3):
        if board[1][2][2] == board[1][1][2] == 0:
            return 1
    elif move == (0,1,1):
        if board[1][0][0] == board[1][1][0] == board[1][0][1] == board[1][1][1] == 0:
            return 1
    elif move == (0,1,2):
        if board[1][0][2] == board[1][1][2] == board[1][0][1] == board[1][1][1] == 0:
            return 1
    elif move == (0,2,2):
        if board[1][2][2] == board[1][1][2] == board[1][2][1] == board[1][1][1] == 0:
            return 1
    elif move == (0,2,1):
        if board[1][2][0] == board[1][1][0] == board[1][2][1] == board[1][1][1] == 0:
            return 1
    else:
        if board [move[0]][move[1]][move[2]] == player:
            return 1
        else:
            return 0


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

def place_remove_interpretor(place):
    
    ''' Function to interpret an input of the format "P 0,0,0" and turn it into an array of 
        3 elements in the familiar format. '''
      
    
    move = (int(place[2]),int(place[4]),int(place[6]))
    
    
    return move

def second_step_interpretor(string):
    
    ''' Function that interprets the second move a string of places and remove
        ie "P 0,0,0 R 0,0,0 R 0,0,1". '''
        
    move = (int(string[10]),int(string[12]),int(string[14]))
    return move

def third_step_interpretor(string):
    
    ''' Function that interprets the third move a string of places and remove
        ie "P 0,0,0 R 0,0,0 R 0,0,1". '''
        
    move = (int(string[18]),int(string[20]),int(string[22]))
    return move

def lift_remove_first_interpretor(string):
    
    ''' Function that interprets the first remove of a string of a lift that completes
        a line or square to facilitate one or two removals. '''
        
    move = (int(string[16]),int(string[18]),int(string[20]))
    return move

def lift_remove_second_interpretor(string):
    
    ''' Function that interprets the second remove of a string of a lift that completes
        a line or square to facilitate one or two removals. '''
        
    move = (int(string[24]),int(string[26]),int(string[28]))
    return move


def move_type(string):
    
    ''' Function to interpret difference between lifts, moves and removes when passed
        in string format. '''
    
    if len(string) == 7:
        return "Place"
    elif string[0] == "P" and string[8] == "R":
        if len(string) == 15:
            return "Place and remove one"
        elif len(string) == 23 and string[16] == "R":
            return "Place and remove two"
    elif string[0] == "L":
        if len(string) == 13:
            return "Lift"
        elif len(string) == 21:
            return "Lift and remove one"
        elif len(string) == 29:
            return "Lift and remove two"
    
    print ("Move type unknown")
    return "Unknown"

def lift_interpretor_implement(string,board,player):
    
    ''' Function to check lift legality and then subsequent implementation. '''
    
    removal = (int(string[2]),int(string[4]),int(string[6]))
    place = (int(string[8]),int(string[10]),int(string[12]))
    if availability_check_remove(removal,board) == 0:
        print ("Piece can't be lifted")
        return board
    else:
        board = implement_remove(removal,board)
        if availability_check(place,board) == 0:
            print ("Piece can't be placed here")
            board = change_board(removal,board,player)
            return (board)
        else:
            board = change_board(place,board,player)
            return board
        
def line_check(move,board,player):
    
    ''' THE MOVE HAS TO HAVE ALREADY BEEN IMPLEMENTED FOR THIS TO WORK! '''
    
    if move[0] not in (0,1):
        return 0
    
    # bottom layer horizontal lines
    if move in ((0,0,0),(0,0,1),(0,0,2),(0,0,3)):
        if board[0][0][0] == board[0][0][1] == board[0][0][2] == board[0][0][3] == player:
            return 1
    elif move in ((0,1,0),(0,1,1),(0,1,2),(0,1,3)):
        if board[0][1][0] == board[0][1][1] == board[0][1][2] == board[0][1][3] == player:
            return 1
    elif move in ((0,2,0),(0,2,1),(0,2,2),(0,2,3)):
        if board[0][2][0] == board[0][2][1] == board[0][2][2] == board[0][2][3] == player:
            return 1
    elif move in ((0,3,0),(0,3,1),(0,3,2),(0,3,3)):
        if board[0][3][0] == board[0][3][1] == board[0][3][2] == board[0][3][3] == player:
            return 1
    
    # bottom layer vertical lines
    if move in ((0,0,0),(0,1,0),(0,2,0),(0,3,0)):
        if board[0][0][0] == board[0][1][0] == board[0][2][0] == board[0][3][0] == player:
            return 1
    elif move in ((0,0,1),(0,1,1),(0,2,1),(0,3,1)):
        if board[0][0][1] == board[0][1][1] == board[0][2][1] == board[0][3][1] == player:
            return 1
    elif move in ((0,0,2),(0,1,2),(0,2,2),(0,3,2)):
        if board[0][0][2] == board[0][1][2] == board[0][2][2] == board[0][3][2] == player:
            return 1
    elif move in ((0,0,3),(0,1,3),(0,2,3),(0,3,3)):
        if board[0][0][3] == board[0][1][3] == board[0][2][3] == board[0][3][3] == player:
            return 1

    # second layer horizontal lines
    if move in ((1,0,0),(1,0,1),(1,0,2)):
        if board[1][0][0] == board[1][0][1] == board[1][0][2] == player:
            return 1
    elif move in ((1,1,0),(1,1,1),(1,1,2)):
        if board[1][1][0] == board[1][1][1] == board[1][1][2] == player:
            return 1
    elif move in ((1,2,0),(1,2,1),(1,2,2)):
        if board[1][2][0] == board[1][2][1] == board[1][2][2] == player:
            return 1
    
    # second layer vertical lines
    if move in ((1,0,0),(1,1,0),(1,2,0)):
        if board[1][0][0] == board[1][1][0] == board[1][2][0] == player:
            return 1
    elif move in ((1,0,1),(1,1,1),(1,2,1)):
        if board[1][0][1] == board[1][1][1] == board[1][2][1] == player:
            return 1
    elif move in ((1,0,2),(1,1,2),(1,2,2)):
        if board[1][0][2] == board[1][1][2] == board[1][2][2] == player:
            return 1
    
    return 0

def square_check(move,board,player):
    
    ''' MOVE MUST ALREADY BE IMPLEMENTED! '''
    
    # first layer
    if move[0] == 0:
        if move in ((0,0,0),(0,0,1),(0,1,0),(0,1,1)):
            if board[0][0][0] == board[0][0][1] == board[0][1][0] == board[0][1][1] == player:
                return 1
        if move in ((0,0,2),(0,0,1),(0,1,2),(0,1,1)):
            if board[0][0][2] == board[0][0][1] == board[0][1][2] == board[0][1][1] == player:
                return 1
        if move in ((0,0,2),(0,0,3),(0,1,2),(0,1,3)):
            if board[0][0][2] == board[0][0][3] == board[0][1][2] == board[0][1][3] == player:
                return 1
        if move in ((0,2,2),(0,2,3),(0,1,2),(0,1,3)):
            if board[0][2][2] == board[0][2][3] == board[0][1][2] == board[0][1][3] == player:
                return 1
        if move in ((0,2,2),(0,2,1),(0,1,2),(0,1,1)):
            if board[0][2][2] == board[0][2][1] == board[0][1][2] == board[0][1][1] == player:
                return 1
        if move in ((0,2,0),(0,2,1),(0,1,0),(0,1,1)):
            if board[0][2][0] == board[0][2][1] == board[0][1][0] == board[0][1][1] == player:
                return 1
        if move in ((0,2,0),(0,2,1),(0,3,0),(0,3,1)):
            if board[0][2][0] == board[0][2][1] == board[0][3][0] == board[0][3][1] == player:
                return 1
        if move in ((0,2,2),(0,2,1),(0,3,2),(0,3,1)):
            if board[0][2][2] == board[0][2][1] == board[0][3][2] == board[0][3][1] == player:
                return 1
        if move in ((0,2,2),(0,2,3),(0,3,2),(0,3,3)):
            if board[0][2][2] == board[0][2][3] == board[0][3][2] == board[0][3][3] == player:
                return 1
    
    # second and third layer
    else:
        if move in ((1,0,0),(1,0,1),(1,1,0),(1,1,1)):
            if board[1,0,0] == board[1][0][1] == board[1][1][0] == board[1][1][1] == player:
                return 1
        if move in ((1,0,2),(1,0,1),(1,1,2),(1,1,1)):
            if board[1,0,2] == board[1][0][1] == board[1][1][2] == board[1][1][1] == player:
                return 1
        if move in ((1,2,2),(1,2,1),(1,1,2),(1,1,1)):
            if board[1,2,2] == board[1][2][1] == board[1][1][2] == board[1][1][1] == player:
                return 1
        if move in ((1,2,0),(1,2,1),(1,1,0),(1,1,1)):
            if board[1,2,0] == board[1][2][1] == board[1][1][0] == board[1][1][1] == player:
                return 1
        if move in ((2,0,0),(2,0,1),(2,1,0),(2,1,1)):
            if board[2,0,0] == board[2][0][1] == board[2][1][0] == board[2][1][1] == player:
                return 1
    
    # if no conditions are met, then there has been no square formed
    return 0
        
def omni_evaluate(string,board,player):
    
    ''' Function to check ALL types of string input. SEPERATE FUNCTION THEN USED TO IMPLEMENT! '''
    
    if move_type(string) == "Place":
        move = place_remove_interpretor(string)
        if availability_check(move,board) == 0:
            return 0
        else:
            return 1
    elif move_type(string) == "Place and remove one":
        move1 = place_remove_interpretor(string)
        if availability_check(move1,board) == 0:
            return 0
        else:
            board = change_board(move1,board,player)
            if 1 in (line_check(move1,board,player),square_check(move1,board,player)):
                move2 = second_step_interpretor(string)
                if availability_check_remove(move2,board,player) == 0:
                    return 0
                else:
                    return 1
            else:
                print ("Have not completed square or line. Cannot remove pieces!")
                return 0
    elif move_type(string) == "Place and remove two":
        move1 = place_remove_interpretor(string)
        if availability_check(move1,board) == 0:
            print ("Place not available")
            return 0
        else:
            board = change_board(move1,board,player)
            if 1 in (line_check(move1,board,player),square_check(move1,board,player)):
                move2 = second_step_interpretor(string)
                if availability_check_remove(move2,board,player) == 0:
                    print ("First remove not avaiable")
                    return 0
                else:
                    board = implement_remove(move2,board)
                    move3 = third_step_interpretor(string)
                    if availability_check_remove(move3,board,player) == 0:
                        print ("Second remove not available")
                        return 0
                    else:
                        return 1
            else:
                print ("Have not completed square or line. Cannot remove pieces!")
                return 0
    elif move_type(string) == "Lift":
        if board == lift_interpretor_implement(string,board,player):
            return 0
        else:
            return 1
    elif move_type(string) == "Lift and remove one":
        place = (int(string[8]),int(string[10]),int(string[12]))
        if board == lift_interpretor_implement(string,board,player):
            return 0
        else:
            board = lift_interpretor_implement(string,board,player)
            if 1 in (line_check(place,board,player),square_check(place,board,player)):
                move1 = lift_remove_first_interpretor(string)
                if availability_check_remove(move1,board,player) == 0:
                    return 0
                else:
                    return 1
            else:
                print ("Did not complete square or line, cannnot remove")
                return 0
    elif move_type(string) == "Lift and remove two":
        place = (int(string[8]),int(string[10]),int(string[12]))
        if board == lift_interpretor_implement(string,board,player):
            return 0
        else:
            board = lift_interpretor_implement(string,board,player)
            if 1 in (line_check(place,board,player),square_check(place,board,player)):
                move1 = lift_remove_first_interpretor(string)
                if availability_check_remove(move1,board,player) == 0:
                    return 0
                else:
                    board = implement_remove(move1,board)
                    move2 = lift_remove_second_interpretor(string)
                    if availability_check_remove(move2,board,player) == 0:
                        return 0
                    else:
                        return 1
            else:
                print ("Did not complete square or line, cannnot remove")
                return 0
    else:
        print ("Omni_evaluate did not recognise move_type")
        return 0
                
def opponent_move(board):
    
    ''' Function to request, interpret, evaluate, and then implement the opponent's move. '''
    
    while True:
        string = input("Please enter move in string format.")
        if omni_evaluate(string,board,1) == 1:
            print ("Legal")
            break
        else:
            print ("Not legal")
    
    if move_type(string) == "Place":
        board = change_board(place_remove_interpretor(string),board,1)
    elif move_type(string) == "Place and remove one":
        board = change_board(place_remove_interpretor(string),board,1)
        board = implement_remove(second_step_interpretor(string),board)
    elif move_type(string) == "Place and remove two":
        board = change_board(place_remove_interpretor(string),board,1)
        board = implement_remove(second_step_interpretor(string),board)
        board = implement_remove(third_step_interpretor(string),board)
    elif move_type(string) == "Lift":
        board = lift_interpretor_implement(string,board,1)
    elif move_type(string) == "Lift and remove one":
        board = lift_interpretor_implement(string,board,1)
        board = implement_remove(lift_remove_first_interpretor(string),board)
    elif move_type(string) == "Lift and remove two":
        board = lift_interpretor_implement(string,board,1)
        board = implement_remove(lift_remove_first_interpretor(string),board)
        board = implement_remove(lift_remove_second_interpretor(string),board)
    
    return board

def count_pieces(board,number):
    count = np.count_nonzero(board[0]==number)
    count = count + np.count_nonzero(board[1]==number)
    count = count + np.count_nonzero(board[2]==number)
    count = count + np.count_nonzero(board[2]==number)
    return count


''' Start Board '''

a = np.zeros((4,4),dtype ='int') # base layer
b = np.zeros((3,3),dtype ='int') # second layer
c = np.zeros((2,2),dtype ='int') # third layer
d = np.zeros(1,dtype ='int') # fourth layer

board = [a,b,c,d]
print_board(board)

opponent_pieces = 15
computer_pieces = 15

''' '''

print ("Opponent goes first")
print()

while board[3][0] == 0:
    
    while count_pieces(board,1) < 15:
        board = opponent_move(board)
        print_board(board)
    
    while count_pieces(board,2) < 15:
        legality = 0
        while legality == 0:   
            move = random_move()
            legality = availability_check(move,board)
        
    
    board = change_board(move,board,2)
    print_board (board)

