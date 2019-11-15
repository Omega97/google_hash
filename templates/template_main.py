""" Google Hash 2019-q """

# local imports
from google_hash.example.sample_algorithms import *
from google_hash.api import Api


# --- 0) Define data structures -------------------------------------------------

def data_structures():
    """this method is not actually used, just write data structures as variables or comments"""

    # raw input:
    ...

    # problem (data-points):
    ...

    # solution:
    ...

    # raw output:
    ...


# --- 1) write file names -------------------------------------------------------

file_names = {'a': 'problems/....txt',
              'b': '...',
              ...: ...}


# --- 2) clean your data --------------------------------------------------------

def cleaning_method(s: str) -> list:
    """convert a line of data into something useful
    """
    ...


# --- 3) define data-set ---------------------------------------------

problem_index = 'a'  # pick from names
first_line = 1  # ignore lines before first_line
last_line = -1  # ignore lines after last (-1 to not ignore)


# --- 4) representation method --------------------------------------

def repr_method(solution):
    """
    string to use when printing solution
    :param solution: list of slides
    :return: str
    """
    ...


# --- 5) score method (optional) --------------------------------------

def score_method(solution, problem):    # optional
    """
    calc score of solution (based on problem)
    """
    ...


# --- 6) pick algorithm --------------------------------------

algorithm = example_a


# --- 7) init, compile and set-up API ----------------------------------

API = Api()
API.compile(file_names=file_names,
            cleaning_method=cleaning_method,
            problem_index=problem_index,
            algorithm=algorithm,
            repr_method=repr_method,
            score_method=score_method)
API.settings(first_line=first_line,
             last_line=last_line)


# --- 8) activate API ----------------------------------

if __name__ == '__main__':
    API.activate()
