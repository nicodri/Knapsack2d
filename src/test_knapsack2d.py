import numpy as np
from numpy.random import random

from knapsack2d import Knapsack2d


def including_sample(w0=1, h0=1, v0=5, Nx=10, Ny=10):
    '''
    Helper to build Nx*Ny rectangles with w0< w <= w0 + N and h0< h <= h0 + N
    which contain the initial rectanle (w0, h0) but with a lower value.
    As a result, (w0, h0, v0) outperforms them and can be considered as noise.
    Used to expand the setup without changing the result.
    '''
    rectangles = [(w0, h0, v0)]
    for i in xrange(1, Nx+1):
        for j in xrange(1, Ny+1):
            v = v0*random()
            r = (w0 + i, h0 + j, v)
            rectangles.append(r)
    return rectangles


def test_simple():
    '''
    Test arrangement building on a simple configuration.
    '''
    setup = (45, 48, [(4, 28, 4.0), (8, 10, 20.0)])
    knap = Knapsack2d(*setup)
    knap.build()
    assert(knap.F[-1, -1] == 520)
    assert(len(knap.arrangement[knap.W, knap.H]) == 26)


def test_simple_opt():
    '''
    Test arrangement optimized building on a simple configuration.
    '''
    setup = (45, 48, [(4, 28, 4.0), (8, 10, 20.0)])
    knap = Knapsack2d(*setup)
    knap.build_opt()
    assert(knap.F[-1, -1] == 520)
    assert(len(knap.arrangement[knap.W, knap.H]) == 26)


def test_output():
    setup = (45, 48, [(4, 28, 4.0), (8, 10, 20.0)])
    knap = Knapsack2d(*setup)
    knap.build_opt()
    output = knap.get_output()
    assert(output == '520.0\n45 48\n0 0 8 10 20.0\n0 10 8 20 20.0\n0 20 8 30 20.0\n0 30 8 40 20.0\n8 0 16 10 20.0\n8 10 16 20 20.0\n8 20 16 30 20.0\n8 30 16 40 20.0\n16 0 24 10 20.0\n16 10 24 20 20.0\n16 20 24 30 20.0\n16 30 24 40 20.0\n0 40 10 48 20.0\n10 40 20 48 20.0\n24 0 34 8 20.0\n24 8 34 16 20.0\n24 16 34 24 20.0\n24 24 34 32 20.0\n24 32 34 40 20.0\n24 40 34 48 20.0\n34 0 44 8 20.0\n34 8 44 16 20.0\n34 16 44 24 20.0\n34 24 44 32 20.0\n34 32 44 40 20.0\n34 40 44 48 20.')


def test_including_sample():
    # Define global setup
    W = 45
    H = 48
    ref0 = (3, 4, 2.)
    ref1 = (8, 10, 25.0)
    ref2 = (7, 9, 14)
    ref3 = (17, 14, 80)
    rectangles = [ref1, ref2, ref3]

    # Generate worse rectangles
    rectangles += including_sample(*ref0, Nx=40, Ny=40)
    rectangles += including_sample(*ref1, Nx=35, Ny=35)
    rectangles += including_sample(*ref2, Nx=35, Ny=35)
    rectangles += including_sample(*ref3, Nx=25, Ny=30)

    # Run experiment
    setup = (W, H, rectangles)
    knap = Knapsack2d(*setup)
    knap.build()
    assert(knap.F[-1, -1] == 695.)
    assert(len(knap.arrangement[knap.W, knap.H]) == 17)

    # optim version
    knap.build_opt()
    assert(knap.F[-1, -1] == 695.)
    assert(len(knap.arrangement[knap.W, knap.H]) == 17)


def test_small_rectangles():
    # Define global setup
    W = 45
    H = 48
    ref0 = (1, 1, 0.1)
    ref1 = (8, 10, 25.0)
    ref2 = (7, 9, 14)
    ref3 = (17, 14, 80)
    rectangles = [ref1, ref2, ref3]

    # Generate worse rectangles
    rectangles += including_sample(*ref0, Nx=40, Ny=40)
    rectangles += including_sample(*ref1, Nx=35, Ny=35)
    rectangles += including_sample(*ref2, Nx=35, Ny=35)
    rectangles += including_sample(*ref3, Nx=25, Ny=30)

    # Run experiment
    setup = (W, H, rectangles)
    knap = Knapsack2d(*setup)
    knap.build()
    # Float comparison
    assert(np.abs(knap.F[-1, -1] - 694.4) < 10**(-8))
    assert(len(knap.arrangement[knap.W, knap.H]) == 106)

    # optim version
    knap.build_opt()
    # Float comparison
    assert(np.abs(knap.F[-1, -1] - 694.4) < 10**(-8))
    assert(len(knap.arrangement[knap.W, knap.H]) == 106)
