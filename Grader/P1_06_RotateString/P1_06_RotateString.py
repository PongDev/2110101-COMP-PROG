mode=input().strip()
row=int(input().strip())
col=0
invalid=False
data=""
for i in range(row):
    inputData=input().strip()
    if (i==0):
        col=len(inputData)
    elif (col!=len(inputData)):
        invalid=True
    data+=inputData
if (invalid):
    print("Invalid size")
else:
    if (mode=="90"):
        for i in range(col):
            for j in range(row):
                print(data[((row-j-1)*col)+i],end="")
            print()
    elif (mode=="flip"):
        for i in range(row):
            print(data[i*col:(i*col)+col][::-1])
    elif (mode=="180"):
        for i in range(row):
            print(data[(row-i-1)*col:((row-i-1)*col)+col][::-1])