from discord.ext import commands, tasks
import discord
import time
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:/Users/thetr/Documents/Python/token/token.env")
token = os.getenv('archiveBotToken')

channels = []
filePath = "C:/Users/thetr/Documents/Python/discordArchive/archive"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    for guild in bot.guilds:
        for channel in guild.text_channels:
            channels.append([channel.name, channel.id])

    #print(channels)
    for items in channels:
        if os.path.exists(f"{filePath}/{items[0]}.txt") == False:
            with open(f"{filePath}/{items[0]}.txt", "w") as f:
                f.write("")
    
    get_message()

    await bot.close()


@bot.command(name='get_message')
async def get_message(ctx):
    channel = bot.get_channel(1113556415563452550)#int(channel[0][1]))
    async for message in channel.history(limit=10000):
        with open(f"{filePath}/{channel[0][0]}.txt", "a") as f:
            f.write(message.content)
            f.write("\n")
        #print(message.content)
    #print('Message not found in the specified channel.')

bot.run(token)