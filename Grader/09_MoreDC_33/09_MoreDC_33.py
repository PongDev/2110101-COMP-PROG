def add_poly(p1,p2):
    r={power:num for num,power in p1}

    for num,power in p2:
        if power not in r:
            r[power]=num
        else:
            r[power]+=num
    return [(num,power) for power,num in sorted(r.items(),reverse=True) if num!=0]

def mult_poly(p1,p2):
    r={}

    for i in p1:
        for j in p2:
            num=i[0]*j[0]
            power=i[1]+j[1]
            if power not in r:
                r[power]=num
            else:
                r[power]+=num
    return [(num,power) for power,num in sorted(r.items(),reverse=True) if num!=0]

for i in range(3):
    exec(input().strip())