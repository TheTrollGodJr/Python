def change(inp):
    count = [0,0]
    characters = [chr(ord('a') + i) for i in range(26)]
    characters.append(" ")
    characters.append(".")
    string = ""
    inp = inp.lower()
    inp = list(inp)
    for i in range(len(inp)):
        while True:
            if inp[i] == characters[count[0]]:
                string = f"{string}{count[1]}{i}"
                count[1] = 0
                break
            else:
                count[0] += 1
                count[1] += 1
                if count[0] == 28:
                    count[0] = 0
    return string

tokenA = "205121218318455216207248139110101125121713131411581621171618101925206211422123192421251726427202822292130233183263317341435233693713823390401419421343844845254620472448"
tokenB = "20512121831845521620724813911010112512171313141158162117161810192520621142212319242125172642720282229213023318326331734143523369371382339040141942134384484525462047"