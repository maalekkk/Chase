import csv
import math
import argparse
import wolf
import sheep
import json


def distance(wolf_coords, sheep_coords):
    return math.sqrt(((sheep_coords[0] - wolf_coords[0]) ** 2) + ((sheep_coords[1] - wolf_coords[1]) ** 2))


def save_to_json_file(positions_data):
    with open('pos.json', mode='w') as json_file:
        json.dump(positions_data, json_file, indent=5)


def save_to_csv_file(alive_sheep_data):
    with open('alive.csv', mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['round_no', 'alive_sheep'])
        writer.writeheader()
        for row in alive_sheep_data:
            writer.writerow({'round_no': row[0], 'alive_sheep': row[1]})


class Simulation:
    def __init__(self):
        self.wolf = wolf.Wolf()
        self.sheep = [sheep.Sheep() for i in range(15)]

    def simulate(self):
        starters_sheep = self.sheep.copy()
        print('Round number', '{0: <15}'.format('Wolf position'), '{0: <8}'.format('Number of live sheep'),
              'Dead sheep number')
        positions_data = []
        alive_sheep_data = []
        for i in range(50):
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
                        self.sheep.remove(dead_sheep)
                        break
            print('{0: <12}'.format(str(i + 1)), '{0: <7}'.format(str("{:.3f}".format(self.wolf.x))),
                  '{0: <7}'.format(str("{:.3f}".format(self.wolf.y))), '{0: <20}'.format(len(self.sheep)),
                  num_of_dead_sheep)
            positions_data.append({
                "round_no": str(i + 1),
                "wolf_pos": self.wolf.coords,
                "sheep_pos": [single_sheep.coords for single_sheep in self.sheep]})
            alive_sheep_data.append([i + 1, len(self.sheep)])
        save_to_json_file(positions_data)
        save_to_csv_file(alive_sheep_data)


def main():
    print('Wolf and sheep simulation')
    simulation = Simulation()
    simulation.simulate()

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-c', '--config', help='Specifying a configuration file', action='store',
                                 metavar='FILE')
    argument_parser.add_argument('-d', '--dir', action='store',
                                 help='Specifies a subdirectory of the current directory where the pos.json and '
                                      'alive.csv files are to be saved',
                                 metavar='DIR')
    argument_parser.add_argument('-l', '--log', action='store', help='Specifies the level of events to be logged.',
                                 metavar='LEVEL')
    argument_parser.add_argument('-r', '--rounds', action='store', help='Specifies the number of turns.', metavar='NUM')
    argument_parser.add_argument('-s', '--sheep', action='store',
                                 help='Specifies that after displaying basic information about the simulation state '
                                      'at the end of each round, the rest of the simulation should be stopped until '
                                      'the user presses a key.', metavar='NUM')
    argument_parser.add_argument('-w', '--wait', action='store_true', help="wait for input after each round")


if __name__ == "__main__":
    main()
