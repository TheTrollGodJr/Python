from PIL import Image
import os

files = os.listdir("E:/Photos/Picture Time")
count = 1

date = [2020, 7, 10]

def dateChange(dateInput):
    global date
    year, month, day = dateInput
    day += 1

    if month == 2:
        if day > 29:
            day = 1
            month = 3
    
    elif (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        if day > 31:
            day = 1
            if month == 12:
                year += 1
                month = 1
            else:
                month += 1
    
    else:
        if day > 30:
            day = 1
            month += 1
    
    date[0] = year
    date[1] = month
    date[2] = day

def dateToString(dateInput):
    year, month, day = dateInput
    year = str(year)

    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)
    
    if day < 10:
        day = "0" + str(day)
    else:
        day = str(day)

    return year + month + day

while True:
    for items in files:
        if dateToString(date) in items:
            img = Image.open(f"E:/Photos/Picture Time/{items}")
            if not "IMG" in items:
                if str(img.size[1]) == "1592":
                    img = img.rotate(90, expand=True)
                else:
                    img = img.rotate(-90, expand=True)
            img.save(f"C:/Users/thetr/Documents/Python/PictureTime/Pictures/{count}.png")
            count += 1
            break
    dateChange(date)
    if (date[0] == 2023) and (date[1] == 7) and (date[2] == 21):
        break
