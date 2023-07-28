file = "Abadox: E/gr*ie?|"

#file[i] == ":":# or (file[i] == "/") or (file[i] == "?") or (file[i] == "*") or (file[i] == '"') or (file[i] == "<") or (file[i] == ">") or (file[i] == "|"):

for character in file:
    print(character)
    if character == ":":
        file = list(map(lambda x: x.replace(":", ""), list(file)))
    elif character == "/":
        file = list(map(lambda x: x.replace("/", ""), list(file)))
    elif character == "?":
        file = list(map(lambda x: x.replace("?", ""), list(file)))
    elif character == "*":
        file = list(map(lambda x: x.replace("*", ""), list(file)))
    elif character == '"':
        file = list(map(lambda x: x.replace('"', ""), list(file)))
    elif character == "<":
        file = list(map(lambda x: x.replace("<", ""), list(file)))
    elif character == ">":
        file = list(map(lambda x: x.replace(">", ""), list(file)))
    elif character == "|":
        file = list(map(lambda x: x.replace("|", ""), list(file)))
    file = "".join(file)

print(file)
'''
if ":" in file: #or ("/" in file) or ("?" in file) or ("*" in file) or ('"' in file) or ("<" in file) or (">" in file) or ("|" in file):
        file = list(file)
        print(file)
        for i in range(len(file)):
            print(file[i], i)
            if file[i] == ":":# or (file[i] == "/") or (file[i] == "?") or (file[i] == "*") or (file[i] == '"') or (file[i] == "<") or (file[i] == ">") or (file[i] == "|"):
                del file[i]
        file = "".join(file)
print(file)
'''