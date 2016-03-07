# Knapsack2d

This folder contains a solution to the knapsack 2d problem. Here is explained the structure of the folder.

* notebook: Provides an ipython notebook with the detailed approach and some tests. All the code there is reproduced in
a more maintanable and proper way in the 'src' folder. The code is shown only for illustration purposes.

* src: contains the code for the solution
    * knapsack2d.py : contains the Knapsack2d class which implement the targeted algorithm.
      * __init__(self, W, H, rectangles=[]) : constructor
      * build(self): build the optimized arrangement for the stored parameters
      * build_opt(self): build the optimized arrangement for the stored parameters with an optimized initialization (see notebook)
      * draw_arangement(self, filename): Draw the optimized arangement (need to be called after building) and save it in '../data/filename'. Drawing are rescaled in a unit square, random patterns are used to differentiate the rectangles from each other
      * get_output(self): build and return the output in the required format (as a raw string)
    * test_knapsack2d.py: contain some unit tests for the Knapsack2d class. Can be efficiently exectued as a routine with py.test
      * To install the package '$ pip install pytest' and '$pip install pytest-cov'.
      * To run the test with coverage: in src '$ py.test --cov-report term-missing --doctest-modules --cov --cov-report term-missing'
   * main.py: To solve the problem written in `inputname.in` with the Knapsack2d class. Saves the required output in 'data/inputname.out' and saves a drawing of the best agencement in 'data/inputname.png'. Usage: `python main.py ../data/inputname.in`
   * helper_io.py: helper for i/o
   * verify.py: Script provided. I implemented my solution as an independent to be able to called this script as asked but you may want to use the Knapsack2d class for more flexibility and features.
* data: contain input, output and drawing data.

Thanks for reading, feel free to reach me for any comment or feedback!

Nicolas Drizard 2016

    
