def isNumber(num):
    if len(num)==0:return False
    
    number="0123456789"
    for i in num:
        if i not in number:
            return False
    else:return True

def getAns(row,col):
    invalidCol=False
    invalidRow=False
    if row=="" or len(row)>1:
        invalidRow=True
    else:
        row="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".find(row)
        if row==-1:invalidRow=True
    if not isNumber(col):
        invalidCol=True
    else:
        col=int(col)
        if (col<1 or col>52):invalidCol=True
    if invalidRow and invalidCol:
        return "Invalid row and column"
    elif invalidRow:
        return "Invalid row"
    elif invalidCol:
        return "Invalid column"
    else:
        return "Black" if row%2==col%2 else "White"

data=input().strip()
if len(data)<=3:
    print(getAns(data[0].strip(),data[1:].strip()))
else:
    validCode=" 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    row=""
    col=""

    pos=0
    pos=data.find("row",pos)+len("row")
    pos=data.find("=",pos)+len("=")
    while pos<len(data) and data[pos] in validCode:
        row+=data[pos]
        pos+=1
    row=row.strip()

    pos=0
    pos=data.find("col",pos)+len("col")
    pos=data.find("=",pos)+len("=")
    while pos<len(data) and data[pos] in validCode:
        col+=data[pos]
        pos+=1
    col=col.strip()

    print(getAns(row,col))