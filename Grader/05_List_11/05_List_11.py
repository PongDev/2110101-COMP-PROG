data = input()

ansList = []
for i in range(10):
    if str(i) not in data:
        ansList.append(str(i))
if (len(ansList) == 0):
    print("None")
else:
    print(",".join(ansList))
