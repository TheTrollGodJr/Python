import random

def rng(dataPoints):
    string = ""
    for i in range(dataPoints):
        string = f"{string}{random.randint(1,100)}|"
    return string

randomOutput = f"{rng(50)}\n{rng(50)}\n{rng(50)}"

input("e1")
evenOutput = f"{rng(50)}\n"
input("e2")
evenOutput = f"{evenOutput}{rng(50)}\n"
input("e3")
evenOutput = f"{evenOutput}{rng(50)}\n"

input("o1")
oddOutput = f"{rng(50)}\n"
input("o2")
oddOutput = f"{oddOutput}{rng(50)}\n"
input("o3")
oddOutput = f"{oddOutput}{rng(50)}\n"

with open("rngManipulation/data.txt", "w") as f:
    f.write(f"{randomOutput}\n\n{evenOutput}\n{oddOutput}")