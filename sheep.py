import logging
import random
from animal import Animal
import log


class Sheep(Animal):
    def __init__(self, init_pos_limit=10.0, sheep_move_dist=0.5):
        super().__init__(random.uniform(-init_pos_limit, init_pos_limit),
                         random.uniform(-init_pos_limit, init_pos_limit))
        self.sheep_move_dist = sheep_move_dist
        log.log_debug('sheep.py', 'Sheep', '__init__', str(init_pos_limit) + str(sheep_move_dist), str(None))

    def move(self):
        axis = random.choice(('x', 'y'))
        self.x += random.choice((self.sheep_move_dist, -self.sheep_move_dist)) if axis == 'x' else 0
        self.y += random.choice((self.sheep_move_dist, -self.sheep_move_dist)) if axis == 'y' else 0
        log.log_debug('sheep.py', 'Sheep', 'move', '', str(None))
