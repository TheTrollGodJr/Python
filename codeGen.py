import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = []
for i in range(6):
    nums.append(random.randint(0,25))

string = ""
for num in nums:
    string = f"{string}{letters[num]}"

f = open("code.txt", "w")
f.write(string)
f.close()

for i in range(6):
    print(string[i])
    inp = input("")
    print("\n\n\n\n\n\n\n\n\n\n\n\n")