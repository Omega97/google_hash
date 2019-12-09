"""algorithms (optimize generation names)


warehouse = (x, y)

drone = ((x, y), (1, 2, ...))    position, payload, flying?


P = number of product types
W = number of warehouses
C = number of orders


----- INPUT ------

n_rows n_col D T L      n_rows, n_col, D drones, T deadline, L = max load of a drone (same 4 every drones)
P   P = number of product types
W0 W1 W2    weights of each product
W   W = number of warehouses
x y     warehouse 1 location
n1 n2 n3    number of items of product 0/1/2
x y     warehouse 2 location
n1 n2 n3    number of items of product 0/1/2
x y     warehouse 3 location
n1 n2 n3    number of items of product 0/1/2


x y     position
n1 n2 n3    list of P numbers describing amount of each product


C number of orders

3 1 2 ...   ID type of product



----- OUTPUT -----

Q = number of commands (al più un'azione / drone / turno) commands in chronological order

drone ID, command


wait
drone_ID W tempo


score = (T - t)/T * 100
all drones start at (0, 0)


----- data -----



"""


def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**.5


def turns_to_fly(p1, p2):
    return 0 if p1 == p2 else round(dist(p1, p2)) + 1


# --- 1) Algorithms -------------------------------------------------------


def example_a(_):
    return [9,
           [0, 'L', 0, 0, 1],
           [0, 'L', 0, 1, 1],
           [0, 'D', 0, 0, 1],
           [0, 'L', 1, 2, 1],
           [0, 'D', 0, 2, 1],
           [1, 'L', 1, 2, 1],
           [1, 'D', 2, 2, 1],
           [1, 'L', 0, 0, 1],
           [1, 'D', 1, 0, 1]]


def alg_1(problem):
    ...


# --- 2) Test -------------------------------------------------------

if __name__ == '__main__':
    from competition2019.sample_main import API

    # re-configure API
    API.set_problem('a')
    API.set_last_line(-1)
    API.set_algorithm(example_a)
    API.run()
