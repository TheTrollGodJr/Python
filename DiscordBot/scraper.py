from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
loading = True
count = 1
spanCount = 1
furigana = ""
engText = ""
link = 'https://jisho.org/search/%23jlpt-n5%20%23words?page=34'

japToEng = {
    "あ":"a",
    "い":"i",
    "う":"u",
    "え":"e",
    "お":"o",
    "か":"ka",
    "き":"ki",
    "く":"ku",
    "け":"ke",
    "こ":"ko",
    "さ":"sa",
    "し":"shi",
    "す":"su",
    "せ":"se",
    "そ":"so",
    "た":"ta",
    "ち":"chi",
    "つ":"tsu",
    "て":"te",
    "と":"to",
    "な":"na",
    "に":"ni",
    "ぬ":"nu",
    "ね":"ne",
    "の":"no",
    "は":"ha",
    "ひ":"hi",
    "ふ":"fu",
    "へ":"he",
    "ほ":"ho",
    "ま":"ma",
    "み":"mi",
    "む":"mu",
    "め":"me",
    "も":"mo",
    "や":"ya",
    "ゆ":"yu",
    "よ":"yo",
    "ら":"ra",
    "り":"ri",
    "る":"ru",
    "れ":"re",
    "ろ":"ro",
    "わ":"wa",
    "を":"o",
    "ん":"n",
    "が":"ga",
    "ぎ":"gi",
    "ぐ":"gu",
    "げ":"ge",
    "ご":"go",
    "ざ":"za",
    "じ":"ji",
    "ず":"zu",
    "ぜ":"ze",
    "ぞ":"zo",
    "だ":"da",
    "ぢ":"ji",
    "づ":"zu",
    "で":"de",
    "ど":"do",
    "ば":"ba",
    "び":"bi",
    "ぶ":"bu",
    "べ":"be",
    "ぼ":"bo",
    "ぱ":"pa",
    "ぴ":"pi",
    "ぷ":"pu",
    "ぺ":"pe",
    "ぽ":"po",
    "ア":"a",
    "イ":"i",
    "ウ":"u",
    "エ":"e",
    "オ":"o",
    "カ":"ka",
    "キ":"ki",
    "ク":"ku",
    "ケ":"ke",
    "コ":"ko",
    "サ":"sa",
    "シ":"shi",
    "ス":"su",
    "セ":"se",
    "ソ":"so",
    "タ":"ta",
    "チ":"chi",
    "ツ":"tsu",
    "テ":"te",
    "ト":"to",
    "ナ":"na",
    "ニ":"ni",
    "ヌ":"nu",
    "ネ":"ne",
    "ノ":"no",
    "ハ":"ha",
    "ヒ":"hi",
    "フ":"fu",
    "ヘ":"he",
    "ホ":"ho",
    "マ":"ma",
    "ミ":"mi",
    "ム":"mu",
    "メ":"me",
    "モ":"mo",
    "ヤ":"ya",
    "ユ":"yu",
    "ヨ":"yo",
    "ラ":"ra",
    "リ":"ri",
    "ル":"ru",
    "レ":"re",
    "ロ":"ro",
    "ワ":"wa",
    "ン":"n",
    "ガ":"ga",
    "ギ":"gi",
    "グ":"gu",
    "ゲ":"ge",
    "ゴ":"go",
    "ザ":"za",
    "ジ":"ji",
    "ズ":"zu",
    "ゼ":"ze",
    "ゾ":"zo",
    "ダ":"da",
    "ヂ":"ji",
    "ヅ":"zu",
    "デ":"de",
    "ド":"do",
    "バ":"ba",
    "ビ":"bi",
    "ブ":"bu",
    "ベ":"be",
    "ボ":"bo",
    "パ":"pa",
    "ピ":"pi",
    "プ":"pi",
    "ペ":"pe",
    "ポ":"po"
}

driver.get(link)
while loading:
    try:
        loadElement = driver.find_element(By.CLASS_NAME, "logo")
        loading = False
        print(loadElement)
    except:
        pass
loading = True

while True:
    try:
        try:
            parent = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div/div[2]/div[1]/div/div[{count}]/div[1]/div[1]")
        except:
            break
        childText = parent.find_element(By.CLASS_NAME, "text").get_attribute("outerText")
        childFurigana = parent.find_element(By.CLASS_NAME, "furigana")

        while True:
            try:
                furiganaSelect = childFurigana.find_element(By.XPATH, f"/html/body/div[3]/div/div/div[2]/div[1]/div/div[{count}]/div[1]/div[1]/div/span[1]/span[{spanCount}]").get_attribute("outerText")
                print(furigana)
                if furiganaSelect == "":
                    try:
                        letter = japToEng[childText[spanCount - 1]]
                        furigana = furigana + childText[spanCount - 1]
                    except:
                        pass
                elif furiganaSelect == "ー":
                    furigana = "--------DELETE LINE OF TEXT HERE--------"
                    break
                else:
                    furigana = furigana + furiganaSelect
                spanCount += 1

            except:
                spanCount = 1
                break

        if len(furigana) > 0:
            for i in range(len(furigana)):
                if furigana[i] == "っ":
                    letter = japToEng[furigana[i + 1]][0]
                    engText = engText + letter

                elif (furigana[i] == "ゃ") or (furigana[i] == "ャ"):
                    engText = list(engText)
                    engText[-1] = "y"
                    engText = "".join(engText)
                    engText = engText + "a"

                elif (furigana[i] == "ゅ") or (furigana[i] == "ュ"):
                    engText = list(engText)
                    engText[-1] = "y"
                    engText = "".join(engText)
                    engText = engText + "u"

                elif (furigana[i] == "ょ") or (furigana[i] == "ョ"):
                    engText = list(engText)
                    engText[-1] = "y"
                    engText = "".join(engText)
                    engText = engText + "o"
                    
                else:
                    print("\n\n", str(engText), str(furigana[i]), "\n\n")
                    engText = engText + japToEng[furigana[i]]
        else:
            for i in range(len(childText)):
                if childText[i] == "っ":
                    letter = japToEng[childText[i + 1]][0]
                    engText = engText + letter

                elif (childText[i] == "ゃ") or (childText[i] == "ャ"):
                    engText = list(engText)
                    engText[-1] = "y"
                    engText = "".join(engText)
                    engText = engText + "a"

                elif (childText[i] == "ゅ") or (childText[i] == "ュ"):
                    engText = list(engText)
                    engText[-1] = "y"
                    engText = "".join(engText)
                    engText = engText + "u"

                elif (childText[i] == "ょ") or (childText[i] == "ョ"):
                    engText = list(engText)
                    engText[-1] = "y"
                    engText = "".join(engText)
                    engText = engText + "o"
                    
                else:
                    print("\n\n", str(engText), str(childText[i]), "\n\n")
                    engText = engText + japToEng[childText[i]]

        definition = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div/div[2]/div[1]/div/div[{count}]/div[2]/div/div[2]/div/span[2]").get_attribute("outerText")
        try:
            defi = definition.split("; ")
            definition = ""
            for items in defi:
                definition = definition + items + ","
            definition = list(definition)
            del definition[-1]
            definition = "".join(definition)
        except:
            pass

        string = f"00|{childText}|{furigana}|{engText}|{definition}|\n"
        print(string)

        f = open("C:/Users/thetr/Documents/Python/DiscordBot/dict.txt", "a", encoding="utf8")
        f.write(str(string))
        f.close()

        string = ""
        furigana = ""
        furiganaSelect =""
        childText = ""
        engText = ""
        count += 1
    except:
        count += 1