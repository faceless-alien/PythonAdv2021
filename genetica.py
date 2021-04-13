import random
class Crocodile():
    def __init__(self, legs, eyes, size):
        self.legs=legs
        self.eyes=eyes
        self.size=size
    def compare(self):
        score=0
        score+=abs(self.legs-4)
        score+=abs(self.eyes-2)
        score+=abs(self.size-5)
        return score
crocs=[]
potomstvo=[]
iterations=0
perfect=True
for i in range(10000):
    i=Crocodile(random.randint(1,10),random.randint(1,10),random.randint(1,10))
    crocs.append(i)
while perfect==True:
    #Оценка
    near_crocs=0
    total=0
    for i in crocs: 
        if i.compare()==0:
            perfect=False 
            break
        else: 
            if i.compare()<3:
                near_crocs+=1
        total+=i.compare()
    else:
        iterations+=1
        print('1 цикл прошел, всего циклов:'+str(iterations))
        print('Почти идеальных крокодилов:'+str(near_crocs))
    #Мутация
    mutation=[]
    for i in range(1001):
        a=random.choice(crocs)
        crocs.pop(crocs.index(a))
        mutation.append(a)
    for i in mutation:
        c=[1,-1]
        b=random.randint(1,3)
        if b==1: i.legs+=random.choice(c)
        elif b==2: i.eyes+=random.choice(c)
        else: i.size+=random.choice(c)
    crocs+=mutation
    #Генерация крокодилов
    for i in range(0,10000, 2):
        parametrs=[crocs[i].legs,crocs[i+1].legs,crocs[i].eyes,crocs[i+1].eyes,crocs[i].size,crocs[i+1].size]
        y=Crocodile(random.choice(parametrs[0:2]),random.choice(parametrs[2:4]),random.choice(parametrs[4:]))
        x=Crocodile(random.choice(parametrs[0:2]),random.choice(parametrs[2:4]),random.choice(parametrs[4:]))
        w=Crocodile(random.choice(parametrs[0:2]),random.choice(parametrs[2:4]),random.choice(parametrs[4:]))
        z=Crocodile(random.choice(parametrs[0:2]),random.choice(parametrs[2:4]),random.choice(parametrs[4:]))
        potomstvo.append(y)
        potomstvo.append(x)
        potomstvo.append(w)
        potomstvo.append(z)
    #Отсев
    iters=0    
    for i in potomstvo:
        if iters==10000:
            break
        if i.compare()>total/1000:
            potomstvo.pop(potomstvo.index(i))
            iters+=1    
    crocs=potomstvo
    potomstvo=[]
print('Итераций понадобилось:'+str(iterations))
    



