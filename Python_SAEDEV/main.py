from functions import ReadAndWrite as rw
from classes.Player import Player
from classes.Mission import Mission


# Creating game map

game_map = [["-1" for j in range(21)] for i in range(21)]
game_center = 0
game_map[10][10] = game_center

# rw.write_map_file(game_map, "./data")


# Game initialisation

player1 = Player()

print(Mission.get_mission_list(), Mission.get_all_mission_coordinates())
mission1 = Mission()
print(Mission.get_mission_list(), Mission.get_all_mission_coordinates())
del mission1
print(Mission.get_mission_list(), Mission.get_all_mission_coordinates())


# Game loop

def game_loop():
    pass
