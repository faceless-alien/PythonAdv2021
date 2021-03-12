class Animal():
    def __init__(self,age):
        self.age=age
class WildAnimal(Animal):
    def __init__(self, age,hunger,hp=100):
        self.age=age
        self.hunger=hunger
        self.hp=hp
class HomeAnimal(Animal):
    def __init__(self, name, age):
        self.name=name
        self.age=age
class Pets(HomeAnimal):
    def pet(self):
        return  self.name+' очень рад'
class Livestock(HomeAnimal):
    pass
class WaterAnimal(WildAnimal):
    pass
class ForestAnimal(WildAnimal):
    pass
class Wolf(ForestAnimal):
    def hunt(self):
        self.hp+=10
        self.hunger+=10
        return "Волк поохотился и поел"
class Cow(Livestock):
    def __init__(self ,age, milk=100, name):
        self.age=age
        self.name=name
        self.milk=milk
    def milk(self):
        self.milk-=random.randint(10, 50-age)
        return self.name'дала '+str(100-self.milk)+"молока"
    def sleep(self):
        self.milk=100
        