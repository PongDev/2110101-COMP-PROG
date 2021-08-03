bidData={}
buyerData={}
n=int(input())

for i in range(n):
    inputData=input().split()
    if len(inputData)==4:
        mode,buyer,product,price=inputData
        price=int(price)
        if product not in bidData:
            bidData[product]={}
        bidData[product][buyer]=[-price,i]
    elif len(inputData)==3:
        mode,buyer,product=inputData
        if product not in bidData:
            bidData[product]={}
        if buyer in bidData[product]:
            bidData[product].pop(buyer)
    if buyer not in buyerData:
        buyerData[buyer]=[0]

for product in bidData:
    price=0
    winner=""
    for buyer in bidData[product]:
        if price==0 or bidData[product][buyer]<price:
            price=bidData[product][buyer]
            winner=buyer
    if price!=0:
        buyerData[winner][0]+=-price[0]
        buyerData[winner].append(product)

for buyer in sorted(buyerData):
    buyerOutput=buyer+": $"+str(buyerData[buyer][0])
    if len(buyerData[buyer])>1:
        buyerOutput+=" -> "+" ".join(sorted(buyerData[buyer][1:]))
    print(buyerOutput)