""" Google Hash 2019-q """
from basic.file_basics import file_to_list
from basic.tensors import split_tensor
from basic.sets import Set
# local imports
from google_hash.example.sample_solution import SlideShow
from google_hash.example.sample_algorithms import group_photos, group_slides


# 1) data generator -------------------------------------------------------------


def data_generator(name):
    """:returns a method that returns data when called"""
    def custom_file_import(first=0, last=None):
        """import data of the problem from file"""
        def improve(w):
            """modify a row of data"""
            if len(w) == 1:
                return [int(w[0])]
            else:
                return [w[0], int(w[1]), Set(*w[2:])]
        v = file_to_list(name + '.txt')[max(1, first):last]
        v = split_tensor(v)
        return [improve(i) for i in v]
    return custom_file_import


# 2) write file names and define data-set generators ----------------------------

names = {'a': 'problems/a_example',
         'b': 'problems/b_lovely_landscapes',
         'c': 'problems/c_memorable_moments',
         'd': 'problems/d_pet_pictures',
         'e': 'problems/e_shiny_selfies'}


# initialize data only when called
data_sets = {i: data_generator(names[i]) for i in names}


# -------------------------------------------------------------------------------


if __name__ == '__main__':

    from google_hash.utils import save_solution, build_final_alg, fancy_print
    from tests.timer import Timer

    # 3) load the data ----------------------------------------------------------

    timer = Timer()
    Name = 'd'
    p = data_sets[Name](last=100)
    fancy_print(p, title='Problem ' + Name)
    timer('loading\n')

    # 4) build final algorithm --------------------------------------------------

    alg = build_final_alg(SlideShow,
                          group_photos,
                          group_slides(k=5))

    # 5) compute solution -------------------------------------------------------

    sol = alg(p)
    timer()
    print('\nscore =', sol.get_score(), '\n')
    # print('\nSolution\n\n%s\n' % str(sol))
    fancy_print(sol, title='Solution')
    save_solution(sol, name=Name)
