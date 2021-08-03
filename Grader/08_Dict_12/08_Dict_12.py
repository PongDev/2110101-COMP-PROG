n=int(input())
translator={}
for i in range(n):
    data=input().split()
    translator[data[0]]=data[1]
    translator[data[1]]=data[0]
m=int(input())
for i in range(m):
    query=input()
    if query in translator:
        print(translator[query])
    else:
        print("Not found")