path={}

while True:
    data=input().split()
    if len(data)==2:
        if data[0] not in path:
            path[data[0]]=set()
        if data[1] not in path:
            path[data[1]]=set()
        path[data[0]].add(data[1])
        path[data[1]].add(data[0])
    else:
        ans={data[0]}

        if data[0] in path:
            for station in path[data[0]]:
                ans.add(station)
                if station in path:
                    for station2 in path[station]:
                        ans.add(station2)
        for i in sorted(ans):
            print(i)
        break