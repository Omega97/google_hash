
class SlideShow:
    """Solution"""
    def __init__(self, solution: list, problem: list):
        """
        :param solution: list of slides [[[1, 20]], ... , [[5]]]
        :param problem: Problem
        """
        self.value = solution
        self.photos = problem
        self.score = None

    def __repr__(self):
        return '\n'.join([str(len(self.value))] + [' '.join([str(j) for j in i]) for i in self.value])

    def __len__(self):
        return len(self.value)

    def __getitem__(self, item):
        return self.value[item]

    def __call__(self, *args, **kwargs):
        return self.value

    def get_score(self):
        """compute score if hasn't already been computed"""
        if self.score is None:
            pt = 0
            for i in range(len(self)-1):
                tags1 = sum(self.photos[j][-1] for j in self.value[i])
                tags2 = sum(self.photos[j][-1] for j in self.value[i + 1])
                a = len(tags1 & tags2)
                b = len(tags1 - tags2)
                c = len(tags2 - tags1)
                pt += min(a, b, c)
            self.score = pt
            return pt
        else:
            return self.score
