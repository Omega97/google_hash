from os import mkdir
from time import time


class PercentageBar:
    """displays a neat percentage bar each time is called"""

    def __init__(self, length=20):
        self.length = length    # length of the bar
        self.p = 0.     # percentage
        self.round = -1     # rounded percentage to match bar length
        self.t = time()
        self.t_left = None

    def __repr__(self):
        out = '[' + '=' * self.round + ' ' * (self.length - self.round) + ']'
        out += '\t' * 2 + str(round(self.p * 100, 1)) + '%'
        if self.t_left:
            out += '\t' * 2 + str(round(-self.t_left, 2)) + ' s'
        return out

    def __call__(self, p):
        x = int(p * self.length)   # new .round
        if x > self.round:  # trigger print
            self.round = x
            t = time()
            if p - self.p > 0 and t - self.t > 0:
                speed = (p - self.p) / (t - self.t)
                self.t_left = (1-p) / speed
            else:
                self.t_left = None
            self.p = p
            self.t = t
            print(self)


def fancy_print(item, attribute='value', lines=4, title=''):
    """print a list or an attribute of the item"""
    print()
    print(title)
    print()
    if hasattr(item, attribute):
        v = getattr(item, attribute)
    else:
        v = item
    if lines is None:
        lines = len(v)
    if len(v) <= lines * 2:
        for i in v:
            print(i)
    else:
        for i in range(lines):
            print(v[i])
        print('... (%d) ...' % (len(v) - lines * 2))
        for i in range(lines):
            print(v[len(v) - lines + i])
    print()


def build_final_alg(solution_class, generator, *algorithms):
    """
    :param solution_class:
    :param generator: generates initial solution given
    :param algorithms:
    :return:
    """
    def final_alg(problem):
        out = generator(problem)
        for alg_ in algorithms:
            out = alg_(problem, out)
        return solution_class(out, problem)
    return final_alg


def save_solution(sol, name):
    """save the solution as file in the right format (given by self.class_)"""
    dir_name = 'solutions'
    try:
        mkdir(dir_name)
    except FileExistsError:
        pass
    name = dir_name + '\\' + name + '_' + str(sol.get_score()) + '.txt'
    with open(name, 'w') as file:
        file.write(sol.__repr__())
        file.close()
