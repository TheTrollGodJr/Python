count = 1
while True:
    print(count)
    inp = input("")
    if inp != "":
        count += int(inp)
    elif inp == "exit":
        break
    else:
        count += 1