from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import os
from os import startfile

load_dotenv(dotenv_path="C:/Users/thetr/Documents/Python/aternosStartup/token.env")
user = os.getenv('login')
password = os.getenv('password')

# Configure Chrome to run in headless mode
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Initialize the Chrome WebDriver with the headless option
driver = webdriver.Chrome(options=chrome_options)

# Now you can use 'driver' to navigate the web, interact with web pages, and perform actions.

# For example, you can navigate to a website:
driver.get("https://aternos.org/go")

submitButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[4]/div[4]/div[4]')))

usernameButton = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[4]/div[4]/div[1]/div[2]/input')
usernameButton.click()
usernameButton.send_keys(str(user))

passwordButton = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[4]/div[4]/div[2]/div[2]/input')
passwordButton.click()
passwordButton.send_keys(str(password))

time.sleep(3)

submitButton.click()

#time.sleep(10)
#input("")

# Close the browser when you're done
driver.quit()