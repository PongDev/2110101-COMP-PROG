def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def is_coprime(a,b,c):
    return gcd(gcd(a,b),c)==1

def primitive_Pythagorean_triples(max_len):
    triple=[]

    for a in range(1,max_len+1):
        for b in range(a,max_len+1):
            for c in range(b,max_len+1):
                if ((a**2)+(b**2)==(c**2) and is_coprime(a,b,c)):
                    triple.append([c,a,b])
    triple=[[a,b,c] for c,a,b in sorted(triple)]
    return triple

exec(input().strip())