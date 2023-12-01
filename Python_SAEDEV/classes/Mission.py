import random as rd

class Mission:
    mission_list = []
    mission_coordinates = set()

    def __init__(self):
        self.coordinates = (rd.randint(0, 20), rd.randint(0, 20))
        Mission.mission_coordinates.add(self.coordinates)
        self.difficulty = rd.randint(1, 9)
        self.workload = self.difficulty
        self.id = -1 # Initiate Mission ID which represents its index in the mission_list class variable

        # Add mission to the mission_list for easier access later on
        Mission.mission_list.append(self)

        self.update_mission_list()
    def __del__(self): # Called upon using "del mission"
        # print(self.mission_list, self.mission_coordinates)
        self.mission_list.pop(self.id)
        self.mission_coordinates.remove(self.coordinates)
        # print(self.mission_list, self.mission_coordinates)

        self.update_mission_list()

    @classmethod
    def get_mission_list(cls):
        return cls.mission_list

    @classmethod
    def get_all_mission_coordinates(cls):
        return cls.mission_coordinates

    @classmethod
    def update_mission_list(cls):
        # Change every mission ID each time a new mission is created so IDs still work as indices
        for i in range(len(cls.mission_list)):
            cls.mission_list[i].id = i
