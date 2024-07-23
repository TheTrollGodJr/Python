def getBoard(): # Get board information and return a 2d list

    # Open and read each line
    with open("server.txt", "r") as f:
        board = f.readlines()

    # Format board into a 2d list
    for i in range(len(board)):
        board[i] = board[i].split()
    return board

def placePiece(board, column=int, player=int):

    for i, row in enumerate(board):
        #print(row[column])
        if int(row[column]) != 0:
            board[i-1][column] = str(player)
        elif i == 5:
            board[i][column] = str(player)

    return board
'''
------------------------------
'''
def run():
    board = getBoard()
    column = int(input("Select a column between 1-7: "))
    board = placePiece(board, column-1, 2)
    file = open("server.txt", "w")
    for line in board:
        file.write(" ".join(line) + "\n")
    file.close()

if __name__ == "__main__":
    run()


    
    
    
    
    