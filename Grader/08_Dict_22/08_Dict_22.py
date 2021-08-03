n=int(input())
iceCreamPrice={}
for i in range(n):
    data=input().split()
    iceCreamPrice[data[0]]=float(data[1])
m=int(input())
remIceCreamSale={}
topSaleList=[]
topSalePrice=0
totalSale=0
for i in range(m):
    data=input().split()
    if data[0] in iceCreamPrice:
        income=iceCreamPrice[data[0]]*int(data[1])
        totalSale+=income
        if data[0] in remIceCreamSale:
            remIceCreamSale[data[0]]+=income
        else:
            remIceCreamSale[data[0]]=income
        if (remIceCreamSale[data[0]]>topSalePrice):
            topSalePrice=remIceCreamSale[data[0]]
            topSaleList=[data[0]]
        elif (remIceCreamSale[data[0]]==topSalePrice):
            topSaleList.append(data[0])
if totalSale==0:
    print("No ice cream sales")
else:
    print("Total ice cream sales:",totalSale)
    print("Top sales:",", ".join(sorted(topSaleList)))