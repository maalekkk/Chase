import math
from animal import Animal
from parse_args import cls_logger, func_logger


def distance(wolf_coords, sheep_coords):
    return math.sqrt(((sheep_coords[0] - wolf_coords[0]) ** 2) + ((sheep_coords[1] - wolf_coords[1]) ** 2))


@cls_logger(func_logger)
class Wolf(Animal):
    def __init__(self, wolf_move_dist=1.0):
        super().__init__()
        self.move_dist = wolf_move_dist

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
        nearest_sheep, nearest_sheep_distance = self.find_the_nearest_sheep(sheep)
        if nearest_sheep_distance < self.move_dist:
            return nearest_sheep
        else:
            self.x, self.y = self.divide_section(self.coords, nearest_sheep.coords,
                                                 nearest_sheep_distance)
