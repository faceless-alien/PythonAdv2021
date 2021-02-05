a,b,c,d=int(input()),int(input()),int(input()),int(input())
for i in range(1001):
    if a*(i**7)+b*(i**2)+c*i==d*-1:
        print(i)
