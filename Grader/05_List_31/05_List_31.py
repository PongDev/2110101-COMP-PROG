data = input().split()
mode = input()

for i in mode:
    if (i == "C"):
        data = data[len(data)//2:]+data[:len(data)//2]
    elif (i == "S"):
        tmp = []
        for i in range(len(data)//2):
            tmp.append(data[i])
            tmp.append(data[(len(data)//2)+i])
        data = tmp
print(" ".join(data))
