with open("rngManipulation/data.txt", "r") as f:
    rand = f.readline().split("|")
    del rand[-1]
    rand = rand + f.readline().split("|")
    del rand[-1]
    rand = rand + f.readline().split("|")
    del rand[-1]

    f.readline()

    even = f.readline().split("|")
    del even[-1]
    even = even + f.readline().split("|")
    del even[-1]
    even = even + f.readline().split("|")
    del even[-1]

    f.readline()

    odd = f.readline().split("|")
    del odd[-1]
    odd = odd + f.readline().split("|")
    del odd[-1]
    odd = odd + f.readline().split("|")
    del odd[-1]

randDist = [0,0] #even, odd
evenDist = [0,0]
oddDist = [0,0]

for items in rand:
    if int(items) % 2 == 0:
        randDist[0] += 1
    else:
        randDist[1] += 1

for items in even:
    if int(items) % 2 == 0:
        evenDist[0] += 1
    else:
        evenDist[1] += 1

for items in odd:
    if int(items) % 2 == 0:
        oddDist[0] += 1
    else:
        oddDist[1] += 1

print(f"RandDist = {randDist}\nevenDist = {evenDist}\noddDist = {oddDist}")