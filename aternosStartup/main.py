from discord.ext import commands, tasks
import discord
from dotenv import load_dotenv
import os
from os import startfile

load_dotenv(dotenv_path="C:/Users/thetr/Documents/Python/aternosStartup/token.env")
token = os.getenv('token')

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is connected")

@bot.event
async def on_message(message):
    if message.content == "!stop":
        exit(1)

    if message.author == bot.user:
        return
    
    if message.content == "!mcstart":
        startfile("C:/Users/thetr/Documents/Python/aternosStartup/startup.py")

    await bot.process_commands(message)

bot.run(token)