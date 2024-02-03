import time
import discord
from discord.ext import commands, tasks
import discord
import time
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_current_datetime():
    current_time = time.localtime()
    formatted_hour_minute = time.strftime("%H:%M", current_time)
    day_of_week = time.strftime("%A", current_time)
    result_list = [day_of_week, formatted_hour_minute.split(":")[0], formatted_hour_minute.split(":")[1]]

    return result_list  # month, day, year, day of the week, hour, minute

count = 0

def sendNotif():
    load_dotenv(dotenv_path="C:/Users/thetr/Documents/Python/token/token.env")
    token = os.getenv('token')

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=".", intents=intents)

    async def send_spam(channel):
        while True:
            await channel.send("E")
            time.sleep(5)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')
        #get_message()
        channel = bot.get_channel(1201281506283356231)
        bot.loop.create_task(send_spam(channel))
    
    @bot.event
    async def on_message(message):
        global count
        count += 1
        if count > 100:
            count = 0
            await bot.close()

        #print(message.content, count)
        if message.author == bot.user:
            return
        else:
            await bot.close()

    bot.run(token)

def checkTime(currentTime):
    print(currentTime)
    if currentTime[0] == "Monday" or currentTime[0] == "Tuesday" or currentTime[0] == "Wednesday" or currentTime[0] == "Thursday" or currentTime[0] == "Friday":
        if currentTime[1] == '5' or currentTime[1] == '05':
            if currentTime[2] == '30':
                sendNotif()
                playSong()

def playSong():
    while True:
        time.sleep(1)
        driver = webdriver.Chrome()
        driver.get("https://www.youtube.com/watch?v=WCCovrKvAtU&ab_channel=rainbeary")

        try:
            video = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="movie_player"]/div[7]/button')))
            video.click()
        except Exception as e:
            print(e)

        while True:
            try:
                exitConfirm = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[7]/button')
                #print("Button Found")
                time.sleep(5)
            except:
                driver.close()
                break


if __name__ == "__main__":
    while True:
        checkTime(get_current_datetime())
        time.sleep(58)