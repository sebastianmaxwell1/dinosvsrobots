class Robot:
    def __init__(self):
        self.robots_battle_name = ''
        self.ground_air_weapons = False
        self.troop_health = ''
        self.power_level = ''

    def create_battle_name(self):
        response = input("Create a name for your battle robot!")
        self.robots_battle_name = response

    def created_robot_name(self):
        print(f'Your robots name is {self.robots_battle_name}')

    def robot_styles(self):
        print("Ground troop(Ground,strong armor,less fire power) or Aerial troop(Aerial,weak armor,heavy fire power)")
        self.ground_air_weapons = int(input("1 for Ground troop or 2 for Aerial Troop"))

    def weapon_choice(self):
        if self.ground_air_weapons <= 1:
            print('Your robot style is a Ground Troop!')
        elif self.ground_air_weapons >= 2:
            print('Your robot style is a Aerial Troop!')

    def robot_stats(self):
        if self.ground_air_weapons == 1:
            self.troop_health = 70
            self.power_level = 60
            print('Your Ground Troop statistics')
        elif self.ground_air_weapons == 2:
            self.troop_health = 35
            self.power_level = 90
            print('Your Aerial Troop statistics')

0