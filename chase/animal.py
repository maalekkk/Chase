from chase.parse_args import cls_logger, func_logger
import logging
import math
import random


@func_logger
def distance(wolf_coords, sheep_coords):
    return math.sqrt(((sheep_coords[0] - wolf_coords[0]) ** 2) + ((sheep_coords[1] - wolf_coords[1]) ** 2))


@cls_logger(func_logger)
class Animal:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self.x}, {self.y}, {self.move_dist})")

    @property
    def coords(self):
        return [self.x, self.y]

    def move(self, param):
        pass


@cls_logger(func_logger)
class Sheep(Animal):
    def __init__(self, init_pos_limit=10.0, sheep_move_dist=0.5):
        super().__init__(random.uniform(-init_pos_limit, init_pos_limit),
                         random.uniform(-init_pos_limit, init_pos_limit))
        self.move_dist = sheep_move_dist
        logging.info(f"{self.__class__.__name__} -> Start position {self.coords}")

    def move(self, param=None):
        old_x = self.x
        old_y = self.y
        axis = random.choice(('x', 'y'))
        self.x += random.choice((self.move_dist, -self.move_dist)) if axis == 'x' else 0
        self.y += random.choice((self.move_dist, -self.move_dist)) if axis == 'y' else 0
        if self.x != old_x or self.y != old_y:
            logging.info(f"{self.__class__.__name__} -> Move from {[old_x, old_y]} to {self.coords}")


@cls_logger(func_logger)
class Wolf(Animal):
    def __init__(self, wolf_move_dist=1.0):
        super().__init__()
        self.move_dist = wolf_move_dist
        logging.info(f"{self.__class__.__name__} -> Start position {self.coords}")

    def find_the_nearest_sheep(self, sheep):
        sheep_distances = [distance(self.coords, single_sheep.coords) for single_sheep in sheep]
        nearest_sheep_distance = min(sheep_distances)
        return sheep[sheep_distances.index(nearest_sheep_distance)], nearest_sheep_distance

    def divide_section(self, point_a, point_b, total_distance):
        m = total_distance - self.move_dist
        x = float((m * point_a[0]) + (self.move_dist * point_b[0])) / (self.move_dist + m)
        y = float((m * point_a[1]) + (self.move_dist * point_b[1])) / (self.move_dist + m)
        return x, y

    def move(self, sheep):
        old_x = self.x
        old_y = self.y
        nearest_sheep, nearest_sheep_distance = self.find_the_nearest_sheep(sheep)
        if nearest_sheep_distance < self.move_dist:
            return nearest_sheep
        else:
            self.x, self.y = self.divide_section(self.coords, nearest_sheep.coords,
                                                 nearest_sheep_distance)
        if self.x != old_x or self.y != old_y:
            logging.info(f"{self.__class__.__name__} -> Move from {[old_x, old_y]} to {self.coords} ")
