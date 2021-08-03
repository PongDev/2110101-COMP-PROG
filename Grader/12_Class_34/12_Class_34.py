class piggybank:
    def __init__(self):
        self.coins={}
        self.count=0
        self.money=0.0
    
    def add(self,v,n):
        if self.count+n>100:
            return False
        else:
            v=float(v)
            self.count+=n
            self.money+=v*n
            if v not in self.coins:
                self.coins[v]=0
            self.coins[v]+=n
            return True
    
    def __float__(self):
        return float(round(self.money,2))
    
    def __str__(self):
        r="{"

        for key,value in sorted(self.coins.items()):
            if len(r)!=1:
                r+=", "
            r+=str(key)+":"+str(value)
        r+="}"
        return r

cmd1=input().split(';')
cmd2=input().split(';')
p1=piggybank();p2=piggybank()
for c in cmd1:eval(c)
for c in cmd2:eval(c)