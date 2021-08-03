data=input()

ans=""
for i in data:
    if (i=="("):
        ans+="["
    elif (i==")"):
        ans+="]"
    elif (i=="["):
        ans+="("
    elif (i=="]"):
        ans+=")"
    else:
        ans+=i
print(ans)