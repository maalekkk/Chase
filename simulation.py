import math
import wolf
import sheep

init_pos_limit = 10.0


def distance(wolf, sheep):
    return math.sqrt(((sheep.x - wolf.x) ** 2) + ((sheep.y - wolf.y) ** 2))


class Simulation:
    def __init__(self):
        self.wolf = wolf.Wolf()
        self.sheep = [sheep.Sheep() for i in range(15)]

    def to_string(self):
        pass


def main():
    print('Wolf and sheep')


if __name__ == "__main__":
    main()
