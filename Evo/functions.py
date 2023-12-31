import random
from colorama import init
from termcolor import colored, cprint
import time

#vars
cmdX = 236
cmdY = 57

#world actions
def generateNewGenome(minConnectPerIn, maxConnectPerIn):
    if maxConnectPerIn > 5:
        print("Error:\nToo many genome Connections")
        exit(1)
    inputs = ["f", "p", "w", "n"]
    outputs = ["u", "d", "l", "r", "e"]
    genome = []
    for items in inputs:
        genomeSection = ""
        connections = random.randint(minConnectPerIn, maxConnectPerIn)
        for i in range(connections):
            out = random.choice(outputs)
            while out in genomeSection:
                out = random.choice(outputs)
            genomeSection = f"{genomeSection}{out}"
        genomeSection = "".join(genomeSection)
        genome.append([f"{items}", genomeSection])
    print(genome)
    return genome

def makeGenomeList(playerAmount, newGenome):
    if newGenome:
        genomeList = []
        for i in range(playerAmount):
            genomeList.append(generateNewGenome(0,5))
        return genomeList
    else:
        return []

def runCommands(string):
    pass

def update(genomeList, foodList, playerList):
    playerListCount = 0
    for genomes in genomeList:
        for genomeParts in genomes:
            if genomeParts[0][0] == "f":
                if foodNear(playerList, foodList):
                    runCommands(genomeParts[0][1])
            if genomeParts[1][0] == "p":
                if playerNear(playerList[playerListCount], playerList):
                    runCommands(genomeParts[1][1])
        playerListCount += 1


def distributeFood(amount):
    foodList = []
    for i in range(amount):
        while True:
            x = random.randint(1, cmdX)
            y = random.randint(1, cmdY)
            foodArray = [x, y]

            addArray = True
            for i in range(len(foodList)):
                if foodList[i] == foodArray:
                    addArray = False
            
            if addArray:
                break

        foodList.append(foodArray)
    
    return foodList

def distributePlayers(amount, foodList):
    playerList = []
    for i in range(amount):
        while True:
            x = random.randint(1, cmdX)
            y = random.randint(1, cmdY)
            playerArray = [x, y]

            addArray = True
            for i in range(len(playerList)):
                if playerList[i] == playerArray:
                    addArray = False
                else:
                    for items in foodList:
                        if items == playerArray:
                            addArray = False
                
            if addArray:
                break
        
        playerArray.append(0)
        playerList.append(playerArray)
    
    return playerList

def generateWorld(foodAmount, playerAmount, newGenomes):
    foodList = distributeFood(foodAmount)    
    playerList = distributePlayers(playerAmount, foodList)
    genomeList = makeGenomeList(playerAmount, newGenomes)
    return foodList, playerList, genomeList

def showWorld(food, players):#, player, walls):
    foodFound = False
    for i in range(cmdY):
        string = ""
        for ii in range(cmdX):
            for items in food:
                if items[0] == ii + 1:
                    if items[1] == i + 1:
                        string = string + "X"#colored('X', 'green')
                        foodFound = True
            for items in players:
                if foodFound == True:
                    foodFound = False
                    break
                if items[0] == ii + 1:
                    if items[1] == i + 1:
                        string = string + "0"
            
            if len(string) != cmdX:
                string = string + " "
                
        print(string)
    time.sleep(1)

def getFood(player, food):
    sideCoords = [[player[0] -1, player[1]], [player[0] + 1, player[1]], [player[0], player[1] - 1], [player[0], player[1] + 1]]
    foundItems = []
    for coords in sideCoords:
        for items in food:
            if items == coords:
                foundItems.append(coords)
    return foundItems

def getPlayers(player, playerList):
    sideCoords = [[player[0] -1, player[1]], [player[0] + 1, player[1]], [player[0], player[1] - 1], [player[0], player[1] + 1]]
    foundItems = []
    for coords in sideCoords:
        for items in playerList:
            if items != player:
                if items == coords:
                    foundItems.append(coords)
    return foundItems

#test if there is a player where the current player is trying to move
def playerAt(player, playerList, dir):
    if dir == "r":
        player = [player[0] + 1, player[1]]
        for items in playerList:
            if items == player:
                return True
    elif dir == "l":
        player = [player[0] - 1, player[1]]
        for items in playerList:
            if items == player:
                return True
    elif dir == "u":
        player = [player[0], player[1] - 1]
        for items in playerList:
            if items == player:
                return True
    elif dir == "d":
        player = [player[0], player[1] + 1]
        for items in playerList:
            if items == player:
                return True
    else:
        return False

#inputs
def foodNear(player, food):
    sideCoords = [[player[0] -1, player[1]], [player[0] + 1, player[1]], [player[0], player[1] - 1], [player[0], player[1] + 1]]
    for coords in sideCoords:
        for items in food:
            if items == coords:
                return True
    return False

def playerNear(player, playerList):
    sideCoords = [[player[0] -1, player[1]], [player[0] + 1, player[1]], [player[0], player[1] - 1], [player[0], player[1] + 1]]
    for coords in sideCoords:
        for items in playerList:
            if items != player:
                if items == coords:
                    return True
    return False


def wallNear():
    pass

def noOptions(player, food, playerList):
    if foodNear(player, food) == False:
        if playerNear(player, playerList) == False:
            return True
    return False

#actions
def moveR(player, playerList):
    if player[0] != cmdX:
        if playerAt(player, playerList, "r") == False:
            player[0] += 1
    return player

def moveL(player, playerList):
    if player[0] != 1:
        if playerAt(player, playerList, "l") == False:
            player[0] -= 1
    return player

def moveU(player, playerList):
    if player[1] != 1:
        if playerAt(player, playerList, "u") == False:
            player[1] -= 1
    return player

def moveD(player, playerList):
    if player[1] != cmdY:
        if playerAt(player, playerList, "d") == False:
            player[1] -= 1
    return player

def eat():
    pass