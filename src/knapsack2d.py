import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def update_in_range(mydict, updates):
    '''
    Update in place mydict in the range defined in the dictionary udpates.
    args:
        updates: {(imin, imax, jmin, jmax) : value}
    '''
    for ranges, value in updates.iteritems():
        for i in xrange(ranges[0], ranges[1]):
            for j in xrange(ranges[2], ranges[3]):
                mydict[(i, j)] = value


def merge_optima(i, j, F, arrangement, axis=0):
    '''
    Update in-place F and arrangement at the point (i, j) by merging along the
    axis the optimum combinaison of two subsequences if exists.
    '''
    # Interpreting axis argument
    index = j if axis else i
    for k in xrange(1, index/2+1):
        # Coordinates to considered for the two subsequence candidate
        # Will try to merge F[c[0]] and F[c[0]] which concatenated cover
        # the full space of the rectangle induced by F[i, j]
        if axis:
            c = [(i, k), (i, j-k)]
        else:
            c = [(k, j), (i-k, j)]
        # Possible new value
        value_merged = F[c[0]] + F[c[1]]
        if value_merged > F[i, j]:
            F[i, j] = value_merged
            # Updating the arrangement if one subsequence is empty (and as a
            # result not in arrangement)
            if c[0] not in arrangement:
                arrangement[(i, j)] = arrangement[c[1]]
            elif c[1] not in arrangement:
                arrangement[(i, j)] = arrangement[c[0]]
            # Case both subsequences contain rectangles.
            # Updata Concatenating arrangement with index shift along x for the
                # second one
            else:

                if axis:
                    a_shifted = [
                        (e[0], e[1] + j - k, e[2], e[3] + j - k, e[4]) for e in arrangement[(i, k)]]
                else:
                    a_shifted = [
                        (e[0] + i - k, e[1], e[2] + i - k, e[3], e[4]) for e in arrangement[(k, j)]]
                arrangement[(i, j)] = arrangement[c[1]] + a_shifted


