def toMorse():
    inp = input("")
    output = ""

    for item in inp:
        if item == "t" or item == "f":
            output += "-"
        elif item == "i" or item == "j":
            output += "."
        elif item == "/":
            output += "/"
    print(output)

def fromMorse():
    inp = input("")
    lineSwap = True
    dotSwap = True
    output = ""

    for item in inp:
        if item == "-":
            if lineSwap:
                output += "t"
            else:
                output += "f"
        elif item == ".":
            if dotSwap:
                output += "i"
            else:
                output += "j"
        elif item == "/":
            output += "/"
        elif item == " ":
            output += " "

        if lineSwap:
            lineSwap = False
        else:
            lineSwap = True
        
        if dotSwap:
            dotSwap = False
        else:
            dotSwap = True

    print(output)

if __name__ == "__main__":
    fromMorse()