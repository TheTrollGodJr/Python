from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Set Chrome options to run the browser in headless mode
chrome_options = Options()
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# Navigate to a webpage
#driver.get('https://github.com/TheTrollGodJr/VOID/blob/main/VOID.pyw')
driver.get('https://google.com')

#code = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="read-only-cursor-text-area"]/text()')))
'''
while True:
    try:
        code = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[2]/div/div[3]/section/div/div/div[1]/div[1]/textarea/text()')
        break
    except Exception:
        print(Exception)
        break
        time.sleep(.1)
exit(1)
'''

code = driver.find_element(By.XPATH, '/html/body/header/div[2]/div[3]/div[1]/div/div[1]/a')#.text

with open("VOID/Main/output.txt", "w") as f:
    f.write(code)

#input("")
# Close the browser
driver.quit()
