n = int(input())

data = []
for i in range(1, n+1):
    pos = input().split()
    posx = float(pos[0])
    posy = float(pos[1])
    data.append([((posx**2)+(posy**2))**0.5, i, [posx, posy]])
data.sort()
print("#"+str(data[2][1])+": ("+str(data[2][2][0])+", "+str(data[2][2][1])+")")
