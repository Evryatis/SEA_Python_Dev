from ressources import ReadAndWrite as rw
from ressources.Player import Player
from ressources.Mission import Mission

# List of available command-line commands

commands = {"help", "move", "rest", "yes", "no", "exit",
            "upgrade", "skip", "bank", "stats", "missions", "work"}

upgrades = {"energy", "coding"}

directions = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}


# Help command

def help():
    print("""
    All the available commands are:
    ===============================
    help: Get this list of commands (does not skip your turn)
    move <DIRECTION>: Move the player in the specified direction
    work: Work on the mission you share your coordinates with
    missions: Show the location of all missions along with their difficulty and remaining workload
    upgrade coding: Upgrade your coding level (costs 10 bitcoins)
    upgrade energy: Upgrade your maximum energy level (costs 10 bitcoins)
    stats: Get your own stats (your coding level, current energy and maximum energy)
    bank: Get the amount of bitcoins you have (does not skip your turn)
    skip: Do nothing this turn
    rest: Rest at the game center and get more energy
    exit: Exit the game (remember to save!) (does not skip your turn)
    yes: Confirm saving/loading/exiting the game
    no: Cancel saving/loading/exiting the game
    
    Available directions: "up", "down", "left" and "right"
    \n""")


# Creating game map

game_map = [["0" for j in range(21)] for i in range(21)]
game_map[10][10] = -1
missions = rw.read_map_file("./data/map1.txt")

# Game loop

def game_loop(map, missions, player_amount):
    # Creates as many players as needed with each one having their own index
    players = [Player(x) for x in range(player_amount)]

    print("Input \"help\" for a list of available commands.\n")
    game_is_running = True
    while game_is_running:
        for player_index in range(len(players)):
            if players[player_index].get_bitcoins() >= 5000:  # Check if any player won the game
                print(f"Player {player_index + 1} has won! He has {players[player_index].get_bitcoins()} bitcoins.")
                game_is_running = False
                break

            # Verify that the "action" input doesn't skip your turn
            turn_ended = False
            while not turn_ended:
                if players[player_index].coordinates == (10, 10):
                    print(f"Player {player_index + 1}, you are on the game-center.")
                else:
                    print(f"Player {player_index + 1}, you are in position ({players[player_index].coordinates[0]}",
                          f"{players[player_index].coordinates[1]}).")
                action = input(
                    f"Player {player_index + 1}, what do you want to do? (\"help\" for commands)\n").lower().split()

                if action[0] not in commands:
                    continue

                if action[0] == "skip":
                    turn_ended = True

                if action[0] == "help":
                    help()

                if action[0] == "exit":
                    confirmation = input("Are you sure you want to leave?\n")
                    if confirmation.split()[0] == "yes":
                        game_is_running = False
                        break

                if action[0] == "move":
                    if len(action) >= 2:
                        if players[player_index].move(directions[action[1]][0],
                                                      directions[action[1]][1]):
                            turn_ended = True
                        else:
                            continue
                    else:
                        continue

                if action[0] == "missions":
                    for mission in missions:
                        print(mission.get_info())

                if action[0] == "stats":
                    print(players[player_index].get_stats())

                if action[0] == "bank":
                    print(f"You currently have {players[player_index].get_bitcoins()} bitcoins.")

                if action[0] == "work":
                    if players[player_index].coordinates in Mission.get_all_mission_coordinates():
                        for i in range(len(missions)):
                            if missions[i].coordinates == players[player_index].coordinates:
                                mission = missions[i]
                                break
                        if mission.is_available() and players[player_index].lower_energy(mission.get_difficulty()):
                            mission.lower_workload(players[player_index].coding_level)
                            if not mission.is_available():
                                players[player_index].add_bitcoins(mission.get_reward())
                                print("You finished this mission.")
                                turn_ended = True
                                break
                        else:
                            print("This mission is not available yet.")
                            continue
                    else:
                        print("You are not on a mission yet.")
                        continue

                if action[0] == "upgrade":
                    if action[1] == "energy":
                        players[player_index].upgrade_energy()
                    elif action[1] == "coding":
                        players[player_index].upgrade_coding()
                    else:
                        continue

                for mission in missions:
                    if not mission.is_available():
                        mission.lower_counter()

            # Check if exit was confirmed, and if so, quit the game
            if action[0] == "exit" and confirmation == "yes":
                game_is_running = False
                break


game_loop(game_map, missions, 1)
