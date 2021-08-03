m=int(input())

p1Score=0
p2Score=0
gameID=0

while True:
    data=input().split()
    if (data[0]=="R" and data[1]=="S"):
        p1Score+=1
    elif (data[0]=="R" and data[1]=="P"):
        p2Score+=1
    elif (data[0]=="S" and data[1]=="P"):
        p1Score+=1
    elif (data[0]=="S" and data[1]=="R"):
        p2Score+=1
    elif (data[0]=="P" and data[1]=="R"):
        p1Score+=1
    elif (data[0]=="P" and data[1]=="S"):
        p2Score+=1
    gameID+=1

    if (p1Score==m):
        print(p1Score,p2Score)
        print("Player 1 wins")
        break
    elif (p2Score==m):
        print(p1Score,p2Score)
        print("Player 2 wins")
        break
    elif (gameID>=3*m):
        print(p1Score,p2Score)
        print("Tie")
        break