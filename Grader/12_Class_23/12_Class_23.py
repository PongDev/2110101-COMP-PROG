class Card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
    def __str__(self):
        return "({} {})".format(self.value,self.suit)
    def next1(self):
        if self.suit=="spade":
            valueList=["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
            return Card(valueList[(valueList.index(self.value)+1)%len(valueList)],"club")
        else:
            suitList=["club","diamond","heart","spade"]
            return Card(self.value,suitList[suitList.index(self.suit)+1])
    def next2(self):
        next=self.next1()
        self.value=next.value
        self.suit=next.suit

n=int(input())
cards=[]
for i in range(n):
    value,suit=input().split()
    cards.append(Card(value,suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])