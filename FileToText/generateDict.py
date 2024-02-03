from functions import numConvert

characters = []

for code_point in range(0x255):
    try:
        character = chr(code_point)
        character.encode('utf-8')
        #print(character, end=' ')
        characters.append(character)
    except UnicodeEncodeError:
        pass

print(characters[302::13])
#print(len(characters))
'''
newList = []

for i in range(256):
    newList.append(characters[-1])
    del characters[-1]

count = 0
with open("FileToText/Conversions.txt", "w", encoding='utf-8') as f:
    f.write("numConvert = {\n")
    for items in newList:
        f.write(f"  '{count}':'{items}',\n")
        count += 1
    f.write("}\n\n")

    count = 0

    f.write("symbolConvert = {\n")
    for items in newList:
        f.write(f"  '{items}':'{count}',\n")
        count += 1
    f.write("}\n\n")

    f.write("string = '")
    for items in newList:
        f.write(items)
    f.write("'\n\n")
'''