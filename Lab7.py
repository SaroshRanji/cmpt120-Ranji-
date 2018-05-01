# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Sarosh Ranji
# Created: 2018-03-30
symbol = [ " ", "x", "o" ] 
def printDivider():
    print("+--------------+")
def printRow(row):
    # initialize output to the left border
    # for each square in the row...
    # add to output the symbol for this square followed by a border
    # print the completed output for this row
    for i in range(3):
        print("|", end="")
        print(" " + symbol[board[row][i] + " ", end="")
        if board[row][i] == 0:
            print(" ", end="")
        elif board[row] [i] == 1:
            print(" X ", end="")
        else:
            print(" 0 ", end="")
    print("|")
def printBoard(board):
    # print the top border
    # for each row in the board...
    # print the row
    # print the next border
    for i in range(3):
        printDivider()
        printRow(i)
def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
    # if so, set it to the player number
    if board[row][col] == 0:
        board[row][col] = player
        return True
    return False # if no square is blank, return False
def getPlayerMove():
    row = int(input ("Enter the row number to play (0-2):"))
    col = int(input ("Enter the column number to play (0-2):"))
    return (row,col) # then return that row and column instead of (0,0)

def hasBlanks(board):
    # for each row in the board...
    # for each square in the row...
    # check whether the square is blank
    # if so, return True
    for i in range(3):
        for j in range(3):
            board[i] [j] == 0:
              return True
    return False #if no square is blank, return False


def gameOver(board):
    #check all the possiblilities looking for a win
    for i in range(3):
       if winRow(i,board):
           print("Player 1 wins!!!")
       elif winRow(i,board,2):
           print("Player 2 wins!!!")
              return
    for i in range(3):
        if winCol(i,board):
           print("Player 1 wins!!!")
       elif winCol(i,board,2):
           print("Player 2 wins!!!")
              return
    for i in range(3):
        if winDiag(i,board):
           print("Player 1 wins!!!")
       elif winDiag(i,board,2):
           print("Player 2 wins!!!")
              return

def winRow(row, board, player):
    for i in range(3):
        if board[row] [i] != player:
            return False
    return True

def winCol(Col, board, player):
    for i in range(3):
        if board[Col] [i] != player:
            return False
    return True
              
def winDiag(diag, board, player):
    for i in range(3):
        if board[diag] [i] != player:
            return False
    return True

def main():
    board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]  # TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board) and not gameOver(board):
        printBoard(board)
        row,col = getPlayerMove()
        if markBoard(board,row,col,player)
            player = player % 2 + 1 # switch player for next turn
        printBoard(board)
main()

