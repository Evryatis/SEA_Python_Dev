import random as rd
from functions import ReadAndWrite

# Initialisation des variables pour la carte

game_center = 3

# Initialisation de la carte

game_map = [[0 for j in range(21)] for i in range(21)]
game_map[10][10] = game_center

class Joueur:
    def __init__(self, coding_level, energy_maximum, energy, bitcoin):
        self.coding_level = coding_level
        self.energy_maximum = energy_maximum
        self.energy = energy
        self.bitcoin = bitcoin

    def amelioration_niveau(self, bitcoin, coding_level):
        if bitcoin > 0:
            self.coding_level += 1
            bitcoin -= 10

    def amelioration_energie(self, bitcoin, energy_maximum):
        if bitcoin > 0:
            self.energy_maximum += 1
            bitcoin -= 10

    def repos(self, energy, energy_maximum):
        while energy <= energy_maximum:
            energy += 0.1
            time.sleep(0.1)


def game_loop():
    pass

def mission_jeu():
    mission_coordinates = (rd.randint(0, 20), rd.randint(0, 20))
    difficulty_sample = rd.randint(1, 9) # On choisi un nombre entre 1 à 9 représentant la difficulté de la mission
    remaining_workload = difficulty_sample
    return [mission_coordinates, difficulty_sample, remaining_workload]


mission1 = mission_jeu()
print(mission1)
