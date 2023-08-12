string = ""
f = open("C:/Users/thetr/Documents/Python/Glados/output.txt", "r")
while True:
    try:
        line = f.readline().split("|")
        prefix = str(line[0].split("/")[3]) + "/" + str(line[0].split("/")[4])
        line = prefix + "|" + str(line[1])
        string = f"{string}{line}"
    except:
        break
f.close()

f = open("C:/Users/thetr/Documents/Glados/list.txt", "w")
f.write(string)
f.close()