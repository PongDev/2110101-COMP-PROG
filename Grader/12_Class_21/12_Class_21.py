class Complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        if self.b==0:
            return str(self.a)
        elif self.a==0:
            if abs(self.b)==1:
                return ("-" if self.b<0 else "")+"i"
            else:
                return str(self.b)+"i"
        elif abs(self.b)==1:
            return "{}{}i".format(str(self.a),("+" if self.b>0 else "-"))
        else:
            return "{}{}{}i".format(str(self.a),("+" if self.b>0 else "-"),str(abs(self.b)))
    def __add__(self,rhs):
        return Complex(self.a+rhs.a,self.b+rhs.b)
    def __mul__(self,rhs):
        return Complex((self.a*rhs.a)-(self.b*rhs.b),(self.a*rhs.b)+(self.b*rhs.a))
    def __truediv__(self,rhs):
        return Complex(((self.a*rhs.a)+(self.b*rhs.b))/((rhs.a**2)+(rhs.b**2)),(((-self.a)*rhs.b)+(self.b*rhs.a))/((rhs.a**2)+(rhs.b**2)))

t,a,b,c,d=[int(x) for x in input().split()]
c1=Complex(a,b)
c2=Complex(c,d)
if   t==1:print(c1)
elif t==2:print(c2)
elif t==3:print(c1+c2)
elif t==4:print(c1*c2)
else     :print(c1/c2)