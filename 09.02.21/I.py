def sum(a):
    res=0
    for i in a:
        res+=i
    return res
def mean(a):
    res=0
    c=0
    for i in a:
        res+=i
        c+=1
    return round(res/c, 6)
def min(a):
    minimum=None
    for i in a:
        if minimum==None:
            minimum=i
        elif minimum<i:
            minimum=i
    return minimum
def max(a):
    maximum=None
    for i in a:
        if maximum==None:
            maximum=i
        elif maximum<i:
            maximum=i
    return maximum
def find(a, item):
    for i in a:
        if item==i+0.000001 or item==i+=i-0.000001:
            return a.find(i)
