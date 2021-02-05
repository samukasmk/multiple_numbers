import argparse
from multiple_numbers import detects_multiplicable_numbers

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A command line tools that tells if is multiple numbers.')
    parser.add_argument('-m', '--multiplicables', type=int, nargs='*', default=[3, 5],
                        help='The multiplicable numbers to do the detections.')
    parser.add_argument('-i', '--initial-number', type=int, default=1,
                        help='The initial number to start the iteration')
    parser.add_argument('-f', '--final-number', type=int, default=100,
                        help='The final number to start the iteration')
    args = parser.parse_args()

    detects_multiplicable_numbers(args.initial_number, args.final_number, args.multiplicables)
