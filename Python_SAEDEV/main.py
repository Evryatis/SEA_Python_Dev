from functions import ReadAndWrite as rw
from classes import Player
from classes import Mission


# Creating game map

game_map = [["-1" for j in range(21)] for i in range(21)]
game_center = 0
game_map[10][10] = game_center

rw.write_map_file(game_map, "./data")


# Game initialisation

player1 = Player()

mission1 = Mission()
print(mission1)


# Game loop

def game_loop():
    pass


