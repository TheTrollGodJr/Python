from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from os import startfile

# Configure Chrome to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Initialize the Chrome WebDriver with the headless option
driver = webdriver.Chrome(options=chrome_options)

# Now you can use 'driver' to navigate the web, interact with web pages, and perform actions.

# For example, you can navigate to a website:
driver.get("https://grabify.link/track/V3YPBG")

element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logs"]/h2/span'))).text
print(f"\n{element}\n")

while element != "2":
    print("refresh")
    driver.refresh()
    time.sleep(5)
    element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logs"]/h2/span'))).text
    print(element)
    time.sleep(20)

# Close the browser when you're done
driver.quit()

startfile("C:/Users/thetr/Documents/Python/broganBday/IPLogger/discordAlert.py")