from time import time


def fancy_print(item, lines=8, title=''):
    """print a list or an attribute of the item (iterable)"""
    print('\n' + title + '\n')
    count = 0
    for i in item:
        count += 1
        if count > lines:
            print('...')
            break
        print(i)
    print()


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
                self.t_left = (1 - p) / speed
            else:
                self.t_left = None
            self.p = p
            self.t = t
            print(self)
