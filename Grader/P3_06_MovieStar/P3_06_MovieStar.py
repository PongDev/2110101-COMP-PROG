actorMovie={}

n=int(input())

for i in range(n):
    data=[e.strip() for e in input().split(",")]
    if data[1] not in actorMovie:
        actorMovie[data[1]]=[]
    if data[2] not in actorMovie:
        actorMovie[data[2]]=[]
    actorMovie[data[1]].append(data[0])
    actorMovie[data[2]].append(data[0])
for q in [e.strip() for e in input().split(",")]:
    if q in actorMovie:
        print(q,"->",", ".join(actorMovie[q]))
    else:
        print(q,"->","Not found")