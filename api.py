from omar_utils.tests.timer import Timer
from omar_utils.basic.file_basics import file_reader
from google_hash.utils import fancy_print
from google_hash.solution_class import Solution


class Api:
    """Application Programming Interface"""

    def __init__(self):
        self.names = None
        self.cleaning_method = None
        self.problem_index = None
        self.do_save_solution = None
        self.do_show = None
        self.first_line = None
        self.last_line = None
        self.algorithm = None
        self.repr_method = None
        self.score_method = None
        self.data_sets = None
        self.problem = None
        self.solution = None

    def compile(self, file_names, cleaning_method, problem_index, algorithm, repr_method, score_method=None):
        self.names = file_names
        self.cleaning_method = cleaning_method
        self.problem_index = problem_index
        self.algorithm = algorithm
        self.repr_method = repr_method
        self.score_method = score_method
        return self

    def settings(self, first_line=0, last_line=-1, do_save_solution=True, do_show=True):
        self.first_line = first_line
        self.last_line = last_line
        self.do_save_solution = do_save_solution
        self.do_show = do_show
        return self

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def set_problem(self, problem_index):
        self.problem_index = problem_index

    def set_first_line(self, first_line):
        self.first_line = first_line

    def set_last_line(self, last_line):
        self.last_line = last_line

    def set_do_show(self, do_show):
        self.do_show = do_show

    def gen_data_sets(self):  # todo simplify
        """dict of names with corresponding data-set generator"""
        self.data_sets = {i: data_points_generator(file_name=self.names[i],
                                                   first_line=self.first_line,
                                                   last_line=self.last_line,
                                                   cleaning_method=self.cleaning_method) for i in self.names}

    def define_problem(self):
        timer = Timer()
        self.problem = list(self.data_sets[self.problem_index]())  # when called returns data generator
        if self.do_show:
            fancy_print(self.data_sets[self.problem_index](), lines=10, title='problem ' + self.problem_index)
            timer('loading data')

    def compute_solution(self):  # todo
        # compute solution
        timer = Timer()
        raw_solution = self.algorithm(self.problem)
        if self.do_show:
            timer('computing raw solution')

        # convert solution to Solution
        self.solution = Solution(raw_solution, self.problem, self.repr_method, self.score_method)
        if self.do_show:
            timer('solution')

    def compute_score(self):
        # compute score
        timer = Timer()
        score = self.solution.get_score()
        if self.do_show:
            fancy_print(self.solution, lines=10, title='solution ' + self.problem_index)
            print('\nscore =', score, '\n')
            timer('score')

    def save(self):
        if self.do_save_solution:
            self.solution.save(name=self.problem_index)

    def activate(self):
        self.gen_data_sets()
        self.define_problem()
        self.compute_solution()
        self.compute_score()
        self.save()


def data_points_generator(file_name, first_line, last_line, cleaning_method=None):
    def wrapped():
        """generator of data-points"""
        count = 1
        for line in file_reader(file_name):
            if count < first_line:
                pass
            elif count > last_line >= 0:
                break
            else:
                yield cleaning_method(line) if cleaning_method else line
            count += 1

    return wrapped
