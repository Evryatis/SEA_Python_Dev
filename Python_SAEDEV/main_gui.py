import os
import tkinter as tk
from ressources.gui_player import player_graphic as Player
from PIL import Image, ImageTk

GAME_MAP = [] # Création de la carte principale, une liste de liste.
for i in range(21):
    GAME_MAP.append([])
    for j in range(21):
        GAME_MAP[i].append(0)

def load_map_from_file(file_path):
    map_data = []

    with open(file_path, 'r') as file: # Ouvre le fichier en read
        for line in file: # Itère chaque ligne du fichier
            values = list(map(int, line.strip().split())) # code un peu fou qui prends les valeurs données dans le format de map1.txt, et les remets dans un format de liste listées
            map_data.append(values)

    return map_data
file_path1 = ("./data/map1.txt")
mission_list = load_map_from_file(file_path1)

def create_grid(canvas, cell_size, mission_list): # Création de la grid dans laquelle se passe le jeu
    for row in range(21):
        for col in range(21):
            canvas.create_rectangle(col * cell_size, row * cell_size, (col + 1) * cell_size, (row + 1) * cell_size, fill="white", outline="black")
    for x, y, color_code, _ in mission_list:
        fill_color = "purple" if color_code == 1 else "lightgreen" if color_code == 2 else "grey"
        canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill=fill_color, outline="black")

def main(): #Création du GUI principal
    main_gui = tk.Tk()
    main_gui.title("CSN_WAR")
    main_gui.geometry('800x480') # Largeur de la fênetre à l'ouverture
    title_label = tk.Label(main_gui, text='CSN_WAR', font='Calibri 24 bold')
    title_label.grid(row=0, column=0, columnspan=2, pady=5)
    main_gui.columnconfigure(0, weight=1)
    grid_canvas = tk.Canvas(main_gui, width=60 * 20, height=40 * 20, bg="white")
    grid_canvas.grid(row=1, column=0, padx=20, pady=20)
    stats_frame = tk.Frame(main_gui)
    stats_frame.grid(row=2, column=0, pady=10)

    map_file_path = os.path.join(os.getcwd(), 'data', 'map1.txt')
    mission_list = load_map_from_file(map_file_path)

    create_grid(grid_canvas, 25, mission_list)

    player = Player(canvas=grid_canvas, index=0)

    def on_key_press(key): # Fonction pour le déplacement du joueur, elle vérifie a chaque fois si le joueur est sur une mission ou pas (nécessaire..)
        if key.keysym == "Left":
            if player.move(-1, 0):
                check_mission()
        elif key.keysym == "Right":
            if player.move(1, 0):
                check_mission()
        elif key.keysym == "Up":
            if player.move(0, -1):
                check_mission()
        elif key.keysym == "Down":
            if player.move(0, 1):
                check_mission()

    def check_mission(): # Fonction en rapport aux missions, au travail sur les missions, et sur les joueurs par-rapport à celles-ci
        global mission_list # pour accèder à la liste de mission
        for index, mission in enumerate(mission_list[:]):
            x, y, color_code, travail = mission
            if (player.coordinates[0], player.coordinates[1]) == (x, y):
                player.work(1) # Player.work appelle une fonction qui enlève une energie au joueur
                travail -= 1 # Réduit le travail restant dans la mission
                mission_list[index] = (x, y, color_code, travail)
                player.update_stats()
                if travail == 0: # Si la mission n'a plus de travail à faire..
                    player.add_bitcoins(100)
                    mission_list.pop(index)
                    player.update_stats()

    main_gui.bind("<KeyPress>", on_key_press)
    main_gui.mainloop()

if __name__ == "__main__":
    main()


    
