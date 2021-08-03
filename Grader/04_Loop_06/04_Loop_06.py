n=int(input())

for i in range(n-1):
    line=""
    line+=(" "*(n-i-1))+"*"
    if ((i*2)-1>0):
        line+=(" "*((i*2)-1))+"*"
    print(line)
print("*"*((2*n)-1))