import sys

from knapsack2d import Knapsack2d
from helper_io import read_input
from verify import validate_output

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python main.py input.in'
        sys.exit()

    # Open input
    with open(sys.argv[1]) as f:
        finput = read_input(f.read()[:-2])
    fname = sys.argv[1].split('.')[0]

    # Build Knapsack2d
    knap = Knapsack2d(*finput)
    knap.build()
    knap.draw_arrangement('../data/{}.png'.format(fname))

    # Validate and save output
    output = knap.get_output()
    if validate_output(output):
        # Saving
        with open('{}.out'.format(fname), 'w') as f:
            f.write(output)
        print 'Output saved as {}.out'.format(fname)
    else:
        print 'Wrong output format'