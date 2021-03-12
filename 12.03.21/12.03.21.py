import random
class Cat():
    def __init__(self,name='',stamina=1000):
        self.name=name
        self.stamina=stamina
    def setName(self,string_name):
        self.name=string_name
    def run(self):
        chance=random.randint(1,100)
        self.stamina-=100
        if chance>89 and chance<101:
            self.stamina=self.stamina+50
            return self.name+' поймала мышь и востановила 50 энергии'
        elif chance<59 and chance<90:
            return self.name+' забралась на дерево'
        else:
            return 'Ничего не произошло, кошка'
    def GetName(self):
        return self.name
    def GetStamina(self):
        return self.stamina
    def Sleep(self):
        self.stamina+=100
    def Eat(self):
        self.stamina+=200
Mursik=Cat()
Mursik.setName('Mursik')
print(Mursik.GetName())
print(Mursik.run())
print(Mursik.GetStamina())
Mursik.Eat()
Mursik.Sleep()
print(Mursik.GetStamina())