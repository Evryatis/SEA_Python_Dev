import tkinter as tk

def write_map_file(game_table, location):
    """
    Write "game-map.txt" file with the location of each element
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
    game_map = open(f"{location}/game-map.txt", "r")
