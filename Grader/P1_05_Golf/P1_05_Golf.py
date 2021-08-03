parSum=0
strokeSum=0
modifyStrokeSum=0

for i in range(9):
    par,stroke,select=[int(e) for e in input().split()]
    parSum+=par
    strokeSum+=stroke
    if (select==1):
        modifyStroke=min(stroke,par+2)
        modifyStrokeSum+=modifyStroke
pointDiff=0.8*((1.5*modifyStrokeSum)-parSum)
if (pointDiff==int(pointDiff) or pointDiff>=0):
    pointDiff=int(pointDiff)
else:
    pointDiff=int(pointDiff)-1
    
finalScore=strokeSum-pointDiff
print(strokeSum)
print(pointDiff)
print(finalScore)