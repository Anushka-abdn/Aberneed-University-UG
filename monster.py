import random

class Monster:
    def __init__(self):
        self.ability = random.randrange(0, 1000)
        self.success = random.randrange(0, 100)

class Thief (Monster):
    def __init__(self):
        super.__init__(self)

    def steal(self, self.ability, self.success):
        if random.randrange(0, self.ability) == random.randrange(0, self.ability):
            myHero._coins() = (myHero._coins() - self.ability)

class Fight (Monster):
    def __init__(self):
        super.__init__(self)

    def fight(self, self.ability, self.success):
        if random.randrange(0, self.success) == random.randrange(0, self.success):
            myHero._health() = (myHero._health() - self.ability)

class Gamer (Monster):
    def __init__(self):
        super.__init__(self)

    def rockpaper (self):
        def weapon (self):
            move = random.randrange(1, 89)
            if x % 3 == 0:
                print ('rock')
                return (0)
            elif (x%3)==1:
                print("paper")
                return(1)
            else print ("scissors"), return (2)
        
        def attack (self, myHero.fight): 
            if self.weapon == myHero.fight:
                print ('draw')
            elif (self.weapon == 0 and myHero.fight == 2) or (self.weapon == 1 and myHero.fight == 0) or (self.weapon == 2 and myHero.fight == 1):
                print ('Monster won')
                return (myHero._coins - rself.ability()), (myHero._health - self.ability() ) #####should be ability but how do i add it####
            else print ('Hero won, move on')


class Goblin:
    def __init__(self):
        self.ability = random.randrange(0, 1000)
        self.success = random.randrange(0, 100)

class ThiefG (Goblin):
    def __init__(self):
        super.__init__(self)

    def steal(self, self.ability, self.success):
        if random.randrange(0, self.ability) == random.randrange(0, self.ability):
            myHero._coins() = (myHero._coins() - self.ability)

class FightG (Goblin):
    def __init__(self):
        super.__init__(self)

    def fight(self, self.ability, self.success):
        if random.randrange(0, self.success) == random.randrange(0, self.success):
            myHero._health() = (myHero._health() - self.ability)

class GamerG (Goblin):
    def __init__(self):
        super.__init__(self)

    def rockpaper (self):
        def weapon (self):
            move = random.randrange(1, 89)
            if x % 3 == 0:
                print ('rock')
                return (0)
            elif (x%3)==1:
                print("paper")
                return(1)
            else print ("scissors"), return (2)
        
        def attack (self, myHero.fight): 
            if self.weapon == myHero.fight:   #####ad peaceful rock paper socsors game####
                print ('draw')
            elif (self.weapon == 0 and myHero.fight == 2) or (self.weapon == 1 and myHero.fight == 0) or (self.weapon == 2 and myHero.fight == 1):
                print ('Tun tun tuuun, non cash for you! ')
                return (myHero._coins + random.randint(0, 50)), (myHero._health + random.randint(0,50) ) #####should be ability but how do i add it####
            else print ('Hero won, make it rain! ')