class Knapsack2d(object):

    """docstring for Knapsack2d"""

    def __init__(self, W, H, rectangles=[]):
        self.W = W
        self.H = H
        self.rectangles = rectangles

    def build(self):
        # Store the total value
        F = np.zeros((self.W+1, self.H+1))
        # Stores the arrangement for each configuration (i,j)
        # key: (i,j) value: [(x1, y1, x2, y2, v)]
        arrangement = {}

        # Best configuration with 1 rectangle
        for r in self.rectangles:
            w, h, v = r
            for i in xrange(1, self.W+1):
                for j in xrange(1, self.H+1):
                    # Rotations of 90 degree possible
                    if ((w <= i and h <= j) or (h <= i and w <= j)) and (v > F[i, j]):
                        F[i, j] = v
                        if not (w <= i and h <= j):
                            arrangement[(i, j)] = [(0, 0, h, w, v)]
                        else:  # by default if two positions possible
                            arrangement[(i, j)] = [(0, 0, w, h, v)]
        # Iteration
        for i in xrange(1, self.W+1):
            for j in xrange(1, self.H+1):
                # Combining 2 sub configurations
                # Along x
                merge_optima(i, j, F, arrangement, axis=0)

                # Along y
                merge_optima(i, j, F, arrangement, axis=1)

        self.F = F
        self.arrangement = arrangement

    def build_opt(self):
        N = len(self.rectangles)
        # Store the total value
        F = np.zeros((self.W+1, self.H+1))
        # Stores the arrangement for each configuratin (i,j)
        # key: (i,j) value: [(x1, y1, x2, y2, v)]
        arrangement = {}

        # Best configuration with 1 rectangle
        # Sorting the rectangle list by decreasing values
        # Complexity is O(N log(N))
        self.rectangles.sort(reverse=True, key=lambda x: x[2])
        ind_max = max(self.W, self.H) + 1
        ind_min = min(self.W, self.H) + 1
        curr_rect = 0
        while ind_max > 0 and ind_min > 0 and curr_rect < N:
            r = self.rectangles[curr_rect]
            w, h, v = r
            min_d = min(w, h)
            max_d = max(w, h)
            if max_d < ind_max or min_d < ind_min:
                if min_d >= ind_min:
                    # Setting F
                    F[min_d:max_d, max_d:ind_max] = v
                    F[max_d:ind_max, min_d:ind_max] = v
                    # Setting arragnement
                    updates = {(min_d, max_d, max_d, ind_max): [(0, 0, min_d, max_d, v)],
                               (max_d, ind_max, min_d, ind_max): [(0, 0, max_d, min_d, v)]}
                    update_in_range(arrangement, updates)
                # Case 2:
                elif max_d < ind_min:
                    # Setting F
                    F[min_d:ind_min, max_d:self.H+1] = v
                    F[ind_min:ind_max, ind_min:ind_max] = v
                    F[max_d:self.W+1, min_d:ind_min] = v
                    # Setting arrangement
                    updates = {(min_d, ind_min, max_d, self.H+1): [(0, 0, min_d, max_d, v)],
                               (ind_min, ind_max, ind_min, ind_max): [(0, 0, min_d, max_d, v)],
                               (max_d, self.W+1, min_d, ind_min): [(0, 0, max_d, min_d, v)]}
                    update_in_range(arrangement, updates)
                # Case 3:
                else:
                    # Setting F
                    F[min_d:ind_min, max_d:self.H+1] = v
                    F[max_d:self.W+1, min_d:ind_min] = v
                    F[min_d:max_d, max_d:ind_max] = v
                    F[max_d:ind_max, min_d:ind_max] = v

                    # Setting arrangement
                    updates = {(min_d, ind_min, max_d, self.H+1): [(0, 0, min_d, max_d, v)],
                               (min_d, max_d, max_d, ind_max): [(0, 0, min_d, max_d, v)],
                               (max_d, ind_max, min_d, ind_max): [(0, 0, max_d, min_d, v)],
                               (max_d, self.W+1, min_d, ind_min): [(0, 0, max_d, min_d, v)]}
                    update_in_range(arrangement, updates)

                ind_min = min_d
                ind_max = max_d
            curr_rect += 1

        # Iteration
        for i in xrange(1, self.W+1):
            for j in xrange(1, self.H+1):
                # Combining 2 sub configurations
                # Along x
                merge_optima(i, j, F, arrangement, axis=0)

                # Along y
                merge_optima(i, j, F, arrangement, axis=1)

        self.F = F
        self.arrangement = arrangement

    def draw_arrangement(self, filename):
        '''
        Method to draw the previously built arrangement. Save it
        as filename in the local path '../data/'
        Raise an error if no arrangement built.
        The plot is rescaled in the unit square as the library used
        plot patches in the unit square.
        '''
        # Check model built
        if self.arrangement is None:
            raise ValueError('Build the arrangement before drawing')

        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='equal')
        patterns = ['-', '+', 'x', 'o', 'O', '.', '*']
        lp = len(patterns)
        # Converting to float for the rescale
        W, H = float(self.W), float(self.H)

        # Building patches (rescaled in the unit box)
        for i, r in enumerate(self.arrangement[self.W, self.H]):
            p = patches.Rectangle(
                (r[0]/W, r[1]/H), (r[2]-r[0])/W, (r[3]-r[1])/H,
                hatch=patterns[i%lp],
                fill=False
            )
            ax.add_patch(p)
        fig.savefig('../data/{}'.format(filename), dpi=90, bbox_inches='tight')

    def get_output(self):
        '''
        Return the output in the required format.
        '''
        # Check model built
        if self.arrangement is None:
            raise ValueError('Build the arrangement before saving')
        # Line 1: total value
        out = str(self.F[self.W, self.H]) + '\n'
        # Line 2
        out += str(self.W) + ' ' + str(self.H) + '\n'
        # Next lines: rectangles in format (x1, y1, x2, y2, v)
        for r in self.arrangement[self.W, self.H]:
            out += ' '.join([str(e) for e in r]) + '\n'

        # Need to retrieve the last \n
        return out[:-2]


