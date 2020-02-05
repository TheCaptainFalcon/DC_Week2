import random
import math

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def print_status(self):
        return("{}'s health is {} and his power is {}").format(self.name, self.health, self.power)
    def attack(self, opponent):
        if not self.alive():
            return("{}'s health has dropped by {}").format(opponent.name, self.power)
            opponent.receive_damage(self.power)
    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if self.health <= 0:
            print("%s is dead." % self.name)
    def alive(self):
        while self.health > 0:
            return("{} has {} health remaining").format(self.name, self.health)
            if hero.health <= 0:
                return("Game over, you lose.")
            elif marco.health <= 0:
                return("Congratulations, you won!")

    class Shadow(Character):
        def __init__(self, name, health, power):
            self.name = name
            self.health = name
            self.power = power

        def dodge(self):
            for i in range(100):
                if random.random() <= .9:
                    print("Gary dodged your attack!")
                elif random.random() > .9:
                    print("Gary tripped on a rock and got smacked!")
                    self.health -= 1    

    class Zombie:
        def __init__(self, name, health, power):
            self.name = name
            self.health = health
            self.power = power

        def zombie_alive(self):
            while self.health > 0:
                print("{} has {} health remaining").format(self.name, self.health)        
                if self.health <= 0:
                    print("{} is regenerating his limbs!" + " Keep attacking to kill him!").format(self.name,)
                    for i in range(100):
                        if random.random() <=.5:
                            print("{} is finally dead!").format(self.name)

    class Medic(Character):
        def __init__(self, name, health, power):
            self.name = name
            self.health = health
            self.power = power
        
        def recuperate(self):
            for i in range(100):
                if random.random() <= 0.2:
                    self.receive_damage += 2
                print("{} took steroids and came back with 2 health restored!").format(self.name)

    class Hero(Character):
        def __init__(self, name, health, power):
            self.name = name
            self.health = health
            self.power = power

        def double_damage(self, opponent):
            for i in range(100):
                if random.random() <= 0.2:
                    opponent.receive_damage * 2
                    print("Johnny got a pump and dealt double damage!")

    class Goblin(Character):
        def __init__(self, name, health, power):
            self.name = name
            self.health = health
            self.power = power   

johnny = Character("Johnny", 10, 5)
marco = Character("Marco", 6, 2)
medicus = Character("Medicus", 7, 3)
gary = Character("Gary" , 1, 3)
jerry = ("Jerry", 4, 1)

print(marco.alive())
# while johnny.alive() and marco.alive():
print(johnny.double_damage)


# print(johnny.display())
# print(marco.display())

# print(johnny.attack(marco))        