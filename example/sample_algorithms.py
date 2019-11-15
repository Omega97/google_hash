"""algorithms"""
from numpy import argmax


# --- 0) Data structures -------------------------------------------------

def data_structures():
    """this method is not actually used"""

    # problem:
    _ = [
        ['H', 3, {'cat', 'beach', 'sun'}],
        ['V', 2, {'selfie', 'smile'}],
        ...]

    # solution:
    _ = \
        [[0], [3], [1, 2], ...]


# --- 1) Algorithms -------------------------------------------------------


def example_a(_):
    return [[0], [3], [1, 2]]


def alg_1(problem):
    out = []
    v = []
    for i in range(len(problem)):
        if problem[i][0] == 'H':
            out += [[i]]
        else:
            v += [i]
            if len(v) == 2:
                out += [v]
                v = []
    return out


def alg_2(size=10):
    def wrapper(problem):
        def local_score(slide1, slide2):
            tags1 = sum([problem[j][-1] for j in slide1])  # sum the tags of all the photos
            tags2 = sum([problem[j][-1] for j in slide2])  # sum the tags of all the photos
            a = len(tags1 & tags2)  # A & B
            b = len(tags1 - tags2)  # A - B
            c = len(tags2 - tags1)  # B - A
            return min(a, b, c)

        def pick_best_and_drop(collection_, out_):
            if len(out):
                scores = [local_score(out_[-1], j) for j in collection_]
                best = int(argmax(scores))
            else:
                best = 0
            out_.append(collection[best])
            collection_ = collection_[:best] + collection_[best + 1:]
            return collection_, out_

        # group photos into slides
        sol0 = alg_1(problem)
        out = []
        collection = []     # list of slides

        for i in sol0:
            collection.append(i)
            if len(collection) > size:
                collection, out = pick_best_and_drop(collection, out)
        while len(collection):
            collection, out = pick_best_and_drop(collection, out)

        return out
    return wrapper


# --- 2) Test -------------------------------------------------------

if __name__ == '__main__':
    from google_hash.example.sample_main import API

    # re-configure API
    API.set_problem('b')
    API.set_last_line(-1)
    API.set_algorithm(alg_2(size=5))
    API.activate()
