#import packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# read links file
with open("morningstar/links.txt", "r", encoding='utf-8') as f:
    links = f.readlines()

# Establish webdriver
driver = webdriver.Chrome()

# Loop through links list
for i in range(len(links)):

    # establish variables
    transcript = []
    count = 1

    # Add video name to list
    links.append(f"{links[i].split(' - ')[1]}")

    # Get webpage
    driver.get(links[i].split(" - ")[0])

    # Clear new file
    with open("morningStar/transcriptions.txt", "w", encoding='utf-8') as f:
        f.write("")

    # Get more button
    moreButton = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/tp-yt-paper-button[1]')))#'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/tp-yt-paper-button[1]')))
    moreButton.click()

    # get transcription button
    transcriptButton = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/div[2]/ytd-structured-description-content-renderer/div/ytd-video-description-transcript-section-renderer/div[3]/div/ytd-button-renderer/yt-button-shape/button')))#'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/div[2]/ytd-structured-description-content-renderer/div/ytd-video-description-transcript-section-renderer/div[3]/div/ytd-button-renderer/yt-button-shape/button')))
    transcriptButton.click()

    # loop through all transctiptions
    while True:
        try:
            # Get current transcription and add to list
            timeStamp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[1]/ytd-engagement-panel-section-list-renderer[4]/div[2]/ytd-transcript-renderer/div[2]/ytd-transcript-search-panel-renderer/div[2]/ytd-transcript-segment-list-renderer/div[1]/ytd-transcript-segment-renderer[{count}]/div/yt-formatted-string')))#.text
            transcript.append(timeStamp.text)
            count += 1
            time.sleep(.1)
        except:
            # Break the loop
            break

    # Write the videos transcription to the new file
    with open("morningStar/transcriptions.txt", "a", encoding='utf-8') as f:
        for items in transcript:
            f.write(f"{items}\n")
        f.write("\n")

# Close webdriver
driver.quit()   