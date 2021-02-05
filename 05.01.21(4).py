max=0
res=0
i=int(input())
while i!=0:
    if i>max:
        res=1
        max=i
    elif i==max:
        res+=1
    i=int(input())
print(res)