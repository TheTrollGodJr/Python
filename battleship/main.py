from tkinter import *
from tkinter import font
import tkinter as tk
import random
from PIL import Image, ImageTk
import time


def main():
    print("Starting...")
    ai_move()
    display()


white = "#FFFFFF"
red = "#A80B00"



def display():
    
    '''
    NOTES:
    - instead of having icon for ship just highlight squares: https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Battleship_game_board.svg/150px-Battleship_game_board.svg.png
    - create function inside of init() for placing pieces for each player before going on to the actual game
    - create button on right side of game to swap between views
    - create a button on the right side to submit your guess
        - when you click a square it should highlight it then save the coords into a variable
        - when the submit button is pressed it sends the saved coords into Jack's function
        
    - when viewing the recieving board/the board you place your pieces on, show ships as green
        - set each hit spot on the board as red -- including ship spots
    '''
    
    global currentScreen
    global placePieces
    global currentScreen
    global hoverCoords
    global pieces
    global pieceSelect
    global pieceRotation
    global running
    global tileList
    global placed_pieces
    global canPlace
    global placeSwapButton
    global redrawTiles
    
    hoverCoords = []
    tileList = []
    
    placePieces = True
    canPlace = True
    placeSwapButton = True
    redrawTiles = True
    
    #carrier is 5 long, battleship is 4 long, cruiser and submarine are 3, destroyer is 2
    pieces = [["5V", "5H"], ["4V", "4H"], ["3V", "3H"], ["3V", "3H"], ["2V", "2H"]] #number stands for length and letter is whether it should be vertical or horizontal
    placed_pieces = []
    
    pieceSelect = 0
    pieceRotation = 0 #0 to select vertical, 1 to selection horizontal
    currentScreen = 0 #0 - player 1 recieving, 1 - player 1 attacking, 2 - player 2 recieving, 3 - player 2 attacking
    
    def resetColor():
        global tileList
        #print(placed_pieces)
        for y, row in enumerate(tileList):
            for x, column in enumerate(row):
                if not((x, y) in placed_pieces):
                    #print(row, column)
                    column.recolor("#FFFFFF")
    
    class hoverButton(tk.Button):

        def __init__(self, master, coordinates, **kw):
            self.coords = coordinates
            tk.Button.__init__(self, master=master, **kw, bg="#FFFFFF", width=2, height=2, command=lambda: onAttack(self.coords))#lambda: shoot_action(coordinates))
            #self.defaultBackground = self["background"]
            self.bind("<Enter>", self.onEnter)
            self.bind("<Leave>", self.onLeave)
            self.color = "#FFFFFF"

        def onEnter(self, e):
            global placePieces
            global canPlace
            global pieceSelect
            global placed_pieces
            global currentScreen
            '''
            if self.color == "#FFFFFF": # White tiles
                self["activebackground"] = "#BABABA"
            #    self.config(bg="#BABABA")
            elif self.color == "#A80B00": # Red tiles
                self["activebackground"] = "#8F0C03"
            #    self.config(bg="#8F0C03")
            '''
            
            
            if placePieces:
                try:
                    self["activebackground"] = "#FFFFFF"
                    resetColor()
                    
                    if pieceSelect > 4:
                        global player1_board
                        global player2_board
                        showPopup()
                        pieceSelect = 0
                        if currentScreen == 0:
                            
                            for coords in placed_pieces:
                                player1_board[coords[0]][coords[1]] = 1
                            
                            placed_pieces = []
                            currentScreen = 2
                        else:
                            
                            for coords in placed_pieces:
                                player2_board[coords[0]][coords[1]] = 1
                            
                            placed_pieces = []
                            # Put code for starting the game after placing pieces
                            
                            placePieces = False
                            currentScreen = 0
                    
                    self["activebackground"] = "#98d984"
                    self.color == "#98d984"
                    if "V" in pieces[pieceSelect][pieceRotation]:
                        hoverCoords = [[self.coords[0], self.coords[1] + i] for i in range(int(pieces[pieceSelect][0][0]))]
                        for item in hoverCoords:
                            try:
                                canPlace = True
                                tileList[item[1]-1][item[0]-1].recolor("#98d984")
                                #tileList[item[1]-1][item[0]-1]["activebackground"] = "#aaaaaa"
                            except:
                                canPlace =  False
                                self["activebackground"] = "#FFFFFF"
                                resetColor()
                    else:
                        hoverCoords = [[self.coords[0] + i, self.coords[1]] for i in range(int(pieces[pieceSelect][0][0]))]
                        for item in hoverCoords:
                            try:
                                canPlace = True
                                tileList[item[1]-1][item[0]-1].recolor("#98d984")
                                #tileList[item[1]-1][item[0]-1]["activebackground"] = "#000000"
                            except:
                                canPlace = False
                                self["activebackground"] = "#FFFFFF"
                                resetColor()
                except:
                    pass
            else:
                pass
        
        def onLeave(self, e):
            global placePieces
            if placePieces:
                resetColor()
            
            
            #self["background"] = self.defaultBackground
            #if self.color == "#FFFFFF": # White tiles
            #    self.config(bg="#FFFFFF")
            #elif self.color == "#A80B00": # Red tiles
            #    self.config(bg="#A80B00")
        def recolor(self, color):
            self.config(bg=color)
            self.color = color

    root = tk.Tk()
    root.geometry("700x600")
    root.title("Battleship")
    
    def startScreen():
        global top
        top = root
        #top.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
        
        title = Label(top, text="Battleship", font=("Courier 10 Pitch", 25))
        title.place(x=220, y=80)
        
        def option(inp):
            global top
            if inp == 0:
                init()
                del top
                #controlScreen()
            elif inp == 1:
                print("AI Mode Not Avaliable")
        
        twoPlayerButton = Button(top, text="2-Player Mode", width=10, height=5, command=lambda: option(0), bg="#def5fc")
        twoPlayerButton.place(x=100, y=200)
        
        AIMode = Button(top, text="AI-Mode", width=10, height=5, command=lambda: option(1), bg="#def5fc")
        AIMode.place(x=430, y=200)
    
    startScreen()

    def onAttack(coords):
        global placePieces
        global placed_pieces
        global canPlace
        global pieceSelect
        if placePieces:
            if canPlace:
                inList = False
                selected = []
                if "V" in pieces[pieceSelect][pieceRotation]:
                    #print("adding pieces")
                    #hoverCoords = [[self.coords[0], self.coords[1] + i] for i in range(int(pieces[pieceSelect][0][0]))]
                    for i in range(int(pieces[pieceSelect][0][0])):
                        selected.append((coords[0] - 1, coords[1] + i - 1))
                        
                    #print(selected)
                    
                    for item in selected:
                        if item in placed_pieces: 
                            inList = True
                            break
                    
                    if not(inList):
                        for i in range(int(pieces[pieceSelect][0][0])):
                            placed_pieces.append((coords[0] - 1, coords[1] + i - 1))
                    #print(placed_pieces)
                        pieceSelect += 1
                else:
                    for i in range(int(pieces[pieceSelect][0][0])):
                        selected.append((coords[0] + i - 1, coords[1] - 1))
                        
                    for item in selected:
                        if item in placed_pieces: 
                            inList = True
                            break
                    
                    if not(inList):
                        for i in range(int(pieces[pieceSelect][0][0])):
                            #
                            # I changed this part but didn't finish it 
                            #
                            player1_board[coords[0]+i-1][coords[1]] = i+1
                            #placed_pieces.append((coords[0] + i - 1, coords[1] - 1))
                        pieceSelect += 1
            
        else:
            global currentScreen
            #print(currentScreen)
            if currentScreen == 1:
                currentScreen = 3
                showPopup()
            elif currentScreen == 3:
                currentScreen = 1
                showPopup()
            
    
    def showPopup():
        global popup
        popup = tk.Toplevel(root)
        #popup.wm_attributes('-fullscreen', True)
        popup.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
        #popup.configure()
        
        def popupClick(button, popup):
            #global button
            button.destroy()
            popup.destroy()
            resetColor()
        
        button = Button(popup, text="Click To Continue", command=lambda: popupClick(button, popup), width=72, height=33)
        button.place(x=10, y=10)
    
    player = Label(root, text="Player-1", font=("Ariel", 15), fg="#8ec1d1")
    frame = ImageTk.PhotoImage(Image.open("battleship/frame.png"))
    frameLabel = Label(root, image=frame)
    
    popup = tk.Toplevel(root)
    #popup.wm_attributes('-fullscreen', True)
    popup.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
    
    button = Button(popup, text="Click To Continue", command=lambda: popupClick(button, popup), width=72, height=33)
    button.place(x=10, y=10)
    
    def rotatePiece():
        global pieceRotation
        if pieceRotation == 0:
            pieceRotation = 1
        else:
            pieceRotation = 0
    
    rotateButton = Button(root, text="Rotate Piece", command=rotatePiece)
    
    def init():
        global tileList
        
        player.place(x=595,y=10)
        frameLabel.place(x=55, y=50)
        
        if placePieces:
            rotateButton.place(x=570, y=100)
        
        # Set up the letters to iterate through
        numberRows = [[Label(root, text=i+1, font=("Courier 10 Pitch", 22))] for i in range(10)]
        letterRows = [[Label(root, text=chr(65 + i), font=("Courier 10 Pitch", 22))] for i in range(10)]
        
        tileList = [[hoverButton(root, coordinates=(x+1, y+1), text="") for x in range(10)] for y in range(10)]
        
        y = 60
        # Place down all the letters
        for items in letterRows:
            for item in items:
                #if item.cget('text') == "I":
                #    item.config(text=" I")
                item.place(x=20, y=y)
                y += 50
        
        x = 73
        # Place down all the numbers
        for items in numberRows:
            for item in items:
                if item.cget('text') == 10:
                    item.place(x=x-10, y=10); continue
                item.place(x=x, y=10)
                x += 50
        # Set up the letters to iterate through
        
        '''
        y=53
        # Place down all the squares
        for row in tileList:
            x=58
            for column in row:
                column.place(x=x, y=y)
                x += 50
            y += 50
        tileList[0][0].recolor("#A80B00")
        print(tileList[0][0].color)
    '''
    
    def controlScreen():
        global placePieces
        global placeSwapButton
        global player2_pieces
        global redrawTiles
        
        #resetColor()
        
        if not(placePieces) and placeSwapButton:
            placeSwapButton = False
            rotateButton.destroy()
            swapButton = Button(root, text="Swap  Board\nView", command=swap)#, font=("Ariel, 8"))
            swapButton.place(x=570, y=100)
            
        
        #global player
        if currentScreen < 2:
            player.config(text="Player-1")
            #hoverBlock = canvas.create_rectangle(0, 0, 500, 500, fill="#def5fc")
            
            if not(placePieces) and currentScreen == 0:
                #print("loop")
                
                for y in range(10):
                    for x in range(10):
                        if player1_board[x][y] == 1:
                            tileList[y][x].config(bg="#98d984")
                        #print("changed")
            #print("change 0")
        else:
            player.config(text="Player-2")
            #print("change 1")
            if not(placePieces):
                for y in range(10):
                    for x in range(10):
                        if player2_board[x][y] == 1:
                            tileList[y][x].config(bg="#98d984")
            
        root.after(100, controlScreen)
    
    def swap():
        global currentScreen
        resetColor()
        time.sleep(1)
        
        if currentScreen == 0: currentScreen = 1
        elif currentScreen == 1: currentScreen = 0
        elif currentScreen == 2: currentScreen = 3
        elif currentScreen == 3: currentScreen = 2
        
    
    
    #controlScreen()
    
    #popup = Button(tp, text="Click To Continue", font=("Courier 10 Pitch", 30), width=700, height=600, command=popupClick)
    #popup.place(x=100, y=100)
    
    root.mainloop()



def ai_move(): # player2 is the ai.
    initial = (random.randint(0, 9), random.randint(0, 9))
    #if 
    print("Move AI")

def ai_ships():
    pass



def shoot_action(coordinates, player):
    if player1_board[coordinates[0]][coordinates[1]] == 1:
        return True
    else:
        return False




if __name__ == "__main__":
    #[[(1,1),(1,2)], []]
    # Both list will end up having a lot of tuples giving coordinates on the board
    '''
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    carrier is 1 (5 long), battleship is 2 (3 long), cruiser is 3 (3 long), submarine is 4 (3 long), destroyer is 5 (2 long)
    '''
    player1_board = [[0 for i in range(10)] for i in range(10)] # The less dumb one
    player2_board = [[0 for i in range(10)] for i in range(10)]
    player1_guesses = []
    #player2_pieces = []
    player2_guesses = []
    main()


