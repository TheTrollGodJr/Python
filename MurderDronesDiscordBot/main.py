from discord.ext import commands, tasks
import discord
from dotenv import load_dotenv
import os
from datetime import datetime
import sys

def time_until_target(target_date):
    # Convert the input string to a datetime object
    target_datetime = datetime.strptime(target_date, '%Y-%m-%d %H:%M:%S')
    
    # Get the current date and time
    current_datetime = datetime.now()
    
    # Calculate the time difference
    time_difference = target_datetime - current_datetime
    
    # Extract days, hours, minutes, and seconds from the time difference
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes, seconds

target_date = "2024-04-12 15:00:00"

load_dotenv(dotenv_path="C:/Users/thetr/Documents/Python/token/token.env")
token = os.getenv('murderdrones')

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is connected")

@bot.event
async def on_message(message):
    global target_date

    if message.author == bot.user:
        return
    
    try:
        if message.content == "/mdhelp":
            await message.channel.send("### Commands\n**/help** - list all commands\n**/countdown** - show time until next episode\n**/change [year]-[month]-[day] [hour]:[minute]:[00]** - set new countdown date. set time in military time\n**/mdstop** - turn off the bot")
        
        if message.content == "/countdown":
            days, hours, minutes, seconds = time_until_target(target_date)
            if days > 0:
                await message.channel.send(f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds until episode 8.")
            elif days < 0:
                await message.channel.send("Countdown finished; use /change to set a new countdown date")
            elif hours > 0:
                await message.channel.send(f"{hours} hours, {minutes} minutes, and {seconds} seconds until episode 8.")
            elif minutes > 0:
                await message.channel.send(f"{minutes} minutes, and {seconds} seconds until episode 8.")
            else:
                await message.channel.send(f"{seconds} seconds until episode 8.")
            
            return
        
        if "/change" in message.content:
            try:
                target_date = message.content.strip()
                date = target_date.split(" ")[0].split("-")
                time = target_date.split(" ")[1]
                await message.channel.send(f"Time updated to {date[0]}, {date[1]}, {date[2]} at {time}")
                return
            except:
                await message.channel.send(f"Invalid Input")
                return
        
        if "/mdstop":
            await bot.close()

        await bot.process_commands(message)
    except Exception as e:
        print(e)
        await message.channel.send("An Error occured")
bot.run(token)