n=int(input())

translator={}
for i in range(n):
    data=input().split()
    translator[data[2]]=data[0]+" "+data[1]
    translator[data[0]+" "+data[1]]=data[2]

m=int(input())

for i in range(m):
    query=input()
    if query in translator:
        print(query,"-->",translator[query])
    else:
        print(query,"--> Not found")