class Player:
    def __init__(self):
        self.coding_level = 1
        self.energy_maximum = 1
        self.energy = 1
        self.bitcoin = 0

    def upgrade_coding(self, bitcoin, coding_level):
        if bitcoin >= 10:
            self.coding_level += 1
            bitcoin -= 10

    def upgrade_energy(self, bitcoin, energy_maximum):
        if bitcoin >= 10:
            self.energy_maximum += 1
            bitcoin -= 10

    def repos(self, energy, energy_maximum):
        while energy <= energy_maximum:
            energy += 0.1
