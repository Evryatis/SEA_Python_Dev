import random as rd

class Mission:
    mission_list = []
    mission_coordinates = set()

    def __init__(self):
        self.coordinates = (rd.randint(0, 20), rd.randint(0, 20))
        Mission.mission_coordinates.add(self.coordinates)
        self.difficulty = rd.randint(1, 9)
        self.workload = self.difficulty

        # Add mission to the mission_list for easier access later on
        Mission.mission_list.append(self)
        Mission.mission_coordinates.add(self.coordinates)

        # Initiate Mission ID which represents its index in the mission_list class variable
        self.id = len(Mission.mission_list) - 1

        # Change every mission ID each time a new mission is created so IDs still work as indices
        for i in range(len(Mission.mission_list)):
            Mission.mission_list[i].id = i
    def __del__(self): # Called upon using "del mission"
        # print(self.mission_list, self.mission_coordinates)
        Mission.mission_list.pop(self.id)
        Mission.mission_coordinates.remove(self.coordinates)
        # print(self.mission_list, self.mission_coordinates)

        for i in range(len(Mission.mission_list)):
            Mission.mission_list[i].id = i

    @classmethod
    def get_mission_list(cls):
        return cls.mission_list

    @classmethod
    def get_all_mission_coordinates(cls):
        return cls.mission_coordinates
