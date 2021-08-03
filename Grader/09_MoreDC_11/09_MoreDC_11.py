def countLeading(data,lead):
    r=0

    for i in data:
        if i==lead:
            r+=1
        else:
            break
    return r

n=int(input())
for i in range(n):
    data=input()
    print(data[countLeading(data,".")//2:])