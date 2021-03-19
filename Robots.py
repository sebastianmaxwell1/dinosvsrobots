class IanMalcolmTheDinosaurDestroyer:
    def __init__(self):
        self.name = "Ian Malcolm The Dinosaur Destroyer"
        self.health_status = 100
        self.power_level = ''
        self.weapon_is_a_computer_screen = True
        self.primary_attack = 'JavaScript Aneurysm'
        self.secondary_attack = 'Bores opponent to death by showing Packers footage'

    def check_health_status(self, health):
        response = input('What is the Ian Malcolm dinosaur destroyers health percentage?')
        if health >= 100:
            print(f'{self.name}Better suit up with new armor quick! Your health is at:{self.health_status}')
        elif self.health_status:
            var = self.health_status == 100
            print("The Ian Malcolm dinosaur destroyer is healthy and ready for battle!")

    def attack_dinosaur(self):
        response = input('Which attack would you like to preform? Primary or Secondary?')
        if input() == self.primary_attack:
            print("You have attacked with JavaScript aneurysm! Your opponent is down and out!")
        elif input() == self.secondary_attack:
            print(f'You have attacked with{self.secondary_attack}')










