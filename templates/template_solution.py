
class Solution:
    """Solution"""
    def __init__(self, solution: list, problem: list):
        """
        :param solution: list of slides [[[1, 20]], ... , [[5]]]
        :param problem: Problem
        """
        self.value = solution
        ...
        self.score = None

    def __repr__(self):
        return ...

    def __len__(self):
        return len(self.value)

    def __getitem__(self, item):
        return self.value[item]

    def __call__(self, *args, **kwargs):
        return self.value

    def get_score(self):
        """compute score if hasn't already been computed"""
        if self.score is None:
            ...
        else:
            return self.score
