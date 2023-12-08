from ressources import ReadAndWrite as rw
from ressources.Player import Player
from ressources.Mission import Mission

# List of available command-line commands

commands = {"help", "move", "rest", "load", "yes", "no", "exit", "upgrade", "energy", "coding", "skip", "bank"}

directions = {"up": (0, -1), "down": (0, 1), "left": (1, 0), "right": (-1, 0)}


# Help command

def help():
    print("""
    All the available commands are:
    ===============================
    help: Get this list of commands (does not skip your turn)
    move <DIRECTION>: Move the player in the specified direction
    upgrade coding: Upgrade your coding level (costs 10 bitcoins)
    upgrade energy: Upgrade your maximum energy level (costs 10 bitcoins)
    bank: Get the amount of bitcoins you have (does not skip your turn)
    skip: Do nothing this turn
    rest: Rest at the game center and get more energy
    load: Load your last saved game
    save: Save your game (does not skip your turn)
    exit: Exit the game (remember to save!) (does not skip your turn)
    yes: Confirm saving/loading/exiting the game
    no: Cancel saving/loading/exiting the game
    
    Available directions: "up", "down", "left" and "right"
    \n\n""")


# Creating game map

game_map = [["0" for j in range(21)] for i in range(21)]
mission_list = [Mission((15, 8), 5),
                Mission((14, 7), 8),
                Mission((4, 9), 1)]

rw.write_map_file(mission_list, "./data/map1.txt")

mission_list2 = rw.read_map_file("./data/map1.txt")

rw.write_map_file(mission_list, "./data/map2.txt")


# Game initialisation

players = [Player(), Player()]


# Game loop

def game_loop(map):
    print("Input \"help\" for a list of available commands.\n")

    game_ended = False
    while not game_ended:
        for player_index in range(len(players)):
            if players[player_index].get_bitcoins() >= 5000:  # Check if any player won the game
                game_ended = True

            action = input(f"Player {player_index + 1}, what do you want to do? (\"help\" for commands)\n").split()

            # Verify that the selected action is part of the available commands
            # AND is not a command that skips your turn
            while not (action[0] in commands and action[0] in {"help", "save", "load", "bank", "exit"}):
                if action[0] == "help":
                    help()

                if action[0] == "exit":
                    action = input("Are you sure you want to leave?\n")
                    if action == "yes":
                        game_ended = True
                        break

                if action[0] == "move":
                    players[player_index].move(directions[action[1][0]],
                                               directions[action[1][1]])

# game_loop()
