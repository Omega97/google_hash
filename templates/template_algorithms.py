"""algorithms"""


# --- 1) Algorithms -------------------------------------------------------


def example_a(_):
    ...


def alg_1(problem):
    ...


# --- 2) Test -------------------------------------------------------

if __name__ == '__main__':
    from google_hash.example.sample_main import API

    # re-configure API
    API.set_problem('a')
    API.set_last_line(-1)
    API.set_algorithm(example_a)
    API.activate()
