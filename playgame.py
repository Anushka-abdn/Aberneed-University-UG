from hero import Hero
from maze_gen_recursive import make_maze_recursion
from maze_gen_recursive import populate
from copy import deepcopy
from getch1 import *
import sys
import random

WALL_CHAR = "#"
SPACE_CHAR = "-"
HERO_CHAR = "H"


class _Environment:
    """Environment includes Maze+Monster+Goblin"""
    def __init__(self, maze):
        self._environment = deepcopy(maze)

    def set_coord(self, x, y, val):
        self._environment[x][y] = val

    def get_coord(self, x, y):
        return self._environment[x][y]

    def print_environment(self, wall="#", space="-", monster = 'M', goblin='G', hero ='H'):
        """print out the environment in the terminal"""
        for row in self._environment:
            row_str = str(row)
            row_str = row_str.replace("1", wall)  # replace the wall character
            row_str = row_str.replace("0", space)  # replace the space character
            row_str = row_str.replace ('3', monster) #add monsters
            row_str = row_str.replace ('2', goblin) #add goblins
            row_str = row_str.replace ('4', hero) #add hero
            print("".join(row_str))


#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

from getch1 import *
import sys


class Hero:
    """this is the hero class, further define it please"""
    def __init__(self):
        """set the coordinate of the hero in the maze"""
        self._coordX = 2
        self._coordY = 2
        self._health = 100
        self._coins = 1000  # gold coins the hero have.
        self._gem=3


    def move(self, environment):
        """move in the maze, it is noted this function may not work in the debug mode"""
        ch2 = getch()
        if ch2 == b'H' or ch2 == "A":
            # the up arrow key was pressed
            print ("up key pressed")


        elif ch2 == b'P' or ch2 == "B":
            # the down arrow key was pressed
            print("down key pressed")


        elif ch2 == b'K' or ch2 == "D":
            # the left arrow key was pressed
            print("left key pressed")

        elif ch2 == b'M' or ch2 == "C":
            # the right arrow key was pressed
            print("right key pressed")

    def move_debug(self, environment):

        """move in the maze, you need to press the enter key after keying in
        direction, and this works in the debug mode"""

        ch2 = sys.stdin.read(1)

        if ch2 == "w":
            # the up arrow key was pressed
            print("up key pressed")

        elif ch2 == "s":
            # the down arrow key was pressed
            print("down key pressed")

        elif ch2 == "a":
            # the left arrow key was pressed
            print("left key pressed")

        elif ch2 == "d":
            # the right arrow key was pressed
            print("right key pressed")

    def fight(self):
        """fight with monsters"""
        return ('I fought the law and the law won')

import random

class Monster:
    def __init__(self):
        self.ability = random.randrange(0, 1000)
        self.success = random.randrange(0, 100)

class Thief (Monster):
    def __init__(self):
        super.__init__(self)

    def steal(self):
        if random.randrange(0, self.ability) == random.randrange(0, self.ability):
            myHero._coins = (myHero._coins - self.ability)

class Fight (Monster):
    def __init__(self):
        super.__init__(self)

    def fight(self):
        if random.randrange(0, self.success) == random.randrange(0, self.success):
            myHero._health = (myHero._health - self.ability)

class Gamer (Monster):
    def __init__(self):
        super.__init__(self)

    def rockpaper (self):
        def weapon (self):
            move = random.randrange(1, 4)
            if move == 3:
                print ('rock')
                return (0)
            elif move == 1:
                print("paper")
                return(1)
            else:
                 print ("scissors")
                 return (2)

        def attack (self):
            result = myHero.fight()
            if self.weapon == result:
                print ('draw')
            elif (self.weapon == 0 and result == 2) or (self.weapon == 1 and result == 0) or (self.weapon == 2 and result == 1):
                print ('Monster won')
                return (myHero._coins - rself.ability()), (myHero._health - self.ability() ) #####should be ability but how do i add it####
            else:
                print ('Hero won, move on')


class Goblin:
    def __init__(self):
        self.ability = random.randrange(0, 1000)
        self.success = random.randrange(0, 100)

class ThiefG (Goblin):
    def __init__(self):
        super.__init__(self)

    def steal(self):
        if random.randrange(0, self.ability) == random.randrange(0, self.ability):
            myHero._coins = (myHero._coins - self.ability)

class FightG (Goblin):
    def __init__(self):
        super.__init__(self)

    def fight(self):
        if random.randrange(0, self.success) == random.randrange(0, self.success):
            myHero._health = (myHero._health - self.ability)

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
            else:
                print ("scissors")
                return (2)


        def attack (self):
            result = myHero.fight()
            if self.weapon == result:
                print ('draw')
            elif (self.weapon == 0 and result == 2) or (self.weapon == 1 and result == 0) or (self.weapon == 2 and result == 1):
                print ('Tun tun tuuun, non cash for you! ')
                return (myHero._coins - rself.ability()), (myHero._health - self.ability() ) #####should be ability but how do i add it####
            else:
                print ('Hero won, make it rain! ')
        
class Game:

    _count = 0

    def __init__(self):
        self.myHero = Hero()
        self.maze = populate(make_maze_recursion(17, 17))
        
        self.MyEnvironment = _Environment(self.maze)  # initial environment is the maze itself
        self._count = 100

    def play(self):
        while True:
            #self.myHero.move_debug(self.MyEnvironment)  #this works in debug mode
            self.myHero.move(self.MyEnvironment)
            print ("move made hehe")
            self.MyEnvironment.print_environment()

            self._count = (self._count -1) 
            print("============================", self._count)


if __name__ == "__main__":

    myGame = Game()
    myGame.play()
    