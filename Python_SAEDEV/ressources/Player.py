class Player:
    player_coordinates = []

    def __init__(self, index):
        self.index = index
        self.coordinates = (10, 10)
        Player.player_coordinates.append(self.coordinates)
        self.coding_level = 1
        self.energy = 1
        self.max_energy = 1
        self.bitcoins = 0

    def move(self, x_movement, y_movement):
        destination = (self.coordinates[0] + x_movement,
                       self.coordinates[1] + y_movement)
        if destination not in Player.player_coordinates or destination == (10, 10) \
                and 0 <= destination[0] <= 20 and 0 <= destination[1] <= 20:
            Player.player_coordinates[self.index] = destination
            self.coordinates = destination
            return True
        return False

    def upgrade_coding(self):
        if self.bitcoins >= 10:
            self.coding_level += 1
            self.bitcoins -= 10

    def upgrade_energy(self):
        if self.bitcoins >= 10 and self.max_energy < 10:
            self.max_energy += 1
            self.bitcoins -= 10

    def add_bitcoins(self, amount):
        self.bitcoins += amount

    def get_bitcoins(self):
        return self.bitcoins

    def rest(self):
        while self.energy <= self.max_energy:
            self.energy += 1
