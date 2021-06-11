from fleet import Fleet
from herd import Herd
import random


def attack_sequence(attacker, defender):
    defender.health -= attacker.attack
    print(f"{attacker.type} attacks {defender.type}")


class Battlefield:

    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def run_game(self):
        j = 0
        k = 0
        while j <= 3 and k <= 3:
            i = get_random_number(0, 2)
            while self.herd.herd[i].health <= 0:
                i = get_random_number(0, 2)

            m = get_random_number(0, 2)
            while self.fleet.fleet[m].health <= 0:
                m = get_random_number(0, 2)

            n = get_random_number(1, 2)

            if n == 1:
                attack_sequence(self.herd.herd[i], self.fleet.fleet[m])
            if n == 2:
                attack_sequence(self.fleet.fleet[m], self.herd.herd[i])
            if self.herd.herd[i].health > 0:
                print(f"{self.herd.herd[i].type}'s HP = {self.herd.herd[i].health}")
            if self.fleet.fleet[i].health > 0:
                print(f"{self.fleet.fleet[m].type}'s HP = {self.fleet.fleet[m].health}")

            if self.herd.herd[i].health <= 0:
                print(f"{self.herd.herd[i].type} health is at 0.")
                i += 1
                j += 1

            elif self.fleet.fleet[m].health <= 0:
                print(f"{self.fleet.fleet[m].type} health is at 0")
                i += 1
                k += 1

            if j == 3:
                print("The fleet of robots has destroyed the dinosaurs")
            if k == 3:
                print("The herd of dinosaurs has destroyed the robots")


def get_random_number(num_1, num_2):
    random_int = random_number(num_1,num_2)
    return random_int


def random_number(min_value, max_value):

    return random.randint(min_value, max_value)


Battlefield().run_game()