from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.discord.com/app")

#wait for login
input("")



load = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div/div[2]/div/div[1]/yt-img-shadow/img')))
time.sleep(3)

'''
while True:
    try:
        load = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div/div[2]/div/div[1]/yt-img-shadow/img')
        break
    except:
        time.sleep(.1)
'''

with open("morningStar/links.txt", "w") as f:
    f.write("")

driver.execute_script("window.scrollTo(0, 400)")
scrollDistance = 400
scrollChange = 250
rowLen = 0
currRow = 1
end = False

# go until the vid "We Need to Delete Artbreeder Before It's Too Late" -- dec 19th 2020
links = []

while True:
    try:
        rowLen += 1
        vid = driver.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[{rowLen}]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/h3/a')
    except:
        break
#print(rowLen)
#'''
while True:
#for j in range(3):
    for i in range(rowLen - 1):
        #print(i)
        #vid = driver.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{currRow}]/div/ytd-rich-item-renderer[{i + 1}]/div/ytd-rich-grid-media/div[1]/div[1]/ytd-thumbnail/a')
        #(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{currRow}]/div/ytd-rich-item-renderer[{i + 1}]/div/ytd-rich-grid-media/div[1]/div[1]/ytd-thumbnail/a')
        vid = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{currRow}]/div/ytd-rich-item-renderer[{i + 1}]/div/ytd-rich-grid-media/div[1]/div[1]/ytd-thumbnail/a')))
        vidName = driver.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{currRow}]/div/ytd-rich-item-renderer[{i + 1}]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/h3/a/yt-formatted-string').text#get_attribute('text')
        print(vidName)
        links.append([str(vid.get_attribute('href')), vidName])
        if vidName == "We Need to Delete Artbreeder Before It's Too Late":
            end = True
            break
    currRow += 1
    #change row
    if end:
        break
    scrollDistance += scrollChange
    driver.execute_script(f"window.scrollTo(0, {scrollDistance})")
    time.sleep(.1)
#    '''
#print(links)

with open("morningStar/links.txt", "a") as f:
    for items in links:
        f.write(f"{items[0]} - {items[1]}\n")

driver.quit()