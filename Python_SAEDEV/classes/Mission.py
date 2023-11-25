import random as rd

class Mission:
    mission_list = []

    def __init__(self):
        self.coordinates = (rd.randint(0, 20), rd.randint(0, 20))
        self.difficulty = rd.randint(1, 9)
        self.workload = self.difficulty
        self.id = -1 # Initiate Mission ID which represents its index in the mission_list class variable

        # Change every mission ID each time a new mission is created so IDs still work as indices
        for i in range(len(Mission.mission_list)):
            Mission.mission_list.id = i
    def __del__(self): # Called upon using "del mission"
        Mission.mission_amount.pop(self.id)

    @classmethod
    def get_mission_list(cls):
        return Mission.mission_list
