from ..ressources.Player import Player


def write_map_file(game_table, location):
    """
    Writes the "game-map.txt" file with the location of each element
    and the name of that element under the following format:

    "x y element_id"

    :param game_table:
    :param location:
    :return:
    """
    game_map = open(f"{location}/game-map.txt", "w")

    for y in range(len(game_table)):
        for x in range(len(game_table[y])):
            game_map.write(f"{x} {y} {game_table[x][y]}\n")

    game_map.close()


def read_map_file(location):
    """
    Reads the "game-map.txt" file and assign each line to its coordinates
    in the map matrix (game_map) in main.py.

    :param location:
    :return map_coordinates:
    """
    game_map = open(f"{location}/game-map.txt", "r")

    # Split each line of the game-map.txt file so that each element is contained in a sublist of map_coordinates
    # map_coordinates is a list which contains lists that represent each line of the game-map.txt
    # Each sublist should follow the format "[x, y, element_id]"
    map_coordinates = [line.split() for line in game_map.readlines()]

    game_map.close()

    for line in map_coordinates:
        for i in range(len(line)):
            line[i] = int(line[i])  # Convert each element of all lines into ints

    return map_coordinates


def save_player_states(location, player_list):
    """
    Writes the saves.txt file with the locations and stats of each player in the player list
    that is passed as an argument under the following format:

    "x y coding_level energy max_energy bitcoins"
    :param location:
    :param player_list:
    :return:
    """
    saves = open(f"{location}/saves.txt", "w")
    for player in player_list:
        saves.write(f"{player.coordinates[0]} {player.coordinates[1]} {player.coding_level} " +
                    f"{player.energy} {player.max_energy} {player.bitcoins}\n")
    saves.close()


def load_player_states(location):
    save_file = open(f"{location}/saves.txt", "r")

    saves = [line.split() for line in save_file.readlines()]

    save_file.close()

    for line in saves:
        for i in range(len(line)):
            line[i] = int(line[i])  # Convert each element of all lines into ints

    players = [Player()] * len(saves)
    for i in range(len(saves)):
        players[i].coordinates = (saves[i][0], saves[i][1])
        players[i].coding_level = saves[i][2]
        players[i].energy = saves[i][3]
        players[i].max_energy = saves[i][4]
        players[i].bitcoins = saves[i][5]

    return players
