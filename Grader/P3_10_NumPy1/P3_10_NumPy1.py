import numpy as np

def eq(A,B,p):
    return np.sum(A==B)>=(p/100)*np.product(A.shape)

def closest_point_indexes(points,p):
    tmp=np.array(np.sqrt(((points[:,0]-p[0])**2)+((points[:,1]-p[1])**2)))
    return np.arange(len(points))[tmp==tmp.min()]

def number_of_inversions(A):
    r=0

    for i in range(len(A)):
        r+=np.sum(A[i:]<A[i])
    return r

exec(input().strip())