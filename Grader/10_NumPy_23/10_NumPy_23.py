import numpy as np

def read_data():

    w=[float(e) for e in input().split()]
    weight=np.array(w)
    n=int(input())
    data=np.ndarray((n,4),int)
    for i in range(n):
        data[i]=[int(e) for e in input().split()]
    return weight,data

def report_lower_than_mean(weight,data):
    studentData=np.array(data,float)
    studentData[:,1]*=weight[0]
    studentData[:,2]*=weight[1]
    studentData[:,3]*=weight[2]
    meanScore=studentData[:,1:4].sum()/len(studentData)
    lowerThanMean=studentData[studentData[:,1:4].sum(axis=1)<meanScore,0]
    lowerThanMean=np.array(lowerThanMean,int)
    lowerThanMean=np.array(lowerThanMean,str)
    if (len(lowerThanMean)>0):
        print(", ".join(lowerThanMean))
    else:
        print("None")

exec(input().strip())