""" Google Hash 2019-q """
from basic.file_basics import file_to_list
from basic.tensors import split_tensor
from basic.sets import Set
# local imports
from google_hash.templates.template_solution import Solution
# from google_hash.templates.template_algorithms import ...


# 1) data generator -------------------------------------------------------------


def data_generator(name):
    """:returns a method that returns data when called"""
    def custom_file_import(first=0, last=None):
        """import data of the problem from file"""
        def improve(w):
            """modify a row of data"""
            ...
        v = file_to_list(name + '.txt')[max(1, first):last]
        v = split_tensor(v)
        return [improve(i) for i in v]
    return custom_file_import


# 2) write file names and define data-set generators ----------------------------

names = {'a': 'problems/a_example',
         'b': 'problems/b_...',
         'c': 'problems/c_...',
         'd': 'problems/d_...',
         'e': 'problems/e_...'}


# initialize data only when called
data_sets = {i: data_generator(names[i]) for i in names}


# -------------------------------------------------------------------------------


if __name__ == '__main__':

    from google_hash.utils import save_solution, build_final_alg, fancy_print
    from tests.timer import Timer

    # 3) load the data ----------------------------------------------------------

    timer = Timer()
    Name = 'a'
    p = data_sets[Name](last=100)
    fancy_print(p, title='Problem ' + Name)
    timer('loading\n')

    # 4) build final algorithm --------------------------------------------------

    alg = build_final_alg(Solution, ...)

    # 5) compute solution -------------------------------------------------------

    sol = alg(p)
    timer()
    print('\nscore =', sol.get_score(), '\n')
    # print('\nSolution\n\n%s\n' % str(sol))
    fancy_print(sol, title='Solution')
    save_solution(sol, name=Name)
