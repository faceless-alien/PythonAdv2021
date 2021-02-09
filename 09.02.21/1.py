def min(a,b,c,d):
    if a<b<c<d:
        return a
    elif b<a<c<d:
        return b
    elif c<a<b<d:
        return c
    else:
        return d

print(min(4, 5, 6, 7))