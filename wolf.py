from simulation import distance
from animal import Animal


class Wolf(Animal):
    def __init__(self):
        super().__init__()
        self.wolf_move_dist = 1.0

    def find_the_nearest_sheep(self, sheep):
        nearest_sheep = sheep[0]
        nearest_sheep_distance = distance(self.coords, nearest_sheep.coords)
        for single_sheep in sheep:
            calculate_distance = distance(self.coords, single_sheep.coords)
            if calculate_distance < nearest_sheep_distance:
                nearest_sheep = single_sheep
                nearest_sheep_distance = calculate_distance
        return nearest_sheep, nearest_sheep_distance

    def divide_section(self, x1, x2, y1, y2, total_distance):
        x = float(((total_distance - self.wolf_move_dist) * x1) + (self.wolf_move_dist * x2)) / (
                self.wolf_move_dist + (total_distance - self.wolf_move_dist))
        y = float(((total_distance - self.wolf_move_dist) * y1) + (self.wolf_move_dist * y2)) / (
                self.wolf_move_dist + (total_distance - self.wolf_move_dist))
        return x, y

    def move(self, sheep):
        nearest_sheep, nearest_sheep_distance = self.find_the_nearest_sheep(sheep)
        if nearest_sheep_distance < self.wolf_move_dist:
            return nearest_sheep
        else:
            self.x, self.y = self.divide_section(self.x, nearest_sheep.x, self.y, nearest_sheep.y,
                                                 nearest_sheep_distance)
