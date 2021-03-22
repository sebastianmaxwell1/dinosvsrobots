class Dinosaurs:
    def __init__(self):
        self.dino_type = 'Velociraptor'
        self.dino_health = ''
        self.dino_energy = ''
        self.dino_weapon = 'claws, bite'
        self.dino_attack_power = ''

    def dino_species(self):
        response = input(f'Your robots name is {self.dino_type}')

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

