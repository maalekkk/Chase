from parse_args import parse_args
from simulation import Simulation
import argparse


def main():
    print('Wolf and sheep simulation')

    argument_parser = argparse.ArgumentParser()
    parameters = parse_args(argument_parser)

    simulation = Simulation(sheep_number=parameters.get('sheep_number'),
                            init_pos_limit=parameters.get('init_pos_limit'),
                            wolf_move_dist=parameters.get('wolf_move_dist'),
                            sheep_move_dist=parameters.get('sheep_move_dist'))

    simulation.simulate(round_number=parameters.get('round_number'),
                        wait=parameters.get('wait'),
                        json_file_path=(str(parameters.get('directory')) + r"\pos.json") if parameters.get(
                            'directory') != '' else r"pos.json",
                        csv_file_path=(str(parameters.get('directory')) + r"\alive.csv" if parameters.get(
                            'directory') != '' else r"alive.csv"))


if __name__ == "__main__":
    main()
