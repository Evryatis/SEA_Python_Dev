import tkinter as tk
from ressources.Player import Player

def create_grid(canvas, row_count, col_count, cell_size):
    for row in range(row_count + 1):
        y = row * cell_size
        canvas.create_line(0, y, col_count * cell_size, y, fill="gray")

    for col in range(col_count + 1):
        x = col * cell_size
        canvas.create_line(x, 0, x, row_count * cell_size, fill="gray")


# GUI Initialization
main_gui = tk.Tk()
main_gui.title("CSN_WAR")
main_gui.geometry('800x480')

# Title
title_label = tk.Label(main_gui, text='CSN_WAR', font='Calibri 24 bold')
title_label.grid(row=0, column=0, columnspan=2, pady=5)

# Grid Initialization for the widgets inside the window
main_gui.columnconfigure(0, weight=1)

# Create a Canvas for the grid, canvas is the most flexible widget.
grid_canvas = tk.Canvas(main_gui, width=20 * 20, height=20 * 20, bg="white")
grid_canvas.grid(row=1, column=0, padx=20, pady=20)  # Adjust padx and pady as needed

# Widget for player-information
player_info = tk.Frame(master = main_gui)
player1 = tk.Label(master = player_info)
player2 = tk.Label(master = player_info)
player3 = tk.Label(master = player_info)
player4 = tk.Label(master = player_info)


# Draw the grid
create_grid(grid_canvas, 20, 20, 20)

# Game main loop
main_gui.mainloop()
