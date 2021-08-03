i=input()
length=len(i)
if (length!=10):
    print("Not a mobile number")
else:
    if (i[:2]=="06"):
        print("Mobile number")
    elif (i[:2]=="08"):
        print("Mobile number")
    elif (i[:2]=="09"):
        print("Mobile number")
    else:
        print("Not a mobile number")