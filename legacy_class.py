class Animal:
    def __init__(self):
        self.name = name
        self.alive = True
        self.fed = False
class Mammal(Animal):
    def eat(self, food):
        self.food = food
class Predator(Animal):
    def eat(self, food):
        self.food = food

class Plant:
    def __init__(self):
        self.name = name
        self.edible = False
