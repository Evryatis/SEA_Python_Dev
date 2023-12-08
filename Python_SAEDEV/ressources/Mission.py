import random as rd


class Mission:
    mission_coordinates = set()

    def __init__(self, coordinates, difficulty):
        self.coordinates = coordinates
        Mission.mission_coordinates.add(self.coordinates)
        self.difficulty = difficulty
        self.workload = self.difficulty

        # Add mission coordinates to the mission_coordinates set for easier access later on
        Mission.mission_coordinates.add(self.coordinates)

    def __del__(self):  # Called upon using "del mission"
        Mission.mission_coordinates.remove(self.coordinates)

    @classmethod
    def get_all_mission_coordinates(cls):
        return cls.mission_coordinates
