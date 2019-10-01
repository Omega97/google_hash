"""algorithms"""
from google_hash.utils import PercentageBar
from basic.sets import Set
from random import shuffle, randrange
# local imports
from google_hash.example.sample_solution import SlideShow


def group_photos(photos: list) -> list:  # generates random solution
    """all horizontal photos get coupled together"""
    print('\n Computing solution...\n')
    hor = [i for i in range(len(photos)) if photos[i][0] == 'H']
    ver = [i for i in range(len(photos)) if photos[i][0] == 'V']
    out = [[i] for i in hor]
    for i in range(len(ver) // 2):
        out += [[ver[i * 2], ver[i * 2 + 1]]]
    shuffle(out)
    return out


def group_slides(k=20):
    """generates the algorithm"""
    def f(photos: list, slides: list) -> list:
        """find best match for each slide"""
        bar = PercentageBar(length=20)
        slides_ = Set(*slides, fast=True)
        output = [slides_[0]]
        slides_ -= slides_[0]
        while len(slides_):
            # pick k random (available) slides
            if k >= len(slides_):
                sub_set = slides_
            else:
                sub_set = Set(slides_[0], fast=True)
                for _ in range(k):
                    sub_set += slides_[randrange(0, len(slides_))]
            # scores of last slide + possible next slides
            scores = [SlideShow([output[-1]] + [i], photos).get_score() for i in sub_set.elements]
            best = sub_set.elements[scores.index(max(scores))]
            output += [best]
            slides_ -= best
            bar(1-len(slides_) / len(slides))
        return output
    return f
