def T2M(pattern,text):
    morse = ''
    for e in text :
        j = pattern.find('[' + e + ']')
        if j==-1:
            return "Invalid : "+text
        j += 3
        k = pattern.find('[',j)
        morse += pattern[j:k] + ' '
    return morse.strip()

def M2T(pattern,codeList):
    r=""

    for code in codeList:
        idx=pattern.find("]"+code+"[")
        if idx==-1:
            return "Invalid : "+" ".join(codeList)
        r+=pattern[idx-1]
    return r

filename=input()

fp=open(filename,"r")
mode=fp.readline().strip()
pattern=fp.readline().strip()
if (mode=="T2M"):
    for line in fp:
        print(T2M(pattern,line.strip()))
elif (mode=="M2T"):
    for line in fp:
        print(M2T(pattern,line.strip().split()))
else:
    print("Invalid code")
fp.close()