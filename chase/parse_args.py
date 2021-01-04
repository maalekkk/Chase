from configparser import ConfigParser
from types import FunctionType
from functools import wraps
import os
import logging
import argparse


def params_str(*args, **kwargs):
    args_str = ', '.join(str(arg) for arg in args)
    if kwargs:
        kwargs_str = ', '.join(f"{key}={val}" for key, val in kwargs.items())
        args_str += f", {kwargs_str}"
    return args_str


def func_logger(func, cls=None):
    @wraps(func)
    def wrapper(*args, **kwargs):
        params = params_str(*args, **kwargs)
        cls_name = f"{cls.__name__}." if cls else ''
        try:
            result = func(*args, **kwargs)
            logging.debug(f"{cls_name}{func.__name__}"
                          f"({params}) -> {result}")
        except Exception as e:
            logging.error(e)
            raise e
        return result

    return wrapper


def cls_logger(func):
    def wrapper(cls):
        methods = [y for x, y in cls.__dict__.items() if not x.startswith('__')
                   and type(y) == FunctionType]
        for method in methods:
            setattr(cls, method.__name__,
                    func(method, cls))
        return cls

    return wrapper


def parse_args(argument_parser):
    argument_parser.add_argument('-c', '--config', help='Specifying a configuration file', action='store',
                                 metavar='FILE', dest='configuration_file', type=str)
    argument_parser.add_argument('-d', '--dir', action='store',
                                 help='Specifies a subdirectory of the current directory where the pos.json and '
                                      'alive.csv files are to be saved', metavar='DIR', dest='directory', type=str)
    argument_parser.add_argument('-l', '--log', help='Specifies the level of events to be logged.',
                                 metavar='LEVEL', dest='log_level', type=str,
                                 choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
    argument_parser.add_argument('-r', '--rounds', action='store', help='Specifies the number of turns.', metavar='NUM',
                                 type=int, dest='rounds_number')
    argument_parser.add_argument('-s', '--sheep', action='store',
                                 help='Specifies the number of sheep.', metavar='NUM', type=int,
                                 dest='sheep_number')
    argument_parser.add_argument('-w', '--wait', action='store',
                                 help='Specifies that after displaying basic information about the simulation state '
                                      'at the end of each round, the rest of the simulation should be stopped until '
                                      'the user presses a key.',
                                 dest='wait', type=bool)
    arguments = argument_parser.parse_args()

    parameters = {
        'round_number': 50,
        'sheep_number': 15,
        'init_pos_limit': 10.0,
        'wolf_move_dist': 1,
        'sheep_move_dist': 0.5,
        'wait': False,
        'directory': '',
        'log': None
    }

    if arguments.configuration_file:
        parameters['init_pos_limit'], parameters['sheep_move_dist'], parameters['wolf_move_dist'] = config_parsing(
            arguments.configuration_file)
    if arguments.directory:
        parameters['directory'] = arguments.directory
        if not os.path.exists(arguments.directory):
            os.makedirs(arguments.directory)
    if arguments.log_level:
        logs_path = os.path.join(parameters['directory'], 'chase.log')
        logging.basicConfig(filename=logs_path,
                            filemode='w', datefmt='%H:%M:%S', level=arguments.log_level,
                            format='%(asctime)s,%(msecs)d :: %(levelname)-8s '
                                   ':: %(message)s')
    if arguments.rounds_number:
        parameters['round_number'] = arguments.rounds_number if arguments.rounds_number > 0 else 50
    if arguments.sheep_number:
        parameters['sheep_number'] = arguments.sheep_number if arguments.sheep_number > 0 else 15
    if arguments.wait:
        parameters['wait'] = arguments.wait
    return parameters


@func_logger
def config_parsing(filename):
    config_parser = ConfigParser()
    config_parser.read(filename)
    terrain = config_parser['Terrain']
    init_pos_limit = terrain.getfloat('InitPosLimit')
    if init_pos_limit != 0:
        if init_pos_limit < 0:
            init_pos_limit = abs(init_pos_limit)
            logging.warning(
                f"{config_parsing.__name__} -> The absolute value was taken from the value you entered (InitPosLimit).")
    else:
        msg = "Number must be not zero"
        logging.error(f"{config_parsing.__name__} -> {msg}")
        raise ValueError(msg)
    movement = config_parser['Movement']
    sheep_move_dist = movement.getfloat('SheepMoveDist')
    wolf_move_dist = movement.getfloat('WolfMoveDist')
    try:
        sheep_move_dist = check_positive_float(sheep_move_dist)
        wolf_move_dist = check_positive_float(wolf_move_dist)
    except argparse.ArgumentTypeError as e:
        logging.error(f"{config_parsing.__name__} -> {e} ")
        raise e
    return init_pos_limit, sheep_move_dist, wolf_move_dist


@func_logger
def check_positive_int(argument):
    try:
        number = int(argument)
    except ValueError as e:
        logging.error(f"{check_positive_int.__name__} -> {e}")
        raise e
    if number <= 0:
        msg = "Number(argument) must be positive value"
        logging.error(f"{check_positive_int.__name__} -> {msg}")
        raise argparse.ArgumentTypeError(msg)
    return number


@func_logger
def check_positive_float(argument):
    try:
        number = float(argument)
    except ValueError as e:
        logging.error(f"{check_positive_int.__name__} -> {e}")
        raise e
    if number <= 0:
        msg = "Number(argument) must be positive value"
        logging.error(f"{check_positive_int.__name__} -> {msg}")
        raise argparse.ArgumentTypeError(msg)
    return number


@func_logger
def check_bool(argument):
    if argument != 'True' and argument != 'False':
        msg = "Argument must be bool value(True or False)."
        logging.error(f"{check_positive_int.__name__} -> {msg}")
        raise argparse.ArgumentTypeError(msg)
    else:
        return bool(argument)
