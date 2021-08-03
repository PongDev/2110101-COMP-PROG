ZigZagMin=None
ZigZagMax=None
ZagZigMin=None
ZagZigMax=None
mode=True

while True:
    data=input().split()
    if (data[0]=="Zig-Zag"):
        print(ZigZagMin,ZigZagMax)
        break
    elif (data[0]=="Zag-Zig"):
        print(ZagZigMin,ZagZigMax)
        break
    left=int(data[0])
    right=int(data[1])
    if (mode):
        ZigZagMin=min(ZigZagMin if ZigZagMin!=None else left,left)
        ZigZagMax=max(ZigZagMax if ZigZagMax!=None else right,right)
        ZagZigMin=min(ZagZigMin if ZagZigMin!=None else right,right)
        ZagZigMax=max(ZagZigMax if ZagZigMax!=None else left,left)
    else:
        ZigZagMin=min(ZigZagMin if ZigZagMin!=None else right,right)
        ZigZagMax=max(ZigZagMax if ZigZagMax!=None else left,left)
        ZagZigMin=min(ZagZigMin if ZigZagMin!=None else left,left)
        ZagZigMax=max(ZagZigMax if ZigZagMax!=None else right,right)
    mode=not mode