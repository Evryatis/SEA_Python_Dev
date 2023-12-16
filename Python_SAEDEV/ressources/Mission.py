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
        self.counter = self.difficulty * self.starting_workload

        # Add mission coordinates to the mission_coordinates set for easier access later on
        Mission.mission_coordinates.add(self.coordinates)

    def __del__(self):
        Mission.mission_coordinates.clear()

    def is_available(self):
        if self.remaining_workload == 0:
            return False
        return True

    def lower_workload(self):
        if self.remaining_workload > 0:
            self.remaining_workload -= 1
            return True
        return False

    def get_reward(self):
        if self.remaining_workload == 0:
            return self.starting_workload * self.difficulty

    def lower_counter(self):
        if self.counter > 0:
            self.counter -= 1
            if self.counter == 0:
                self.remaining_workload = self.starting_workload

    def get_difficulty(self):
        return self.difficulty

    def get_info(self):
        info = f"""
                This mission is located in {self.coordinates}.
                It will has a difficulty of {self.difficulty},
                a starting workload of {self.starting_workload},
                and a remaining workload of {self.remaining_workload}.
                It will require {self.remaining_workload * self.difficulty} E to be finished.
                """
        return info

    @classmethod
    def get_all_mission_coordinates(cls):
        return cls.mission_coordinates
