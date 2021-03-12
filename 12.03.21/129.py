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
Wolf=ForestAnimal(15, 100)
