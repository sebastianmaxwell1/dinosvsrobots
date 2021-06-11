from robots import Robot
from weapon import Weapon

class Fleet:

    def __init__(self):
        self.fleet = [Robot("Terminator", 100, Weapon("shotgun"), 20), Robot("iron giant", 100,Weapon("size and strength"), 40), Robot("Iron man", 100, Weapon("Rockets"), 50)]
