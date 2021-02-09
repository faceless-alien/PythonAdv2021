def frequent(a,b,c):
    if a==0:
        if b==0 or c==0:
            return False
    elif b==0:
        if c==0:
            return False
        else:
            return True
    else:
        return True