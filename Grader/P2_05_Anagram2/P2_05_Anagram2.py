str1=input()
str2=input()

hsh1={}
hsh2={}

for i in range(0,26):
    hsh1[chr(ord("a")+i)]=0
    hsh2[chr(ord("a")+i)]=0

for i in str1.lower():
    if "a"<=i<="z":
        hsh1[i]+=1
for i in str2.lower():
    if "a"<=i<="z":
        hsh2[i]+=1

print(str1)
empty=True
for i in range(0,26):
    char=chr(ord("a")+i)
    if (hsh1[char]>hsh2[char]):
        empty=False
        diff=hsh1[char]-hsh2[char]
        print(" - remove",diff,char+("'s" if diff>1 else ""))
if empty:
    print(" - None")
print(str2)
empty=True
for i in range(0,26):
    char=chr(ord("a")+i)
    if (hsh2[char]>hsh1[char]):
        empty=False
        diff=hsh2[char]-hsh1[char]
        print(" - remove",diff,char+("'s" if diff>1 else ""))
if empty:
    print(" - None")