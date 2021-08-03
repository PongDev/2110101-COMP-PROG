playerScore=[0]*2
ballScore={
    "R":1,
    "Y":2,
    "G":3,
    "W":4,
    "B":5,
    "P":6,
    "K":7
}

redLeft=6
otherLeft=6
phase=1

while True:
    data=list(input())
    data[0]=int(data[0])-1
    for i in data[1:]:
        if i!="X":
            if phase==1 and i=="R":
                redLeft-=1
            elif phase==2:
                otherLeft-=1
            playerScore[data[0]]+=ballScore[i]
    if phase==1 and redLeft==0:
        phase=2
    elif phase==2 and otherLeft==0:
        print(playerScore[0],playerScore[1])
        if (playerScore[0]==playerScore[1]):
            print("Tie")
        else:
            print("Player",1 if playerScore[0]>playerScore[1] else 2,"wins")
        break