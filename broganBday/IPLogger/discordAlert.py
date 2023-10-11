from discord.ext import commands, tasks
import discord
from dotenv import load_dotenv
import os
import time

load_dotenv(dotenv_path="C:/Users/thetr/Documents/Python/broganBday/IPLogger/token.env")
token = os.getenv('token')

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    for i in range(5):
        channel = bot.get_channel(1129454119673925672)
        await channel.send(f"@everyone\nPuzzle Completed {i + 1}") #send hiragana
        time.sleep(10)
    exit(1)

bot.run(token)