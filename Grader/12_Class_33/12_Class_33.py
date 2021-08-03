class piggybank:
    def __init__(self):
        self.c1=0
        self.c2=0
        self.c5=0
        self.c10=0
        self.money=0

    def add1(self,n):
        self.c1+=n
        self.money+=n

    def add2(self,n):
        self.c2+=n
        self.money+=n*2

    def add5(self,n):
        self.c5+=n
        self.money+=n*5

    def add10(self,n):
        self.c10+=n
        self.money+=n*10

    def __int__(self):
        return self.money

    def __lt__(self,rhs):
        return self.money<rhs.money

    def __str__(self):
        return "{{1:{}, 2:{}, 5:{}, 10:{}}}".format(self.c1,self.c2,self.c5,self.c10)
        # return f"{{1:{self.c1}, 2:{self.c2}, 5:{self.c5}, 10:{self.c10}}}"

cmd1=input().split(";")
cmd2=input().split(";")
p1=piggybank();p2=piggybank()
for c in cmd1:eval(c)
for c in cmd2:eval(c)