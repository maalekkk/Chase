import random
from animal import Animal

init_pos_limit = 10.0


class Sheep:
    def __init__(self):
        self.x = random.uniform(-init_pos_limit, init_pos_limit)
        self.y = random.uniform(-init_pos_limit, init_pos_limit)
        self.sheep_move_dist = 0.5

    def move(self):
        direction = random.randint(1, 4)
        if direction == 1:
            self.x += self.sheep_move_dist
        elif direction == 2:
            self.x -= self.sheep_move_dist
        elif direction == 3:
            self.y += self.sheep_move_dist
        elif direction == 4:
            self.y -= self.sheep_move_dist
