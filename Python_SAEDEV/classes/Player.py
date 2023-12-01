class Player:
    max_energy = 10

    def __init__(self):
        self.coordinates = (10, 10)
        self.coding_level = 1
        self.energy_maximum = 1
        self.energy = 1
        self.bitcoins = 0

    def move_player(self, x_movement, y_movement):
        self.coordinates = (self.coordinates[0] + x_movement,
                            self.coordinates[1] + y_movement)

    def upgrade_coding(self):
        if self.bitcoins >= 10:
            self.coding_level += 1
            self.bitcoins -= 10

    def upgrade_energy(self):
        if self.bitcoins >= 10:
            self.energy_maximum += 1
            self.bitcoins -= 10

    def add_bitcoins(self, amount):
        self.bitcoins += amount

    def rest(self):
        while self.energy <= self.max_energy:
            self.energy += 1
