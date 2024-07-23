import keyboard

def checkIndex(array=list, pointer=int):
    try:
        value = array[pointer]
    except IndexError:
        array.append(0)
    return array

def waitForKey():
    key =  keyboard.read_key()
    while True:
        if keyboard.is_pressed(key): continue
        else: break
    return ord(key)

if __name__ == "__main__":

    file = "brainfProjects/programs/test.txt"

    with open(file, "r") as f:
        code = f.read()

    array = [0]
    loopIndexes = []
    pointer = 0
    count = 0

    while True:
        try:
            item = code[count]
        except:
            break

        if item == ">":
            pointer += 1
            checkIndex(array, pointer)
        elif item == "<":
            if pointer != 0: pointer -= 1
        elif item == "+" and array[pointer] < 255: array[pointer] += 1
        elif item == "-":
            array[pointer] -= 1
            if array[pointer] < 0:
                array[pointer] = 255
        elif item == ",": array[pointer] = waitForKey()
        elif item == ".": print(chr(array[pointer]), end="")
        elif item == "[": 
            if array[pointer] != 0: loopIndexes.append([pointer, count])
        elif item == "]":
            if array[loopIndexes[-1][0]] > 0:
                pointer = loopIndexes[-1][0]
                count = loopIndexes[-1][1]
            else:
                del loopIndexes[-1]
        count += 1
    print("\n", array[pointer])