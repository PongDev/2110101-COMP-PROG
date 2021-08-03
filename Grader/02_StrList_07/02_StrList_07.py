data=input()
num1=data[3:32:7]
num2=data[7:28:5]
sum=str(int(num1)+int(num2)+10000)
ans=sum[-4:-1]
num3=((int(sum[-2])+int(sum[-3])+int(sum[-4]))%10)+1
if (num3==1):
    ans+="A"
if (num3==2):
    ans+="B"
if (num3==3):
    ans+="C"
if (num3==4):
    ans+="D"
if (num3==5):
    ans+="E"
if (num3==6):
    ans+="F"
if (num3==7):
    ans+="G"
if (num3==8):
    ans+="H"
if (num3==9):
    ans+="I"
if (num3==10):
    ans+="J"
print(ans)