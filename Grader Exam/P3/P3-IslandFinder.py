def fill(plate,floor,x,y):
    if 0<=x<len(floor) and 0<=y<len(floor[0]) and floor[x][y] and not plate[x][y]:
        plate[x][y]=True
        fill(plate,floor,x+1,y)
        fill(plate,floor,x-1,y)
        fill(plate,floor,x,y+1)
        fill(plate,floor,x,y-1)

mode=input().strip().upper()
c,r,h=[int(e) for e in input().split(",")]
topView=[[False for j in range(c)] for i in range(r)]
lastFloor=None
ans=[]
for k in range(h):
    floor=[]
    for i in range(r):
        floor.append(list(input().strip().upper()))
    floor=[[True if floor[i][j]=="X" else False for j in range(c)] for i in range(r)]
    if lastFloor!=None:
        plate=[[False for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if lastFloor[i][j]:
                    fill(plate,floor,i,j)
        for i in range(r):
            for j in range(c):
                if floor[i][j]==True and plate[i][j]==False:
                    ans.append((k,"I" if topView[i][j] else "M",i,j))
    lastFloor=floor
    topView=[[topView[i][j] or floor[i][j] for j in range(c)] for i in range(r)]
ans.sort()
if len(ans)==0:
    print("There is no island")
else:
    for i in ans:
        if mode=="N":
            print("{},{},{}".format(i[0],i[2],i[3]))
        elif mode=="Y":
            print("{},{},{},{}".format(i[0],i[1],i[2],i[3]))