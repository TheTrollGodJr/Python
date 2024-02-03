from discord.ext import commands, tasks
import discord
import time
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:/Users/thetr/Documents/Python/token/token.env")
token = os.getenv('token')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

# Set a constant distance value
constant_distance = 5

#target_channel_id = 1129467559322857614

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    #get_message()
    channel = bot.get_channel(1194500356231659631)
    with open("FileToText/output.txt", "r", encoding='utf-8') as f:
        while True:
            try:
                await channel.send(f.readline())
                time.sleep(.1)
            except:
                break
    await bot.close()

'''
@bot.command(name='get_message')
async def get_message(ctx):
    channel = bot.get_channel(target_channel_id)
    async for message in channel.history(limit=10000):
        print(message.content)

    #print('Message not found in the specified channel.')
'''
    
bot.run(token)