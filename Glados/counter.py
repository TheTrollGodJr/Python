string = ""
f = open("C:/Users/thetr/Documents/Python/Glados/output.txt", "r")
count = 1
while True:
    try:
        line = f.readline().split("|")[1]
        print(line)
        #prefix = str(line[0].split("/")[3]) + "/" + str(line[0].split("/")[4])
        #line = prefix + "|" + str(line[1])
        #string = f"{string}{line}"
        string = f"{string}/content/gdrive/MyDrive/GladosFiles/wavs/{count}.wav|{line}\n"
        count += 1
    except:
        break
f.close()

f = open("C:/Users/thetr/Documents/Glados/list.txt", "w")
print("opened")
f.write(string)
f.close()
