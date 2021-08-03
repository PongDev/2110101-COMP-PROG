def verifyDNA(DNA):
    for i in DNA:
        if i not in "ATGC":
            return False
    return True

DNA=input().strip().upper()
cmd=input()

if verifyDNA(DNA):
    if cmd=="R":
        original="ATGC"
        transfer="TACG"
        newDNA=""
        for i in DNA:
            newDNA+=transfer[original.find(i)]
        newDNA=newDNA[::-1]
        print(newDNA)
    elif cmd=="F":
        print("A={}, T={}, G={}, C={}".format(DNA.count("A"),DNA.count("T"),DNA.count("G"),DNA.count("C")))
    elif cmd=="D":
        cmd=input()
        r=0
        for i in range(len(DNA)-1):
            if (DNA[i:i+2]==cmd):r+=1
        print(r)
else:
    print("Invalid DNA")