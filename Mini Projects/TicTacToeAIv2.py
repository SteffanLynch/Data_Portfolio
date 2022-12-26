#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 13:15:59 2021

@author: steffanlynch
"""

board = [' ' for x in range(10)]
# we are printing 10 spaces instead of 9 for ease of use.
# plauyer and computer will be choosing the position of the board to play based on the index
# if we use a range of 9, the index will be 0-8
# if we use a range of 10, we can ignore the first space and use indexes of 1-9 instead (which is more intuitive)

def insertLetter(letter, pos):
    board[pos] = letter

#returns a boolean value because of the comparison operator    
def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # Based on all the possible winning consecutive lines
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le))   # diagonal

def playerMove():
    run = True
    # We don't want to play the game unless the player inputs a valid position
    while run:
        move = input("Please select a position to place your 'X' (1-9): ")
        #exceptions and error handling
        #make sure they inpiut a correct value
        try:
            move = int(move) # make sure their input is an integer
            if move > 0 and move < 10: #ensure it is within the correct range
                if spaceIsFree(move): # make sure they move in empty space
                    run = False # loop ends because inputv is valid
                    insertLetter('X', move) # defined function for player to place their 'X'
                else:
                    print('Please select an empty space.')
            else:
                print('Please select a number in the range.')
        except:
            print('Please type a number!')
            
def compMove():
    #list of any empty square on the board
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    
    for let in ['O', 'X']: # loop through possible moves for both player and comp
        for i in possibleMoves:
            boardCopy = board[:] #copy original board
            boardCopy[i] = let # place letter into the indice of forf loop for available moves
            if isWinner(boardCopy, let):
                move = i
                return move
    # if no winning moves, we want to play in the corner        
    cornersOpen = [] # empty list of corners
    for i in possibleMoves:
        if i in [1, 3, 5, 7]: # cheking if any open spaces are corners
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    # then we want to play center if possible
    if 5 in possibleMoves:
        move = 5
        return move
    
    # finally we want to play any moves on the edges
    edgesOpen = [] # empty list of corners
    for i in possibleMoves:
        if i in [2, 4, 6, 8]: # cheking if any open spaces are corners
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    
    return move

def selectRandom(li):
    import random
    
    ln = len(li)
    r = random.randrange(0, ln)
    return (li[r])

#function that returns True if more than one positions is empty and False if not
#remember that we actually have 10 spaces, not 9. So there will always be one empty space
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
    
    # it might be simple but the aim is efficiency.
    # if you're going to reuse a block of code, then its best to define it 

def main():
    print('Welcome Message to player')
    printBoard(board)
    
    # Game continues while the board is not full. If is full, the game is a tie
    # As defined by the isBoardFull function
    while not(isBoardFull(board)):
        
        # Computer: 'O'. Player: 'X'
        # Checking that the computer hasn't already won; otherwise no point playing
        # So player moves ONLY if computer HAS NOT already won the game
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
           
        else:    # else means that the computer has not not won which means you have lost
            print('Sorry Buddy. You lost this time!')
            break    #the game is over and loop is broken
            
        # Checking that the you haven't already won
        # So computer moves if you HAVE NOT already won
        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0: # would mean that computer wasn't able to come up with a move
                print('Tie Game')
            else: 
                insertLetter('O', move)
                print("Computer place an 'O' in position", move, ": ")
                printBoard(board)
           
        else:    # else means that the player has not not won which means you have won
            print('Congratulations! You wont this game')
            break    #the game is over and loop is broken
    
    #if the board is full, the game is tie and the loop is broken
    if isBoardFull(board):
        print('The game is a tie')

main()5
        
               