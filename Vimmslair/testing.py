from playwright.sync_api import sync_playwright

fileName = 'Abadox - The Deadly Inner War (USA)'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://vimm.net/vault/10")

    with page.expect_download() as download_info:
        page.locator('xpath=/html/body/div[4]/div[2]/div/div[3]/div[2]/div[1]/table/tbody/tr[21]/td/table/tbody/tr[1]/td[2]/form/button').click()

    download = download_info.value
    download.save_as(f'C:/Users/thetr/Documents/games/{fileName}.zip')









'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

fileName = 'Abadox - The Deadly Inner War (USA)'

def enable_download(driver):
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': "C:/Users/thetr/Downloads"}}
    driver.execute("send_command", params)

def setting_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    return chrome_options

def isFileDownloaded():
    file_path = f"C:/Users/thetr/Downloads/{fileName}.zip"
    while not os.path.exists(file_path):
        time.sleep(1)
    if os.path.isfile(file_path):
        print("File Downloaded successfully..")



driver.get('https://vimm.net/vault/10')
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[3]/div[2]/div[1]/table/tbody/tr[21]/td/table/tbody/tr[1]/td[2]/form/button').click()
time.sleep(20)
driver.close()


if __name__ == '__main__':
    driver = webdriver.Chrome(options=setting_chrome_options())
    enable_download(driver)
    driver.get("https://vimm.net/vault/10")
    button = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[3]/div[2]/div[1]/table/tbody/tr[21]/td/table/tbody/tr[1]/td[2]/form/button').click()
    #isFileDownloaded()
    print("\ndownloaded\n")
'''