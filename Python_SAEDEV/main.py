from Python_SAEDEV.ressources import ReadAndWrite as rw
from ressources.Player import Player
from ressources.Mission import Mission

# Creating game map

game_map = [["-1" for j in range(21)] for i in range(21)]
game_center = 0
game_map[10][10] = game_center

# rw.write_map_file(game_map, "./data")

map_coordinates = rw.read_map_file("./data")


# Game initialisation

players = [Player(), Player()]
players[1].coordinates = (12, 5)
print(players[1].coordinates)

mission1 = Mission()

rw.save_player_states("./data", players)

players = rw.load_player_states("./data")
print(players[1].coordinates)


# Game loop

def game_loop():
    pass
