import tkinter as tk
import os
#from ressources import ReadAndWrite as rw
import main.py as main


TASK_LOCATION = 1
GAME_CENTER = 2

mission_list = rw.read_map_file("./data/map1.txt")

GAME_MAP = []
for i in range(21):
    GAME_MAP.append([])
    for j in range(21):
        GAME_MAP[i].append(0)


def create_grid(canvas, cell_types, cell_size):
    """
    Draw the grid on the canvas based on cell types.
    """
    row_count = len(cell_types)
    col_count = len(cell_types[0])

    for row in range(row_count):
        for col in range(col_count):
            cell_type = cell_types[row][col]

            x = col * cell_size
            y = row * cell_size

            # Set properties based on cell type
            fill_color = "white"
            if cell_type == TASK_LOCATION:
                fill_color = "lightblue"
            elif cell_type == GAME_CENTER:
                fill_color = "lightgreen"

            # Draw the cell
            canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill=fill_color, outline="gray")

def main():
    # GUI Initialization
    main_gui = tk.Tk()
    main_gui.title("CSN_WAR")
    main_gui.geometry('800x480')

    # Title
    title_label = tk.Label(main_gui, text='CSN_WAR', font='Calibri 24 bold')
    title_label.grid(row=0, column=0, columnspan=2, pady=5)

    # Grid Initialization for the widgets inside the window
    main_gui.columnconfigure(0, weight=1)

    # Create a Canvas for the grid
    grid_canvas = tk.Canvas(main_gui, width=20 * 20, height=20 * 20, bg="white")
    grid_canvas.grid(row=1, column=0, padx=20, pady=20)

    # Get the absolute path to the map file
    map_file_path = os.path.join(os.getcwd(), 'data', 'game-map.txt')

    # Load map data from a file
    map_data = GAME_MAP

    # Draw the grid with cell types
    create_grid(grid_canvas, map_data, 20)

    # Placeholder for game-related functions (replace with actual functions)
    # For example, you can call functions to handle player movements, tasks, etc.

    # Game main loop
    main_gui.mainloop()

if __name__ == "__main__":
    main()
    
