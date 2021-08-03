data=input()
if data[-1]=="s" or data[-1]=="x" or data[-2:]=="ch":
    print(data+"es")
elif data[-1]=="y" and (data[-2] not in "aeiou"):
    print(data[:-1]+"ies")
else:
    print(data+"s")