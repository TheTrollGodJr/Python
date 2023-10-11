import time
import random
import os
from os import startfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

files = os.listdir(r"C:\Users\thetr\Documents\Python\wakeUp\videos")

while True:
    time.sleep(5)
    day = time.ctime().split(" ")[0]
    if (day != "Sun") and (day != "Sat"):
        tm = time.ctime().split(" ")[4].split(":")[:2]
        if (tm[0] == "04") and (tm[1] == "40"):
            time.sleep(15)
            driver = webdriver.Chrome()
            driver.get("https://www.youtube.com/watch?v=7HgJIAUtICU&ab_channel=Vaundy")

            try:
                video = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="movie_player"]/div[6]/button')))
                video.click()
            except Exception as e:
                print(e)

            time.sleep(240)
            driver.close()
            time.sleep(3)
            startfile(f"C:/Users/thetr/Documents/Python/wakeUp/videos/{random.choice(files)}")
            startfile(f"C:/Users/thetr/Documents/Python/wakeUp/writing/app.py")
