import math

init_pos_limit = 10.0


def distance(wolf, sheep):
    return math.sqrt(((sheep.x - wolf.x) ** 2) + ((sheep.y - wolf.y) ** 2))


def main():
    print('Wolf and sheep')


if __name__ == "__main__":
    main()
