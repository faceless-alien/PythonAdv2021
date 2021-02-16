dictionary=open('words.txt','r').read()
def HemmingDistance(a, b):
    dist=abs(len(a)-len(b))
    for i in range(min(len(a),len(b))):
        if a[i]!=b[i]:
            dist+=1
    return dist
        

text=open('input.txt','r').read()
output=open('output.txt','w')
for line in text:
    words=line.split()
    for i in words:
        i=i.split('.')[0]
        res=len(i)+1
        slovo=i
        for u in dictionary:
            b=HemmingDistance(u, i)
            if b==0:
                output.write(u+' ')
                break
            elif b<res:
                res=b
                slovo=u
        else:
            output.write(slovo+' ')
    
                    
                
