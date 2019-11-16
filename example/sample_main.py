""" Google Hash 2019-q """
from omar_utils.basic.file_basics import convert_to_number
from omar_utils.basic.sets import Set
# local imports
from google_hash.example.sample_algorithms import *
from google_hash.api import Api


# --- 0) Define data structures ----------------------------------

def data_structures():
    """this method is not actually used"""

    # raw input:
    '4'
    'H 3 cat beach sun'
    'V 2 selfie smile'
    ...

    # problem (data-points):
    _ = [
        ['H', 3, {'cat', 'beach', 'sun'}],
        ['V', 2, {'selfie', 'smile'}],
        ...]

    # solution:
    _ = \
        [[0], [3], [1, 2], ...]

    # raw output:
    '3'     # length
    '0'
    '3'
    '1 2'
    ...


# --- 1) write file names ----------------------------------------

file_names = {'a': 'problems/a_example.txt',
              'b': 'problems/b_lovely_landscapes.txt',
              'c': 'problems/c_memorable_moments.txt',
              'd': 'problems/d_pet_pictures.txt',
              'e': 'problems/e_shiny_selfies.txt'}


# --- 2) clean your data -----------------------------------------

def cleaning_method(s: str) -> list:
    """convert a line of data into something useful
    example: '1 a b c' -> [1, {'a', 'b', 'c'}]
    """
    v = s.split()
    v = convert_to_number(v)
    return [v[0], v[1], Set(*v[2:])]


# --- 3) representation method -----------------------------------

def repr_method(solution):
    """
    string to use when printing solution
    :param solution: list of slides     [[0], [3], [1, 2]]
    :return: str                        3\n0\n3\n1 2
    """
    return '\n'.join([str(len(solution))] +
                     [' '.join([str(j) for j in i]) for i in solution])


# --- 4) score method (optional) ---------------------------------

def score_method(solution, problem):
    """
    calc score of solution (based on problem)
    :param solution:
    :param problem:
    :return: score
    """
    pt = 0
    for i in range(len(solution) - 1):
        a = solution[i]
        assert 1 <= len(a) <= 2
        if len(a) == 1:
            assert problem[a[0]][0] == 'H'
        if len(a) == 2:
            assert problem[a[0]][0] == 'V' and problem[a[1]][0] == 'V'

        tags1 = sum([problem[j][-1] for j in solution[i]])  # sum the tags of all the photos
        tags2 = sum([problem[j][-1] for j in solution[i+1]])  # sum the tags of all the photos

        a = len(tags1 & tags2)  # A & B
        b = len(tags1 - tags2)  # A - B
        c = len(tags2 - tags1)  # B - A
        pt += min(a, b, c)
    return pt


# --- 5) pick algorithm & define data-set ------------------------

# algorithm
algorithm = example_a

# data-set
problem_index = 'a'  # pick from names
first_line = 2  # ignore lines before first_line
last_line = -1  # ignore lines after last (-1 to not ignore)


# ----------------------------------------------------------------


# --- automatic init, compile and set-up API ---------------------

API = Api()
API.compile(file_names=file_names,
            cleaning_method=cleaning_method,
            problem_index=problem_index,
            algorithm=algorithm,
            repr_method=repr_method,
            score_method=score_method)
API.settings(first_line=first_line,
             last_line=last_line)


# --- automatic API activation -----------------------------------

if __name__ == '__main__':
    API.run()
