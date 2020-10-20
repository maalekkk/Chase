class Animal:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def coords(self):
        return [self.x, self.y]

    def move(self):
        pass
