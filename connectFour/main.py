#You can modify this as needed, but no game data should be stored here. You have to use the "server.txt" for game data

#Your file should be named player.py
import player
#Your file should be named computer.py
import computer

#This resets your "server.txt" file whenever you start a new game
file = open("connectFour/server.txt", "w")
file.write("0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n") #Replace this String with whatever you want to start with in your "server.txt"
file.close()

#player.py and computer.py need to have functions called run() that will be called here
#run() should return True if the game is over
#run() should return False if the game should continue
while True:
    if player.run() == True or computer.run() == True:
        break
print("Game Over")