r=[]
def readInt(n, m):
    global r
    for i in range(n):
        j=[]
        for u in input().split():
            j.append(u)
        r.append(j)
def print2D(a):
    res=''
    for i in a:
        for j in i:
            res+=j+' '
        res+='\n'
    return res
readInt(2, 3)
print(print2D(r))