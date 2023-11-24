import tkinter as tk

def populate_map():
    game_map = open("../game-map.txt", "w")

    # Initiate map_coordinates table
    map_coordinates = [[0 for j in range(21)] for i in range(21)]

    # Write "game-map.txt" file with the location of each element and the name of that element under the following format
    # x y element_name

    for y in range(len(map_coordinates)):
        for x in range(len(map_coordinates[y])):
            game_map.write(f"x y Empty\n")

    game_map.close()

def read_file():
    game_map = open("")
