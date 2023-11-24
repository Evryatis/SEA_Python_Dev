import tkinter as tk
import random as rd

# Initialisation des variables pour la carte

game_center = 3
coding_level = 1
energy_max = 1
energy = 1
Bitcoins = 0


# Initialisation de la carte

game_map = [[0 for j in range(21)] for i in range(21)]
game_map[10][10] = game_center


# Moteur du Jeu
def game_loop():
    pass

def mission_jeu():
    mission_coordinates = (rd.randint(0, 20), rd.randint(0, 20))
    difficulty_sample = rd.randint(1, 9) # On choisi un nombre entre 1 à 9 représentant la difficulté de la mission
    remaining_workload = difficulty_sample
    return [mission_coordinates, difficulty_sample, remaining_workload]


mission1 = mission_jeu()
print(mission1)
