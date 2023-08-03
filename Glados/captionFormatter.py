import os

fileNames = os.listdir(r"C:\Users\thetr\Documents\Glados\original")
prefix = "/content/TTS-TT2/wavs/"
count = 0
lineCount = 0
string = ""
fileString = ""

f = open(r"C:\Users\thetr\Documents\Python\Glados\captions.txt", "r", encoding='utf-8')

while True:
    try:
        run = False
        line = f.readline()
        line = line.split(": ")
        file = line[0].split('"')[1].split("glados.")[1].split("\n")[0]
        #print(file)
        line = line[1]

        for items in fileNames:
            if file in items:
                run = True
                print(items)
                break
        
        if run:
            line = list(line)
            while True:
                #del line[-1]
                try:
                    if (line[lineCount] == '"') or (line[lineCount] == '!') or (line[lineCount] == '?') or (line[lineCount] == '_') or (line[lineCount] == '"') or (line[lineCount] == '.') or (line[lineCount] == ","):
                        del line[lineCount]
                    if (line[lineCount] == '-'):
                        line[lineCount] = " "
                    lineCount += 1
                except:
                     lineCount = 0
                     line = "".join(line).lower()
                     line = list(line)
                     line[0] = line[0].upper()
                     line = "".join(line)
                     break
        
            string = f"{string}{prefix}{count}.wav|{line}.\n"
            fileString = fileString + f"{file}|{count}\n"
            count += 1
            
    except:
        break
f.close()

f = open(r"C:\Users\thetr\Documents\Python\Glados\output.txt", "w")
f.write(string)
f.close()

f = open("C:/Users/thetr/Documents/Python/Glados/filenames.txt", "w")
f.write(fileString)
f.close()