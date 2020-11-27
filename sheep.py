import random
from animal import Animal
from parse_args import cls_logger, func_logger


@cls_logger(func_logger)
class Sheep(Animal):
    def __init__(self, init_pos_limit=10.0, sheep_move_dist=0.5):
        super().__init__(random.uniform(-init_pos_limit, init_pos_limit),
                         random.uniform(-init_pos_limit, init_pos_limit))
        self.move_dist = sheep_move_dist

    def move(self):
        axis = random.choice(('x', 'y'))
        self.x += random.choice((self.move_dist, -self.move_dist)) if axis == 'x' else 0
        self.y += random.choice((self.move_dist, -self.move_dist)) if axis == 'y' else 0
