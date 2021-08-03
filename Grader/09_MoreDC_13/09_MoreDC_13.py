n=int(input())

allTeam=set()
lostTeam=set()
for i in range(n):
    data=input().split()
    allTeam.add(data[0])
    allTeam.add(data[1])
    lostTeam.add(data[1])
print(sorted(allTeam-lostTeam))