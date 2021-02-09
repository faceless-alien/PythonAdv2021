def HemmingDistance(a, b):
    res=0
    for i in len(a):
        if a[i]!=b[i]:
            res+=1
    return res
