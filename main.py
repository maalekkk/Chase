import argparse
import os
from configparser import ConfigParser
from simulation import Simulation
import logging


def check_int_number(argument):
    number = 0
    try:
        number = int(argument)
    except ValueError:
        print("The given argument isn't a number.")
    if number <= 0:
        raise argparse.ArgumentTypeError("Number(argument) must be positive value")
    return number


def check_float_number(argument):
    number = 0.0
    try:
        number = float(argument)
    except ValueError:
        print("The given argument isn't a number.")
    if number <= 0:
        raise argparse.ArgumentTypeError("Number(argument) must be positive value")
    return number


def check_bool(argument):
    if argument is not True or argument is not False:
        raise argparse.ArgumentTypeError("Wait argument must be bool value.")


def config_parsing(filename):
    config_parser = ConfigParser()
    config_parser.read(filename)
    terrain = config_parser['Terrain']
    init_pos_limit = abs(terrain.getfloat('InitPosLimit'))
    movement = config_parser['Movement']
    sheep_move_dist = check_float_number(movement.getfloat('SheepMoveDist'))
    wolf_move_dist = check_float_number(movement.getfloat('WolfMoveDist'))
    return init_pos_limit, sheep_move_dist, wolf_move_dist


def main():
    print('Wolf and sheep simulation')

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-c', '--config', help='Specifying a configuration file', action='store',
                                 metavar='FILE', dest='configuration_file', type=str)
    argument_parser.add_argument('-d', '--dir', action='store',
                                 help='Specifies a subdirectory of the current directory where the pos.json and '
                                      'alive.csv files are to be saved', metavar='DIR', dest='directory', type=str)
    argument_parser.add_argument('-l', '--log', action='store', help='Specifies the level of events to be logged.',
                                 metavar='LEVEL', dest='log_level', type=str)
    argument_parser.add_argument('-r', '--rounds', action='store', help='Specifies the number of turns.', metavar='NUM',
                                 type=check_int_number, dest='rounds_number')
    argument_parser.add_argument('-s', '--sheep', action='store',
                                 help='Specifies the number of sheep.', metavar='NUM', type=check_int_number,
                                 dest='sheep_number')
    argument_parser.add_argument('-w', '--wait', action='store',
                                 help='Specifies that after displaying basic information about the simulation state '
                                      'at the end of each round, the rest of the simulation should be stopped until '
                                      'the user presses a key.',
                                 dest='wait', type=check_bool)
    arguments = argument_parser.parse_args()

    parameters = {
        'round_number': 50,
        'sheep_number': 15,
        'init_pos_limit': 10.0,
        'wolf_move_dist': 1,
        'sheep_move_dist': 0.5,
        'wait': False,
        'directory': None,
        'log': None
    }

    log_levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    if arguments.configuration_file:  # trzeba zrobić obsługę wyjątku jeśli by nie było takiego pliku
        parameters['init_pos_limit'], parameters['sheep_move_dist'], parameters['wolf_move_dist'] = config_parsing(
            arguments.configuration_file)
    if arguments.directory:
        parameters['directory'] = arguments.directory
        if not os.path.exists(arguments.directory):
            os.makedirs(arguments.directory)
    if arguments.log_level:
        logging.basicConfig(format='%(process)d-%(levelname)s-%(asctime)s-%(message)s', filename='chase.log',
                            level=log_levels.get(str(arguments.log_level)))
    if arguments.rounds_number:
        parameters['round_number'] = arguments.rounds_number if arguments.rounds_number > 0 else 50
    if arguments.sheep_number:
        parameters['sheep_number'] = arguments.sheep_number if arguments.sheep_number > 0 else 15
    if arguments.wait:
        parameters['wait'] = arguments.wait

    simulation = Simulation(sheep_number=parameters.get('sheep_number'),
                            init_pos_limit=parameters.get('init_pos_limit'),
                            wolf_move_dist=parameters.get('wolf_move_dist'),
                            sheep_move_dist=parameters.get('sheep_move_dist'))
    simulation.simulate(round_number=parameters.get('round_number'),
                        wait=parameters.get('wait'),
                        json_file_path=(str(parameters.get('directory')) + r"\pos.json") if parameters.get(
                            'directory') is not None else r"pos.json",
                        csv_file_path=(str(parameters.get('directory')) + r"\alive.csv" if parameters.get(
                            'directory') is not None else r"alive.csv"))


if __name__ == "__main__":
    main()
