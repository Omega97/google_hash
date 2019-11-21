"""Google Hash Application Programming Interface"""
from omar_utils.tests.timer import Timer
from omar_utils.basic.file_basics import file_reader
# local imports
from utils import fancy_print
from solution_class import Solution


class Api:
    def __init__(self):
        # config
        self.names = None
        self.cleaning_method = None
        self.problem_index = None
        self.algorithm = None
        self.repr_method = None
        self.score_method = None
        self.data_sets = None
        self.problem = None
        self.solution = None
        # settings
        self.first_line = 0
        self.last_line = -1
        self.do_save_solution = True
        self.do_show = True
        self.do_report = False
        self.do_report_time = True

    def set(self, attribute, value):
        """override attribute, only if value is not None"""
        if value is not None:
            if hasattr(self, attribute):
                setattr(self, attribute, value)

    def report(self, *args, inline=1):
        if self.do_report:
            print('\n' * inline, '>>> ', ' '.join([str(i) for i in args]))

    def report_time(self, *args):
        if self.do_report_time:
            print('\n', '>>> ', ' '.join([str(i) for i in args]))

    def compile(self, file_names=None, cleaning_method=None, problem_index=None,
                algorithm=None, repr_method=None, score_method=None):
        """set methods (None = don't change)"""
        self.set('names', file_names)
        self.set('cleaning_method', cleaning_method)
        self.set('problem_index', problem_index)
        self.set('algorithm', algorithm)
        self.set('repr_method', repr_method)
        self.set('score_method', score_method)
        return self

    def settings(self, first_line=None, last_line=None, do_save_solution=None,
                 do_show=None, do_report=None, do_report_time=None):
        """set variables (None = don't change)"""
        self.set('first_line', first_line)
        self.set('last_line', last_line)
        self.set('do_save_solution', do_save_solution)
        self.set('do_show', do_show)
        self.set('do_report', do_report)
        self.set('do_report_time', do_report_time)
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

    # --- checks ------------------------------------------------------------------------

    def check_defined(self, *args, error_type=None):
        """checks that both args and kwargs are both not None, in witch case raises error_type"""
        if error_type is None:
            error_type = NotImplementedError
        not_defined_attr = []
        error = None
        # scan
        for attr in args:
            if hasattr(self, attr):
                if getattr(self, attr) is None:
                    not_defined_attr += [attr]
                    error = error_type(attr)
            else:
                not_defined_attr += [attr]
                error = AttributeError(attr)
        # report
        if len(not_defined_attr):
            self.report('Warning! Argument not defined:')
            for attr in not_defined_attr:
                self.report(' - ' + attr, inline=0)
            if error:
                raise error

    def optional(*args):
        """decorated methods are skipped if some parameter is missing"""

        def wrapped(fun):
            def wrapped_2(self, *ag, **kw):
                self.check_defined(*args, error_type=AssertionError)
                return fun(self, *ag, **kw)

            wrapped_2.__name__ = fun.__name__ + '_'
            return wrapped_2

        return wrapped

    def compulsory(*args):
        """decorated methods stop the routine execution if some parameter is missing"""

        def wrapped(fun):
            def wrapped_2(self, *ag, **kw):
                self.check_defined(*args, error_type=NotImplementedError)
                return fun(self, *ag, **kw)

            wrapped_2.__name__ = fun.__name__ + '_'
            return wrapped_2

        return wrapped

    # --- functionalities ---------------------------------------------------------------

    @compulsory('names', 'first_line', 'last_line', 'cleaning_method')
    def gen_data_sets(self):
        """dict of names with corresponding data-set generator"""
        self.data_sets = {i: data_points_generator(file_name=self.names[i],
                                                   first_line=self.first_line,
                                                   last_line=self.last_line,
                                                   cleaning_method=self.cleaning_method) for i in self.names}

    @compulsory('data_sets', 'problem_index')
    def define_problem(self):
        self.problem = list(self.data_sets[self.problem_index]())  # when called returns data generator
        if self.do_show:
            fancy_print(self.data_sets[self.problem_index](), lines=10, title='problem ' + self.problem_index)

    @compulsory('problem', 'repr_method', 'algorithm')
    def compute_solution(self):
        # compute solution
        raw_solution = self.algorithm(self.problem)
        self.solution = Solution(raw_solution, self.problem, self.repr_method)

    @optional('solution', 'problem_index', 'score_method')
    def compute_score(self):
        self.solution.set_score_method(self.score_method)
        score = self.solution.get_score()
        if self.do_show:
            fancy_print(self.solution, lines=10, title='solution ' + self.problem_index)
            print('\n\tscore =', score, '\n')

    @optional('problem_index')
    def save(self):
        if self.do_save_solution:
            self.solution.save(name=self.problem_index)

    # --- routine -----------------------------------------------------------------------

    def routine(self):
        """generator of methods to execute
                - enforces sequencing
                - returns control to user to allow interleaving code"""
        v = [self.gen_data_sets,
             self.define_problem,
             self.compute_solution,
             self.compute_score,
             self.save]

        def routine_generator():
            for method in v:
                yield method

        return routine_generator

    def run(self, min_time=0.005):
        """
        routine execution
        :param min_time: min time required that a method needs to take in order to report time (seconds)
        :return:
        """
        self.report('running Api...')
        successful = True
        for method in self.routine()():
            timer = Timer()
            try:
                self.report('calling "' + method.__name__ + '"')
                method()
            except NotImplementedError:  # handle compulsory methods
                self.report('routine aborted at "' + method.__name__ + '"')
                successful = False
                break
            except AssertionError:  # handle optional methods
                self.report('...skipping', method.__name__)
                pass
            finally:
                if self.do_report_time:
                    t = timer(method.__name__).lapse
                    # report only meaningful time
                    if t > min_time:
                        self.report_time(str(timer))
        if successful:
            self.report('Api has been successfully executed!')
        else:
            self.report('Api has been shut down due to a lack of arguments!')


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
