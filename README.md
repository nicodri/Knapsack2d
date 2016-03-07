# Knapsack2d

This folder contains a solution to the knapsack 2d problem. Here is explained the structure of the folder.

* notebook: Provides an ipython notebook with the detailed approach and some tests. All the code there is reproduced in
a more maintanable and proper way in the 'src' folder. The code is shown only for illustration purposes.

* src: contains the code for the solution
    * knapsack2d.py : contains the Knapsack2d class which implement the targeted algorithm.
      * __init__(self, W, H, rectangles=[]) : constructor
      * build(self): build the optimized arrangement for the stored parameters
      * build_opt(self): build the optimized arrangement for the stored parameters with an optimized initialization (see notebook)
      * draw_arangement(self, filename): Draw the optimized arangement (need to be called after building) and save it in '../data/filename'
      * get_output(self): build and return the output in the required format (as a raw string)
    * test_knapsack2d.py: contain some unit tests for the Knapsack2d class. Can be efficiently exectued as a routine with py.test
      * To install the package '$ pip install pytest' and '$pip install pytest-cov'.
      * To run the test with coverage: in src '$ py.test --cov-report term-missing --doctest-modules --cov --cov-report term-missing'

    
