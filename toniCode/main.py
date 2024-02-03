import random

'''
all this does though is open each of the files and copy each line into a list for each file.
the original file for commands.txt wasn't a text file but I put all of the stuff in it in a text file, I dont know -
    how your going to deal with that but you can figure that out.
'''

with open("toniCode/firstnames.txt", "r") as f:
    firstnames = f.readlines()

with open("toniCode/surnames.txt", "r") as f:
    surnames = f.readlines()

with open("toniCode/commands.txt", "r") as f:
    commands = f.readlines()

# this is an argument passed when you start the program; change that however you need
recordCount = 1

# declaring an initializing variable
#refer = [["", ""]]
refer = {"":""}
line = ""

# updates the refer list if a new value is present or updates an existing value
def updateRefer(varName, value):
    global refer
    itemFound = False
    for items in refer:
        if items[0] == varName:
            items[1] = value
            itemFound = True
    if itemFound == False:
        refer.append([varName, value])

# makes things like \n and \t write correctly
def fixEscapeCharcters(inp):
    inp = inp.replace("\\n", "\n")
    inp = inp.replace("\\t", "\t")
    inp = inp.replace('\\"', '\"')
    return inp

# loop for the number specified in the arguments
for i in range(recordCount):
    #loops through commands
    for item in commands:
        # if command is HEADER
        if "HEADER" in item:
            # write the header
            header = fixEscapeCharcters(item.split(' ', 1)[1][1:len(item.split(' ', 1)[1]) - 2])
        
        #writes given string value
        elif "STRING" in item:
            # add the string to the line
            splitChar = item[7]
            line = f"{line}{fixEscapeCharcters(item.split(splitChar)[1])}"

        #writes random name
        elif "WORD" in item:
            #writes random firstname
            if "firstname" in item:
                # choose a random item from firstnames and add it to the current line
                fName = random.choice(firstnames).replace("\n", "")
                print(fName)
                line = f"{line}{fName}"
                refer.update({item.split(" ")[1]:fName})
            
            #writes random surname
            else:
                # choose a random item from surnames and add it to the current line
                sName = random.choice(surnames).replace("\n", "")
                print(sName)
                line = f"{line}{sName}"
                refer.update({item.split(" ")[1]:sName})

        #writes a random number within the given range        
        elif "INTEGER" in item:
            # generate a random number between the min and max specified
            num = random.randint(int(item.split(" ")[2]), int(item.split(" ")[3]))
            # Im assuming it wants me to output the generated number intot the line but it doesnt say anywhere so idk
            line = f"{line}{num}"
            refer.update({item.split(" ")[1]:str(num)})
        
        #goes to the refer list to find the value to wright
        elif "REFER":
            reference = refer[item.split(' ')[1].replace('\n', '')]
            line = f"{line}{reference}"
        #print(refer)

#writes output file
with open("toniCode/output.txt", "w") as f:
    f.write(header)
    f.write(line)
