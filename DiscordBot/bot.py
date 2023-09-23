from discord.ext import commands, tasks
import discord
import time
from dotenv import load_dotenv
import os
import random

load_dotenv(dotenv_path="C:/Users/thetr/Documents/Python/DiscordBot/token.env")
token = os.getenv('token')

times = []
lines = []
values = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
ids = []
cards = False
cardsLoaded = False
log = ""
inp = ""
dailyCards = 3

def addTime(startTime, addition):
    count = 0
    time = startTime.split(":")
    hour = int(time[0])
    minute = int(time[1])
    minute = minute + int(addition)

    while minute > 59:
        count += 1
        minute -= 60

    hour = hour + count
    if minute < 10:
        time = str(hour) + ":0" + str(minute)
    else:
        time = str(hour) + ":" + str(minute)

    return time

def changeStartTime(time):
    global times
    time = str(time)
    times = []
    times.append(time)
    times.append(addTime(time, 13))
    times.append(addTime(time, 24))
    times.append(addTime(time, 41))
    times.append(addTime(time, 86))
    times.append(addTime(time, 120))
    times.append(addTime(time, 171))
    times.append(addTime(time, 247))
    times.append(addTime(time, 361))
    times.append(addTime(time, 532))
    times.append(addTime(time, 780))

def loadFlashcards():
    global values
    global lines
    lineCounter = 0

    f = open("C:/Users/thetr/Documents/Python/DiscordBot/nlpt5.txt", "r", encoding='utf-8')
    lines = f.readlines()
    f.close()

    for items in lines:
        line = str(items.split("|")[0])
        if line[0] == "0":
            line = list(line)
            del line[0]
            line = "".join(line)
        line = int(line)
        values[line].append(lineCounter)
        lineCounter += 1

def selectCards():
    selectedItems = []
    for i in range(30):
        for ii in range(dailyCards):
            try:
                selectedItems.append(random.choice(values[i]))
            except:
                break
    return selectedItems

monthToNum = {
    "Jan":"01",
    "Feb":"02",
    "Mar":"03",
    "Apr":"04",
    "May":"05",
    "Jun":"06",
    "Jul":"07",
    "Aug":"08",
    "Sep":"09",
    "Oct":"10",
    "Nov":"11",
    "Dec":"12"
}

currTime = ""
currDate = ""

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is connected")
    #channel = bot.get_channel(1129467559322857614)
    #await channel.send('Enter starting time using "!startTime [time string]"')
    timeUpdate.start()
    langTimeCheck.start()
    #language.start()
    reminders.start()

@tasks.loop(seconds=30)
async def timeUpdate():
    global currTime
    global currDate
    currTime = time.ctime().split(" ")[3].split(":")[0] + ":" + time.ctime().split(" ")[3].split(":")[1]
    if time.ctime()[8] == " ":
        currDate = f"{monthToNum[time.ctime().split(' ')[1]]}/0{time.ctime().split(' ')[3]}/{time.ctime().split(' ')[5][2]}{time.ctime().split(' ')[5][3]}"
    else:
        currDate = f"{monthToNum[time.ctime().split(' ')[1]]}/{time.ctime().split(' ')[2]}/{time.ctime().split(' ')[4][2]}{time.ctime().split(' ')[4][3]}"

@tasks.loop(seconds=30)
async def langTimeCheck():
    if not(times == ""):
        for items in times:
            if items == currTime:
                global cards
                global log 
                cards = True
                log = f"# {currDate} - {currTime}\n"

