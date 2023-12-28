from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with open("morningstar/links.txt", "r", encoding='utf-8') as f:
    links = f.readlines()

for i in range(len(links)):
    transcript = []
    links.append(f"{links[i].split(' - ')[1]}")
    driver = webdriver.Chrome()
    driver.get(links[i].split(" - ")[0])
    #driver.get("https://www.youtube.com/watch?v=XZZaGvcbBSo&ab_channel=Markiplier")##https://www.youtube.com/watch?v=C_dH5mjej9k")

    with open("morningstar/transcriptions.txt", "w", encoding='utf-8') as f:
        f.write("")

    moreButton = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/tp-yt-paper-button[1]')))#'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/tp-yt-paper-button[1]')))
    moreButton.click()

    transcriptButton = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/div[2]/ytd-structured-description-content-renderer/div/ytd-video-description-transcript-section-renderer/div[3]/div/ytd-button-renderer/yt-button-shape/button')))#'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/div[2]/ytd-structured-description-content-renderer/div/ytd-video-description-transcript-section-renderer/div[3]/div/ytd-button-renderer/yt-button-shape/button')))
    transcriptButton.click()

    count = 1

    while True:
        try:
            #                                                                                       /html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[1]/ytd-engagement-panel-section-list-renderer[5]/div[2]/ytd-transcript-renderer/div[2]/ytd-transcript-search-panel-renderer/div[2]/ytd-transcript-segment-list-renderer/div[1]/ytd-transcript-segment-renderer[2]/div/yt-formatted-string
            #                                                                                       /html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[1]/ytd-engagement-panel-section-list-renderer[5]/div[2]/ytd-transcript-renderer/div[2]/ytd-transcript-search-panel-renderer/div[2]/ytd-transcript-segment-list-renderer/div[1]/ytd-transcript-segment-renderer[1]/div/yt-formatted-string
            #                                                                                       /html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[1]/ytd-engagement-panel-section-list-renderer[4]/div[2]/ytd-transcript-renderer/div[2]/ytd-transcript-search-panel-renderer/div[2]/ytd-transcript-segment-list-renderer/div[1]/ytd-transcript-segment-renderer[1]/div/yt-formatted-string
            #                                                                                       /html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[1]/ytd-engagement-panel-section-list-renderer[4]/div[2]/ytd-transcript-renderer/div[2]/ytd-transcript-search-panel-renderer/div[2]/ytd-transcript-segment-list-renderer/div[1]/ytd-transcript-segment-renderer[1]/div/yt-formatted-string
            #                                                                                       /html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[1]/ytd-engagement-panel-section-list-renderer[4']/div[2]/ytd-transcript-renderer/div[2]/ytd-transcript-search-panel-renderer/div[2]/ytd-transcript-segment-list-renderer/div[1]/ytd-transcript-segment-renderer[1]/div/yt-formatted-string
            timeStamp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[1]/ytd-engagement-panel-section-list-renderer[4]/div[2]/ytd-transcript-renderer/div[2]/ytd-transcript-search-panel-renderer/div[2]/ytd-transcript-segment-list-renderer/div[1]/ytd-transcript-segment-renderer[{count}]/div/yt-formatted-string')))#.text
            #print(timeStamp)
            print(timeStamp.text)
            transcript.append(timeStamp.text)
            count += 1
        except:
            print('failed')
            count = 0
            break

    #input('')

    with open("morningstar/transcriptions.txt", "a", encoding='utf-8') as f:
        for items in transcript:
            f.write(f"{items}\n")
        f.write("\n")

#time.sleep(5)

driver.quit()