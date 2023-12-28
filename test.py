import random

nums = []
for i in range(1, 100):
    nums.append(i)

evens = []
odds = []

for items in nums:
    if items % 2 == 0:
        evens.append(str(items))
    else:
        odds.append(str(items))

evenString = ""
for i in range(5000):
    evenString = f"{evenString} {random.choice(evens)}"

oddString = ""
for i in range(5000):
    oddString = f"{oddString} {random.choice(odds)}"

with open("odds.txt", "w") as f:
    f.write(oddString)

with open("evens.txt", "w") as f:
    f.write(evenString)