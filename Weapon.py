class Weapons:
    def __init__(self):
        self.stats = ''
        self.energy = ''
        self.weapon = ''




    def dino_stats(self):
        if self.dino_weapon == 1:
            self.dino_health = 60
            self.dino_energy = 60
            self.dino_attack_power = 45
            print(f'Your dinosaurs health is {self.dino_health}, Claw Attack level is {self.dino_attack_power}')
        elif self.dino_weapon == 2:
            self.dino_health = 60
            self.dino_energy = 60
            self.dino_attack_power = 50
            print(f' Your dinosaurs health is {self.dino_health}, Bite Attack level is {self.dino_attack_power}')


def robot_stats(self):
    if self.ground_air_weapons == 1:
        self.troop_health = 70
        self.power_level = 60
        print(f'Your Ground Troop starting health is {self.troop_health}, Power level is {self.power_level}')
    elif self.ground_air_weapons == 2:
        self.troop_health = 35
        self.power_level = 90
        print(f' Your Aerial Troop starting health is {self.troop_health}, Power level is {self.power_level}')
