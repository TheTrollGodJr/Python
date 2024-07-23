import copy
import random

def write():
    with open("server.txt", "w") as f:
        f.write("0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n")

def getBoard(): # Get board information and return a 2d list

    # Open and read each line
    with open("server.txt", "r") as f:
        board = f.readlines()

    # Format board into a 2d list
    for i in range(len(board)):
        board[i] = board[i].split()
    
    return board

def isEmpty(board):
    empty = True
    for row in board:
        for column in row:
            if column != "0":
                empty = False
    
    return empty

def placePiece(board, column=int, player=int):

    for i, row in enumerate(board):
        #print(row[column])
        if int(row[column]) != 0:
            board[i-1][column] = str(player)
        elif i == 5:
            board[i][column] = str(player)

    return board

# Swaps rows and columns
# Effectively rotates the board 90 degrees counter-clockwise
def flipBoard(board):
    newBoard = [[],[],[],[],[],[],[]]
    for row in board:
        for i, column in enumerate(row):
            newBoard[i].append(column)
    return newBoard

def horizontalCheck(board):
    #print(board)
    redCount = 0
    yellowCount = 0
    for row in board:
        for i in range(len(row)):
            if row[i] == "1":
                yellowCount = 0
                redCount += 1
            elif row[i] == "2":
                redCount = 0
                yellowCount += 1
            elif row[i] == "0":
                redCount = 0
                yellowCount = 0

            if redCount == 4:
                return 1
            elif yellowCount == 4:
                return 2
            
def diagonalCheck(board):
    y = 0
    values = [0,0,0,0]
    for i in range(len(board)):
        try:
            for i in range(len(board[0])):
                values[0] = board[i + y][i]
                values[1] = board[i + y + 1][i + 1]
                values[2] = board[i + y + 2][i + 2]
                values[3] = board[i + y + 3][i + 3]

                if all(item == values[0] and int(item) > 0 for item in values):
                    return int(values[0])
        except:
            y += 1

    y = 0
    values = [0,0,0,0]
    for i in range(len(board)):
        try:
            for i in range(len(board[0])):
                values[0] = board[i + y][(i * -1) - 1]
                values[1] = board[i + y + 1][(i * -1) - 2]
                values[2] = board[i + y + 2][(i * -1) - 3]
                values[3] = board[i + y + 3][(i * -1) - 4]

                if all(item == values[0] and int(item) for item in values):
                    return int(values[0])
        except:
            y += 1

    return 0

# Returns 0 if no winner, 1 if red wins, and 2 if yellow wins
def checkBoard(board):

    # Check Horizonally
    horizontal = horizontalCheck(board)
    if horizontal == 1:
        return 1
    elif horizontal == 2:
        return 2
    
    vertical = horizontalCheck(flipBoard(board))
    if vertical == 1:
        return 1
    elif vertical == 2:
        return 2
    '''
    diagonal = diagonalCheck(board)
    if diagonal == 1:
        return 1
    elif diagonal == 2:
        return 2
    '''
    return 0
    
def horizontalCount(board, pieceRow, pieceColumn):
    redCount = 0
    values = []
    for i, column in enumerate(board[pieceRow]):
        #if i == pieceColumn:
        #    continue

        if column == "1":
            redCount += 1
        else:
            #if board[pieceRow][int(column) + 1] != "1":
            values.append(redCount)
            redCount = 0
    
    values.append(redCount)
    #print(values)
    
    return max(values)-1
                
# Returns the top piece of a selected column; 0 is the top, 5 is the bottom
def getY(board, x):
    y = 0
    for row in board:
        if row[x] == "0":
            y += 1
        else:
            return y
    return 5
    # flip the board then index until the new piece, return the index for a y

def printBoard(board):
    output = ""
    for row in board:
        for i, column in enumerate(row):
            if column == "0":
                if i == 6:
                    output += "⚫ \n"
                else:
                    output += "⚫ "

            elif column == "1":
                if i == 6:
                    output += "🔴 \n"
                else:
                    output += "🔴 "

            elif column == "2":
                if i == 6:
                    output += "🟡 \n"
                else:
                    output += "🟡 "
    return output

def genNewBoards(board):
    newboard = []
    for i in range(len(board[0])):
        newboard.append(placePiece(copy.deepcopy(board), i, 1))
    return newboard

def selectPiece(board):

    # If the board is empty, choose a random column and return it
    if isEmpty(board):
        return random.randint(0,6)
    
    weights = [0,0,0,0,0,0,0]
    newBoards = genNewBoards(board)

    #for i, currentBoard in enumerate(newBoards):
    #    if checkBoard(currentBoard) > 0:
    #        return i # what the crap does this mean
    
    for i, selectedBoard in enumerate(newBoards):
        currentBoardY = getY(selectedBoard, i)
        
        weightChange = horizontalCount(selectedBoard, currentBoardY, i)
        weightChange += horizontalCount(flipBoard(selectedBoard), i, currentBoardY)

        weights[i] += weightChange
    
    #print("\n\n", weights)
    
    return weights.index(max(weights))

def boardToString(board):
    rows = []
    for row in board:
        rows.append(" ".join(row))
    string = ""
    for item in rows:
        string += f"{item}\n"
    return string
    
def resetBoard():
    file = open("server.txt", "w")
    file.write("0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n") #Replace this String with whatever you want to start with in your "server.txt"
    file.close()

def run():
    board = getBoard()
    
    winner = checkBoard(board)
    if winner == 1:
        print("\nRed wins\n")
        resetBoard()
        return True
    elif winner == 2:
        print("\nYellow wins\n")
        resetBoard()
        return True
    
    selectedColumn = selectPiece(board)
    print(selectedColumn)
    
    board = placePiece(board, selectedColumn, 1)
    print(printBoard(board))
    
    winner = checkBoard(board)
    if winner == 1:
        print("\nRed wins\n")
        resetBoard()
        return True
    elif winner == 2:
        print("\nYellow wins\n")
        resetBoard()
        return True
    
    with open("server.txt", "w") as f:
        f.write(boardToString(board))
        
    return False
    #print(boardToString(board))

if __name__ == "__main__":
    run()
    
    #🔴🟡⚫
    