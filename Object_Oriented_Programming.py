class Cat :
    #class attribute
    species = "mammal"
    legs = 4
    eyes = 2
    tail = 1

    #initialize / Instance Attribtues
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Instance Method - Description    
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
    def eat(self, food):
        self.food = food
        return "{} ate {} pounds of food".format(self.name, self.food)

gus = Cat("Gus", 9)
description = gus.description()

print (description)
print(gus.eat(1))