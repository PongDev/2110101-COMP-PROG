str1=input()
str2=input()

if (len(str1)!=len(str2)):
    print("Incomplete answer")
else:
    ans=0
    for i in range(len(str1)):
        if (str1[i]==str2[i]):
            ans+=1
    print(ans)