@tasks.loop(seconds=30)
async def reminders():
    f = open("C:/Users/thetr/Documents/Python/DiscordBot/reminders.txt", "r")
    fContent = f.readlines()
    f.close()

    if not(fContent == ""):
        for items in fContent:
            if items.split("|")[0] == currDate:
                if items.split("|")[1] == currTime:
                    channel = bot.get_channel(1129454119673925672)
                    await channel.send(f"@everyone:\n> {items.split('|')[2]}")
                    fContent.remove(items)
        
        f = open("C:/Users/thetr/Documents/Python/DiscordBot/reminders.txt", "w")
        f.write("")
        f.close()

        f = open("C:/Users/thetr/Documents/Python/DiscordBot/reminders.txt", "a")
        for i in range(len(fContent)):
            f.write(fContent[i])
        f.close()

#reset the variables  log, cardsLoaded, cards, inp, lines, ids
@tasks.loop(seconds=1)
async def language():
    if cards:
        global cardsLoaded
        if cardsLoaded == False:
            loadFlashcards()
            selectedCards = selectCards()
            cardsLoaded = True

        for items in selectedCards:
            channel = bot.get_channel(1129467533372686428)
            await channel.send(f"{lines[items].split('|')[2]}") #send hiragana
            while inp == "":
                pass

            answer = lines[items].split("|")[4]
            if "," in answer:
                answer = answer.split(",")
            else:
                answer = [answer]

            correct = False
            for parts in answer:
                if parts == inp:
                    correct = True
                    await channel.send(f"### *{inp}* is correct")
                    currLine = lines[items].split("|")
                    if currLine[0][0] == "0":
                        currLineNum = list(currLine[0])
                        del currLineNum[0]
                        currLineNum = "".join(currLineNum)

                    currLineNum = int(currLine[0]) + 1
                    if len(currLineNum) == 1:
                        currLineNum = "0" + str(currLineNum)
                    else:
                        currLineNum = str(currLineNum)
                    
                    currLine[0] = currLineNum
                    currLine = f"{currLine[0]}|{currLine[1]}|{currLine[2]}|{currLine[3]}|{currLine[4]}|" 
                    lines[items] = currLine
            
            if correct == False:
                corrections = lines[items].split("|")[4]
                if "," in corrections:
                    corrections = corrections.split(",")
                    string = ""
                    for parts in corrections:
                        string = f"{string}> {parts}\n"
                    corrections = string
                await channel.send(f"### *{inp}* is incorrect\n\nCorrect answers are:\n{corrections}")

                currLine = lines[items].split("|")
                currLine[0] = "00"
                currLine = f"{currLine[0]}|{currLine[1]}|{currLine[2]}|{currLine[3]}|{currLine[4]}|" 
                lines[items] = currLine


