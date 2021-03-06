def knows(R,x,y):
    return y in R[x]

def is_celeb(R,x):
    for member in R:
        if member!=x and (not knows(R,member,x)):
            return False
    if len(R[x])==0 or (len(R[x])==1 and x in R[x]):
        return True
    else:
        return False

def find_celeb(R):
    for x in R:
        if is_celeb(R,x):
            return x
    return None

def read_relations():
    R=dict()
    while True:
        d=input().split()
        if len(d)==1:break
        if d[0] not in R:
            R[d[0]]=set()
        if d[1] not in R:
            R[d[1]]=set()
        R[d[0]].add(d[1])
    return R

def main():
    R=read_relations()
    c=find_celeb(R)
    if c==None:
        print('Not Found')
    else:
        print(c)

exec(input().strip())