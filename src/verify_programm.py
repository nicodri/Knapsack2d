import sys

from knapsack2d import Knapsack2d
from helper_io import read_input
from verify import validate_output

if __name__ == '__main__':
    # Reading raw input
    input_ = ''
    while True:
        try:
            input_ += raw_input() + '\n'
        except EOFError:
            break

    # Converting input (remove last \n)
    finput = read_input(input_[:-2])

    # Build Knapsack2d
    knap = Knapsack2d(*finput)
    knap.build()

    # Validate and return output
    output = knap.get_output()
    print output