@bot.event
async def on_message(message):
    if message.content == "!stop":
        exit(1)

    global times
    global cards

    if cards == True:
        log = f"{log}||{message.author}: {message.content}||\n"
        if message.channel.id == 1129467533372686428:
            ids.append(message.id)

    if message.author == bot.user:
        return

    try:
        if cards == True:
            global inp
            inp = message.content
        #if message.channel.id == 1129467533372686428:
        #    await message.delete()

        if message.content == "!help":
            await message.channel.send("## All Commands\n> **!help**\n> !addTime [time]\n> !createPreset [Preset Name]\n> !dailyCards [amount]\n> !delete\n> !removeTime [time]\n> !selectPreset [Preset Name]\n> !setReminder [mm/dd/yy] [time] [reminder content]\n> !showPresets\n> !spacedRepetition [time]\n> !stop\n> !timeList\n")
        
        if message.content == "ping":
            await message.channel.send("pong")

        if message.content == "!delete":
            await message.delete()

        if "!dailyCards" in message.content:
            try:
                global dailyCards
                dailyCards = int((message.content).split(" ")[1])
                await message.channel.send(f"Daily Cards set to *{dailyCards}*")
            except:
                await message.channel.send("Invalid Input")

        if "!addTime" in message.content:
            try:
                mess = (message.content).split(" ")[1]
                if ";" in mess:
                    mess = list(mess)
                    for i in range(len(mess)):
                        if ";" == mess[i]:
                            mess[i] = ":"
                    mess = "".join(mess)
                times.append(mess)
                await message.channel.send(f"*{mess}* was added")
            except:
                await message.channel.send("Invalid Input")

        if "!removeTime" in message.content:
            try:
                times.remove((message.content).split(" ")[1])
                await message.channel.send(f"*{(message.content).split(' ')[1]}* was removed")
            except:
                await message.channel.send("Invalid Input")

        if "!selectPreset" in message.content:
            try:
                f = open("C:/Users/thetr/Documents/Python/DiscordBot/presets.txt", "r")
                presets = f.readlines()
                f.close()
                messParts = (message.content).split(" ")
                if len(messParts) == 2:
                    mess = str(messParts[1])
                else:
                    for i in range(len(messParts)):
                        mess = ""
                        if i > 0:
                            mess = f"{mess} {messParts[i]}"
                presetFound = False
                for items in presets:
                    if mess in items:
                        presetFound = True
                        preset = items.split("|")[0]
                        times = str(items.split("|")[1]).split(",")
                if presetFound:
                    await message.channel.send(f"Preset *{preset}* was loaded.")
                else:
                    await message.channel.send(f"Preset '{mess}' wasn't found.")
            except:
                await message.channel.send("Invalid Input")

        if "!createPreset" in message.content:
            try:
                messParts = (message.content).split(" ")
                if len(messParts) == 2:
                    mess = str(messParts[1])
                else:
                    mess = ""
                    for i in range(len(messParts)):
                        if i > 0:
                            mess = f"{mess} {messParts[i]}"
                string = f"{mess}|"
                for items in times:
                    string = f"{string}{items},"
                string = f"{string}|\n"
                string = list(string)
                del string[-3]
                string = "".join(string)
                f = open("C:/Users/thetr/Documents/Python/DiscordBot/presets.txt", "a")
                f.write(string)
                f.close()
                await message.channel.send(f"Created preset '{mess}'.")
            except:
                await message.channel.send("Invalid Input")

        if "!showPresets" in message.content:
            f = open("C:/Users/thetr/Documents/Python/DiscordBot/presets.txt", "r")
            text = f.readlines()
            f.close()
            string = "Presets are:\n"
            for items in text:
                string = f"{string}{items.split('|')[0]}\n"
            await message.channel.send(string)

        if "!spacedRepetition" in message.content:
            try:
                mess = (message.content).split(" ")[1]
                changeStartTime(mess)
                await message.channel.send(f"Start Time Set For {mess}")
            except:
                await message.channel.send("Invalid Input")

        if message.content == "!timeList":
            if len(times) == 0:
                await message.channel.send("No Times Assigned")
            else:
                string = ""
                for i in range(len(times)):
                    string = string + times[i] + ", "
                string = list(string)
                del string[-2]
                string = "".join(string)
                await message.channel.send(string)
        

        if "!setReminder" in message.content:
            try:
                mess = (message.content).split(" ")
                date = mess[1]

                if (int(date[0])) < 10:
                    date = "0" + date
                    
                remTime = mess[2]
                messageContent = ""

                for i in range(len(mess)):
                    if i > 2:
                        messageContent = messageContent + mess[i] + " "
                
                f = open("C:/Users/thetr/Documents/Python/DiscordBot/reminders.txt", "r")
                remSave = f.readlines()
                f.close()

                remSave.append(f"{date}|{remTime}|{messageContent}\n")
                await message.channel.send(f"Reminder: *{messageContent}* saved for *{remTime}* on *{date}*")

                messageContent = ""
                for i in range(len(remSave)):
                    messageContent = messageContent + remSave[i]

                f = open("C:/Users/thetr/Documents/Python/DiscordBot/reminders.txt", "w")
                f.write(messageContent)
                f.close()
            except:
                await message.channel.send("Invalid Input")
    
    except:
        await message.channel.send("An error occured, please try again.")

    await bot.process_commands(message)

bot.run(token)
