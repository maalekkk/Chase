from simulation import distance


class Wolf:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.wolf_move_dist = 1.0

    def find_the_nearest_sheep(self, sheep):
        nearest_sheep = sheep[0]
        nearest_sheep_distance = distance(self, nearest_sheep)
        for i in sheep:
            calculate_distance = distance(self, i)
            if distance(self, i) < nearest_sheep_distance:
                nearest_sheep = i
                nearest_sheep_distance = calculate_distance
        return nearest_sheep, nearest_sheep_distance

    def move(self, sheep):
        nearest_sheep, nearest_sheep_distance = self.find_the_nearest_sheep(sheep)
        if nearest_sheep < self.wolf_move_dist:
            return nearest_sheep
        else:
            pass
