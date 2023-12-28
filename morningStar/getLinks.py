from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@markiplier/videos")
#time.sleep(10)
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

#notes:
#make it count how many vids are in each row and set that variable
#use that variable to count each row
#after each row scroll down a little bit.

#/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/h3/a/yt-formatted-string
#/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/h3/a
#/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[1]/ytd-thumbnail/a
#/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[2]/div/ytd-rich-grid-media/div[1]/div[1]/ytd-thumbnail/a
#/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[2]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[1]/ytd-thumbnail/a
#/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{currRow}]/div/ytd-rich-item-renderer[{i + 1}]/div/ytd-rich-grid-media/div[1]/div[1]/ytd-thumbnail/a
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

#element = WebDriverWait(driver, 10).until(EC.presence_of_element_located())

'''
input("")
time.sleep(1)
driver.execute_script(f"window.scrollTo(0, 650)")
time.sleep(1)
driver.execute_script(f"window.scrollTo(0, 900)")
input("")

distanceChange = 140
input("")
time.sleep(1)
scrollDistance += distanceChange
driver.execute_script(f"window.scrollTo(0, {scrollDistance})")
time.sleep(1)
scrollDistance += distanceChange
driver.execute_script(f"window.scrollTo(0, {scrollDistance})")
time.sleep(1)
scrollDistance += distanceChange
driver.execute_script(f"window.scrollTo(0, {scrollDistance})")
time.sleep(1)
scrollDistance += distanceChange
driver.execute_script(f"window.scrollTo(0, {scrollDistance})")
time.sleep(1)
input("")'''
driver.quit()

'''
while True:
    try:
        goButton = driver.find_element(By.XPATH, '//*[@id="requestSubmit"]')
        break
    except:
        time.sleep(.1)

siteInput = driver.find_element(By.XPATH, '//*[@id="url"]')
siteInput.send_keys("youtube.com")
goButton.click()

while True:
    try:
        searchBar = driver.find_element(By.XPATH, '//*[@id="search"]')
        break
    except:
        time.sleep(.1)

searchBar.send_keys("markiplier")
#time.sleep(5)
input("")

driver.quit()'''