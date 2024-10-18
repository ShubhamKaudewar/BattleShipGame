

class Ship:
    def __init__(self, id, x1, y1, size, destroyed=False):
        self.id = id
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.size = int(size)
        self.x2 = self.x1 + self.size
        self.y2 = self.y1 + self.size
        self.destroyed = destroyed

    def add_ship(self):
        pass

