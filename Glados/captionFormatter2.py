import os
delList = []
delCount = 0
string = ""
fileString = ""
prefix = "/content/TTS-TT2/wavs/"
count = 1

f = open("C:/Users/thetr/Documents/Python/Glados/filenames.txt", "r")
filenames = f.readlines()
f.close()

f = open("C:/Users/thetr/Documents/Python/Glados/captions.txt", "r", encoding='utf-8')

while True:
    try:
        caption = f.readline()
        delList = []
        delCount = 0
        quote = caption.split(": ")

        if len(quote) == 2:
            quote = quote[1]
        else:
            quote = quote[1] + quote[2]

        file = caption.split('"')[1].split("glados.")[1]

        quote = list(quote)
        for i in range(len(quote)):
            quote[i] = quote[i].lower()
            if "-" == quote[i]:
                delList.append(i)
            elif ":" == quote[i]:
                delList.append(i) 
            elif "[" == quote[i]:
                delList.append(i)
            elif "]" == quote[i]:
                delList.append(i)   
            elif "<" == quote[i]:
                delList.append(i)
            elif ">" == quote[i]:
                delList.append(i)
            elif "(" == quote[i]:
                delList.append(i)  
            elif ")" == quote[i]:
                delList.append(i)
            elif "," == quote[i]:
                delList.append(i)
            elif '"' == quote[i]:
                delList.append(i)
            elif "." == quote[i]:
                delList.append(i)                      

        for items in delList:
            del quote[int(items) - delCount]
            delCount += 1

        quote[0] = quote[0].upper()
        if quote[-2] != "!":
            quote[-1] = ""
        if quote[-2] == "?":
            quote[-1] = ""
        else:
            quote[-1] = "."
        quote = "".join(quote)

        string = f"{string}{prefix}{count}.wav|{quote}\n"
        fileString = f"{fileString}{file}|{count}\n"
        count += 1
    except:
        break
f.close()

f = open("C:/Users/thetr/Documents/Python/Glados/output.txt", "w")
f.write(string)
f.close()

f = open("C:/Users/thetr/Documents/Python/Glados/filenames.txt", "w", encoding='utf-8')
f.write(fileString)
f.close()