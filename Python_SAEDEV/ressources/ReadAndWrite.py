from .Mission import Mission


# UNUSED
# from .Player import Player


def write_map_file(game_table, location):
    """
    Writes the "map" file at the specified location (file path) with
    every Mission and their difficulty under the following format:

    "X Y DIFFICULTY"

    :param game_table:
    :param location:
    :return:
    """
    game_map = open(location, "w")

    for y in range(len(game_table)):
        for x in range(len(game_table[y])):
            cell = game_table[x][y]
            if isinstance(cell, Mission):
                game_map.write(f"{cell.coordinates[0]} {cell.coordinates[1]} {cell.difficulty}\n")

    game_map.close()


def read_map_file(location):
    """
    Reads the "game-map.txt" file and assign each line to its coordinates
    in the map matrix (game_map) in main.py.

    :param location:
    :return map_coordinates:
    """
    # map_coordinates is the map matrix for which each element represents one cell of the map
    map_coordinates = [[0 for j in range(21)] for i in range(21)]
    map_coordinates[10][10] = 1  # The game-center has a value of 1

    game_map = open(f"{location}/game-map.txt", "r")

    # This loop imports every Mission and inserts it into map_coordinates to the right coordinates
    for line in game_map.readlines():
        line.split()
        mission_coordinates = (line[0], line[1])
        map_coordinates[line[0]][line[1]] = Mission(mission_coordinates, line[2])

    game_map.close()

    for line in map_coordinates:
        for i in range(len(line)):
            line[i] = int(line[i])  # Convert each element of all lines into ints

    return map_coordinates

# USELESS AND OBSOLETE
# def save_player_states(location, player_list):
#     """
#     Writes the saves.txt file with the locations and stats of each player in the player list
#     that is passed as an argument under the following format:
#
#     "x y coding_level energy max_energy bitcoins"
#     :param location:
#     :param player_list:
#     :return:
#     """
#     saves = open(f"{location}/saves.txt", "w")
#     for player in player_list:
#         saves.write(f"{player.coordinates[0]} {player.coordinates[1]} {player.coding_level} " +
#                     f"{player.energy} {player.max_energy} {player.bitcoins}\n")
#     saves.close()


# USELESS AND OBSOLETE
# def load_player_states(location):
#     save_file = open(f"{location}/saves.txt", "r")
#
#     saves = [line.split() for line in save_file.readlines()]
#
#     save_file.close()
#
#     for line in saves:
#         for i in range(len(line)):
#             line[i] = int(line[i])  # Convert each element of all lines into ints
#
#     players = [Player()] * len(saves)
#     for i in range(len(saves)):
#         players[i].coordinates = (saves[i][0], saves[i][1])
#         players[i].coding_level = saves[i][2]
#         players[i].energy = saves[i][3]
#         players[i].max_energy = saves[i][4]
#         players[i].bitcoins = saves[i][5]
#
#     return players
