import math
import wolf
import sheep


def distance(point_1, point_2):
    return math.sqrt(((point_2.x - point_1.x) ** 2) + ((point_2.y - point_1.y) ** 2))


def print_headers():
    print('| Round number |    Wolf position     | Number of live sheep | Dead sheep number |')


class Simulation:
    def __init__(self):
        self.wolf = wolf.Wolf()
        self.sheep = [sheep.Sheep() for i in range(15)]

    def simulate(self):
        print_headers()
        starters_sheep = self.sheep.copy()
        for i in range(150):
            if len(self.sheep) <= 0:
                break
            for single_sheep in self.sheep:
                single_sheep.move()
            dead_sheep = self.wolf.move(self.sheep)
            num_of_dead_sheep = '-'
            if dead_sheep is not None:
                for count, single_sheep in enumerate(starters_sheep):
                    if dead_sheep == single_sheep:
                        num_of_dead_sheep = count
                        print(dead_sheep.x, dead_sheep.y)
                        self.sheep.remove(dead_sheep)
                        break
            self.to_string(i, num_of_dead_sheep)

    def to_string(self, iterator, dead_sheep):
        print(str(iterator), str("{:.3f}".format(self.wolf.x)), str("{:.3f}".format(self.wolf.y)), len(self.sheep),
              dead_sheep)


def main():
    print('Wolf and sheep')
    simulation = Simulation()
    simulation.simulate()


if __name__ == "__main__":
    main()
