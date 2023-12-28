from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Chrome to run in headless mode
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Initialize the Chrome WebDriver with the headless option
driver = webdriver.Chrome(options=chrome_options)

# Now you can use 'driver' to navigate the web, interact with web pages, and perform actions.

# For example, you can navigate to a website:
driver.get("https://www.xe.com/currencyconverter/")

#dollarInput = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="amount"]')))
#dollarInput.click()
#dollarInput.send_keys("100")

#convertButton = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[2]/section/div[2]/div/main/div/div[2]/button')
#convertButton.click()

#time.sleep(30)

popup = WebDriverWait(driver, 40).until(EC.element_located_to_be_selected((By.XPATH, '#//*[@id="yie-overlay-9131260e-d77a-53bc-95d7-75a84936d02c"]'))) 
#exitPopup = driver.find_element(By.XPATH, '//*[@id="element-Fftdpk"]') 
#exitPopup.click()

driver.execute("""
var element = document.querySelector(".classname");
if (popup)
    element.parentNode.removeChild(popup);
""")

inp = input()

# Close the browser when you're done
driver.quit()
#//*[@id="element-x_6p20"]/span
#//*[@id="element-x_6p20"]
#//*[@id="element-x_6p20"]/span/svg
#//*[@id="element-x_6p20"]/span/svg/line[1]
#
#//*[@id="element-Fftdpk"]/span/svg
#//*[@id="element-Fftdpk"]/span
#//*[@id="element-Fftdpk"]
#
#//*[@id="yie-backdrop-fc6e9e34-5711-5f0e-a986-502bca89c6d4"]
#
#//*[@id="yie-overlay-9131260e-d77a-53bc-95d7-75a84936d02c"]
#//*[@id="yie-overlay-fc6e9e34-5711-5f0e-a986-502bca89c6d4"]
#//*[@id="yie-overlay-eb6f9728-4f36-5a08-9f33-8c868fd1b529"]