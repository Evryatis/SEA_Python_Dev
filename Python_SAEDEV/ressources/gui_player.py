import os
import tkinter as tk
from PIL import Image, ImageTk

class player_graphic:
    player_coordinates = []

    def __init__(self, canvas, index):
        self.index = index
        self.coordinates = (10, 10)
        player_graphic.player_coordinates.append(self.coordinates)
        self.coding_level = 1
        self.energy = 1
        self.max_energy = 1
        self.bitcoins = 0
        image_path = os.path.join(os.path.dirname(__file__), 'player_image.jpg')
        self.player_image = Image.open(image_path)
        self.player_image = self.player_image.resize((20, 20))
        self.player_image = ImageTk.PhotoImage(self.player_image)
        self.canvas = canvas
        self.player_image_id = self.canvas.create_image(
        self.coordinates[0] * 25, self.coordinates[1] * 25, anchor=tk.NW, image=self.player_image)
        self.stats_text = tk.Text(self.canvas, height=5, width=50)
        self.stats_text_id = self.canvas.create_window(600, 10, anchor=tk.NW, window=self.stats_text)
        self.stats_text2 = tk.Text(self.canvas, height=5, width=50)
        self.stats_text_id2 = self.canvas.create_window(600, 20, anchor=tk.NW, window=self.stats_text)
        self.stats_text = tk.Text(self.canvas, height=5, width=50)
        self.stats_text_id = self.canvas.create_window(600, 10, anchor=tk.NW, window=self.stats_text)
        self.work_button = tk.Button(self.canvas, text="Work", command=lambda: self.work(1))
        self.rest_button = tk.Button(self.canvas, text="Rest", command=self.rest)
        self.upgrade_coding_button = tk.Button(self.canvas, text="Upgrade Coding Level", command=self.upgrade_coding)
        self.upgrade_energy_button = tk.Button(self.canvas, text="Upgrade Max Energy", command=self.upgrade_energy)
        self.work_button_id = self.canvas.create_window(600, 120, anchor=tk.NW, window=self.work_button)
        self.rest_button_id = self.canvas.create_window(600, 150, anchor=tk.NW, window=self.rest_button)
        self.upgrade_coding_button_id = self.canvas.create_window(600, 180, anchor=tk.NW, window=self.upgrade_coding_button)
        self.upgrade_energy_button_id = self.canvas.create_window(600, 210, anchor=tk.NW,window=self.upgrade_energy_button)
        self.update_stats()

    def move(self, x_movement, y_movement): # Fonction bouger
        destination = (self.coordinates[0] + x_movement, self.coordinates[1] + y_movement) # La fameuse destination dans le readme

        if 0 <= destination[0] <= 20 and 0 <= destination[1] <= 20: # Vérifie que le joueur ne sort pas de la carte
            if destination not in player_graphic.player_coordinates: # Si tout est clair..
                self.clear_stats()
                player_graphic.player_coordinates[self.index] = destination
                self.coordinates = destination
                self.canvas.coords(self.player_image_id, destination[0] * 25, destination[1] * 25)
                self.update_stats()
                return True

        return False

    def work(self, amount):
        work_amount = 1
        if work_amount <= self.energy:
            self.energy -= work_amount
            self.update_stats()

    def update_stats(self):
        self.stats_text.insert(tk.END, self.get_stats())

    def clear_stats(self):
        self.stats_text.delete(1.0, tk.END)

    def update_stats_text(self):
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.insert(tk.END, self.get_stats())

    def upgrade_coding(self):
        if self.bitcoins >= 10:
            self.coding_level += 1
            self.bitcoins -= 10
            self.update_stats_text()

    def upgrade_energy(self):
        if self.bitcoins >= 10 and self.max_energy < 10:
            self.max_energy += 1
            self.bitcoins -= 10
            self.update_stats_text()

    def add_bitcoins(self, amount):
        self.bitcoins += amount
        self.update_stats_text()


    def get_stats(self):
        stats = f"""
                Coding Level: {self.coding_level},
                Energy Level: {self.energy},
                Max Energy: {self.max_energy},
                Bitcoins: {self.bitcoins}
                """
        return stats

    def rest(self):
        if self.coordinates == (10, 10):
            if self.energy <= self.max_energy:
                self.energy += 1
                return True
            return False