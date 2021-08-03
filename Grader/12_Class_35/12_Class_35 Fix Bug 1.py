class roman:
    def __init__(self,r):
        romanNumber={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

        self.str=r
        self.int=0

        ptr=0
        while ptr<len(self.str):
            if ptr==len(self.str)-1:
                self.int+=romanNumber[self.str[ptr]]
                break
            if romanNumber[self.str[ptr]]<romanNumber[self.str[ptr+1]]:
                self.int+=romanNumber[self.str[ptr+1]]-romanNumber[self.str[ptr]]
                ptr+=1
            else:
                self.int+=romanNumber[self.str[ptr]]
            ptr+=1
    
    def __lt__(self,rhs):
        return self.int<rhs.int
    
    def __str__(self):
        return self.str
    
    def __int__(self):
        return self.int
    
    def __add__(self,rhs):
        num=self.int+rhs.int
        r=""

        if (num>1000):
            r+="M"*(num//1000)
            num%=1000
        if (num>100):
            if (num//100>=5):
                if (num//100==9):
                    r+="CM"
                else:
                    r+="D"+(((num//100)-5)*"C")
            else:
                if (num//100==4):
                    r+="CD"
                else:
                    r+=(num//100)*"C"
            num%=100
        if (num>10):
            if (num//10>=5):
                if (num//10==9):
                    r+="XC"
                else:
                    r+="L"+(((num//10)-5)*"X")
            else:
                if (num//10==4):
                    r+="XL"
                else:
                    r+=(num//10)*"X"
            num%=10
        if (num>0):
            if (num>=5):
                if (num==9):
                    r+="IX"
                else:
                    r+="V"+((num-5)*"I")
            else:
                if (num==4):
                    r+="IV"
                else:
                    r+=num*"I"
        return roman(r)

t,r1,r2=input().split()
a=roman(r1);b=roman(r2)
if   t=='1':print(a<b)
elif t=='2':print(int(a),int(b))
elif t=='3':print(str(a),str(b))
elif t=='4':print(int(a+b))
else       :print(str(a+b))