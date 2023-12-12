import random as rd


class Mission:
    mission_coordinates = set()

    def __init__(self, coordinates, difficulty, workload):
        self.coordinates = coordinates
        if self.coordinates not in Mission.mission_coordinates:
            Mission.mission_coordinates.add(self.coordinates)
        self.difficulty = difficulty
        self.starting_workload = workload
        self.remaining_workload = workload

        # Add mission coordinates to the mission_coordinates set for easier access later on
        Mission.mission_coordinates.add(self.coordinates)

    def __del__(self):
        Mission.mission_coordinates.clear()

    def get_reward(self):
        if self.remaining_workload == 0:
            return

    @classmethod
    def get_all_mission_coordinates(cls):
        return cls.mission_coordinates
