f = open("C:/Users/thetr/Documents/Python/DiscordBot/dict.txt", "r", encoding="utf-8")
text = f.readlines()
f.close()

#f = open("C:/Users/thetr/Documents/Python/DiscordBot/feedback.txt", "w")
#f.write("")
#f.close()

count = 0
line = ""

for items in text:
    line = text[count].split("|")
    if (float(len(line[2])) * 2.5) < float(len(line[3])):
        pass
        #f = open("C:/Users/thetr/Documents/Python/DiscordBot/feedback.txt", "a")
        #f.write(str(count) + "\n")
        #f.close()
    count += 1