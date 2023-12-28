roc = .2 #rate of change
maxValue = 100 #the highest value before it goes down
notes = [] #actual note values
change = [] #listed rate of change for each note value
flip = [] # 1 if it increases, 0 if it decreases

for i in range(20):
  i=i
  notes.append(1)
  flip.append(1)

multiply = 1
while multiply > 0:
  change.append(round(roc * multiply, 2))
  multiply -= .05
change[0] = 1

print(f"change = {change}\nnotes = {notes}\nflip = {flip}")

for i in range(len(notes)):
    if flip[i] == 1:
        notes[i] += change[i]
    else:
       notes[i] -= change[i]
    
    if notes[i] >= maxValue:
       notes[i] = maxValue
       flip[i] = 0
    elif notes[i] <= 0:
       notes[i] = 0
       flip[i] = 1

print("\n\n")
print(f"change = {change}\nnotes = {notes}\nflip = {flip}")