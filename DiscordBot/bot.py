from discord.ext import commands, tasks
import discord
import time
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:/Users/thetr/Documents/Python/DiscordBot/token.env")
token = os.getenv('token')

times = []

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
    channel = bot.get_channel(1129467559322857614)
    await channel.send('Enter starting time using "!startTime [time string]"')
    timeUpdate.start()
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
async def language():
    if not(times == ""):
        for items in times:
            if items == currTime:
                pass #language flash card thing here
            

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


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == "!help":
        await message.channel.send("## All Commands\n> **!help**\n> !startTime [time string]\n> !stop\n> !timeList\n> !setReminder [mm/dd/yy] [time] [reminder content]")
    
    if message.content == "ping":
        await message.channel.send("pong")

    if message.content == "!stop":
        exit(1)

    if "!startTime" in message.content:
        mess = (message.content).split(" ")[1]
        print(mess)
        changeStartTime(mess)
        await message.channel.send(f"Start Time Set For {mess}")
        print(times)

    if message.content == "!timeList":
        if len(times) == 0:
            await message.channel.send("No Times Assigned")
        else:
            string = ""
            for i in range(len(times)):
                string = string + times[i] + ", "
            await message.channel.send(string)

    if "!setReminder" in message.content:
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

    await bot.process_commands(message)

bot.run("TOKEN")
