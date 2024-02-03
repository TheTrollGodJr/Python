import time
import discord
from discord.ext import commands, tasks
import discord
import time
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:/Users/thetr/Documents/Python/token/token.env")
token = os.getenv('tessaBotToken')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

async def send_spam(channel):
    while True:
        await channel.send("# Tessa")
        time.sleep(1)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    #get_message()
    channel = bot.get_channel(1202385571817721879)
    bot.loop.create_task(send_spam(channel))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content == "!stop":
        await bot.close()

bot.run(token)