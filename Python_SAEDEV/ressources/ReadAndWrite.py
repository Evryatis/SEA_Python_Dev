from .Mission import Mission


# UNUSED
# from .Player import Player


def write_map_file(mission_list, location):
    """
    Writes the "map" file at the specified location (file path) with
    every Mission and their difficulty under the following format:

    "X Y DIFFICULTY"

    :param game_table:
    :param location:
    :return:
    """
    game_map = open(location, "w")

    for mission in mission_list:
        game_map.write(f"{mission.coordinates[0]} {mission.coordinates[1]} {mission.difficulty}\n")

    game_map.close()


def read_map_file(location):
    """
    Reads the "map" file and returns a list of Mission objects
    :param location:
    :return map_coordinates:
    """
    mission_list = []

    mission_file = open(location, "r")

    # This loop imports every Mission and inserts it into map_coordinates to the right coordinates
    for line in mission_file.readlines():
        line = [int(x) for x in line.split()]
        mission_coordinates = (line[0], line[1])
        mission_list.append(Mission(mission_coordinates, line[2]))

    mission_file.close()

    return mission_list

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
