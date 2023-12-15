import tkinter as tk
import os
from ressources import ReadAndWrite as rw



GAME_MAP = []
for i in range(21):
    GAME_MAP.append([])
    for j in range(21):
        GAME_MAP[i].append(0)

# def load_map_from_file(file_path, default_value=0):
#     """
#     Load map data from a text file and return a 2D list.
#     Each element represents the type of cell at that position.
#     """
#     with open(file_path, 'r') as file:
#         map_data = [list(map(int, line.strip().split())) for line in file]
#
#     # Find the maximum number of columns in any row
#     max_columns = max(len(row) for row in map_data)
#
#     # Pad each row with the default value to make them equal in length
#     map_data = [row + [default_value] * (max_columns - len(row)) for row in map_data]
#
#     return map_data



TASK_LOCATION = 1
GAME_CENTER = 2

mission_list = rw.read_map_file("./data/map1.txt")
game_map1 = [["white" for x in range(21)] for y in range(21)]
for mission in mission_list:
    game_map1[mission.coordinates[0]][mission.coordinates[1]] = "lightblue"

def create_grid(canvas, cell_types, cell_size):
    """
    Draw the grid on the canvas based on cell types.
    """
    """row_count = len(cell_types)
    col_count = len(cell_types[0])

    for row in range(row_count):
        for col in range(col_count):
            cell_type = cell_types[row][col]

            x = col * cell_size
            y = row * cell_size

            if row in mission_list[row] and col in mission_list[row]:
                if 1 in mission_list[row]:
                    fill_color = "lightblue"
                if 2 in mission_list[row]:
                    fill_color = "lightgreen"
            # Set properties based on cell type
            fill_color = "white"
            if 0 <= row < len(mission_list) and 0 <= col < len(mission_list[row]):
                if 1 in mission_list[row]:
                    fill_color = "lightblue"
                if 2 in mission_list[row]:
                    fill_color = "lightgreen"

            canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill=fill_color, outline="gray")"""
    # for mission in mission_list:
    #     x, y, color_code, _ = mission
    # 
    #     # Calculate the actual row and column indices based on x and y coordinates
    #     row = y
    #     col = x
    # 
    #     # Set fill_color based on color_code
    #     if color_code == 1:
    #         fill_color = "lightblue"
    #     elif color_code == 2:
    #         fill_color = "lightgreen"
    #     else:
    #         fill_color = "white"
    # 
    #     # Draw the cell
    #     canvas.create_rectangle(col * cell_size, row * cell_size, (col + 1) * cell_size, (row + 1) * cell_size, fill=fill_color, outline="gray")
    
    for y in range(len(cell_types)):
        for x in range(len(cell_types)):
            fill_color = cell_types[x][y]

            canvas.create_rectangle(col * cell_size, row * cell_size, (col + 1) * cell_size, (row + 1) * cell_size,
                                    fill=fill_color, outline="gray")

def mission_addon():
    pass

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
    map_file_path = os.path.join(os.getcwd(), 'data', 'map1.txt')

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
    

    
