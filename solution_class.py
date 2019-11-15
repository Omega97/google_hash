from os import mkdir
from time import strftime
from omar_utils.basic.file_basics import write_file


class Solution:
    """Solution"""
    def __init__(self, solution: list, problem: list, repr_method, score_method):
        """
        :param solution: list of slides     [[1, 20], [3], ... , [5]]
        :param problem: generator of problem data-points    [['H', 3, {beach, sun, cat}], ...]
        """
        self.solution = solution
        self.problem = problem
        self.score = None

        self.repr_method = repr_method
        self.score_method = score_method

    def __repr__(self):
        return self.repr_method(self.solution)

    def __len__(self):
        return len(self.solution)

    def __getitem__(self, item):
        return self.solution[item]

    def __call__(self, *args, **kwargs):
        return self.solution

    def __iter__(self):
        return iter(self.solution)

    def save(self, name='', dir_name='solutions', extension='.txt'):
        """save the solution as file in the right format"""
        try:
            mkdir(dir_name)
        except FileExistsError:
            pass
        if name:
            name += ' '
        name += strftime("%Y_%m_%d %H_%M_%S")
        write_file(dir_name + '\\' + name + extension, self.__repr__())

    def get_score(self):
        """compute score if hasn't already been computed"""
        if self.score is not None:
            return self.score
        else:
            # calc score
            s = self.score_method(self.solution, self.problem)
            self.score = s
            return s
