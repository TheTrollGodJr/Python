from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.narakeet.com/app/text-to-audio/?projectId=447d1070-9264-47bb-9079-f5dd3c2511b3")

loading = True
while loading:
    try:
        loaded = driver.find_element(By.XPATH, "/html/body/main/div[5]/div/h1[1]")
        loading = False
    except:
        pass

dropDown = Select(driver.find_element(By.XPATH, "/html/body/main/div[5]/div/div[1]/div[1]/select"))
dropDown.select_by_value("es-MX")


dropDown = Select(driver.find_element(By.XPATH, "/html/body/main/div[5]/div/div[1]/div[2]/select"))
dropDown.select_by_value('silvana')

inp = input("")