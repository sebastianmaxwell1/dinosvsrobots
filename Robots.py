class Robot:

    def __init__(self, robot, power,weapon, attack):
        self.type = robot
        self.health = 100
        self.power = power
        self.weapon = weapon
        self.attack = attack


# class Robot:
#     def __init__(self):
#         self.robots_battle_name = ['Battle Robot']
#         self.ground_air_weapons = False
#         self.troop_health = ''
#         self.power_level = ''

#     def create_battle_name(self):
#         response = input("Create a name for your battle robot!")
#         self.robots_battle_name = response

#     def created_robot_name(self):
#         response = input(f'Your robots name is {self.robots_battle_name}')

#     def robot_styles(self):
#         print("Ground troop(Ground,strong armor,less fire power) or Aerial troop(Aerial,weak armor,heavy fire power)")
#         self.ground_air_weapons = int(input("1 for Ground troop or 2 for Aerial Troop"))

#     def weapon_choice(self):
#         if self.ground_air_weapons <= 1:
#             print('Your robot style is a Ground Troop!')
#         elif self.ground_air_weapons >= 2:
#             print('Your robot style is a Aerial Troop!')

#     def robot_stats(self):
#         if self.ground_air_weapons == 1:
#             self.troop_health = 70
#             self.power_level = 60
#             print(f'Your Ground Troop starting health is {self.troop_health}, Power level is {self.power_level}')
#         elif self.ground_air_weapons == 2:
#             self.troop_health = 35
#             self.power_level = 90
#             print(f' Your Aerial Troop starting health is {self.troop_health}, Power level is {self.power_level}')
