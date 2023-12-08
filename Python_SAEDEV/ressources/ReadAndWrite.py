import tkinter as tk
import os

# Constants for cell types
REGULAR_SPACE = 0
TASK_LOCATION = 1
GAME_CENTER = 2

def load_map_from_file(file_path, default_value=-1):
    """
      Charge les données du texte, chaque élément du texte represente un élément dans la carte
      """
    with open(file_path, 'r') as file: # With s'assure que le fichier se ferme même en cas d'erreur

        map_data = [list(map(int, line.strip().split())) for line in file]

    # Find the maximum number of columns in any row
    max_columns = max(len(row) for row in map_data)

    # Pad each row with the default value to make them equal in length
    map_data = [row + [default_value] * (max_columns - len(row)) for row in map_data]

    return map_data


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
    main_gui.iconbitmap('logo.PNG')

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
    map_data = load_map_from_file(map_file_path)

    # Draw the grid with cell types
    create_grid(grid_canvas, map_data, 20)

    # Placeholder for game-related functions (replace with actual functions)
    # For example, you can call functions to handle player movements, tasks, etc.

    # Game main loop
    main_gui.mainloop()

map_file_path = os.path.join(os.getcwd(), 'data', 'game-map.txt')
map_data = load_map_from_file(map_file_path)
if True:
    for i in map_data:
        print(i)
        for e in i:
            if e == 2:
                print("Game Center!")
            if e == 1:
                print("Mission!")

if __name__ == "__main__":
    main()


