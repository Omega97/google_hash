from googlehashlib import *
from math import ceil


# ---- INPUT ------------------------------------------------------------


files = {'a': 'problems\\example.in',
         'b': 'problems\\busy_day.in',
         'c': 'problems\\mother_of_all_warehouses.in',
         'd': 'problems\\redundancy.in'}


# ---- VARIABLES ------------------------------------------------------------


# world
n_rows = 'n_rows'
n_col = 'n_col'
n_turns_max = 'n_turns_max'

# products
n_product_types = 'n_product_types'
product_weights = 'product_weights'

# warehouses
n_warehouses = 'n_warehouses'
wh_id = 'wh_id'
wh_coo = 'wh_coo'
wh_inventory = 'wh_inventory'

# orders
n_orders = 'n_orders'
order_id = 'order_id'
destination = 'destination'
item_amount = 'item_amount'
items = 'items'

# drones
n_drones = 'n_drones'
max_payload = 'max_payload'
drone_id = 'drone_id'
drone_inventory = 'drone_inventory'


# ---- DATA ------------------------------------------------------------


def refined_data():
    """generator of lists if int (from file)"""
    for i in raw_file_gen(files['a']):
        yield [int(j) for j in i.split(' ')]


def info_dict():
    """dict of all useful info of the problem"""
    out = {}
    data_gen = refined_data()
    values = next(data_gen)

    out[n_rows] = values[0]
    out[n_col] = values[1]
    out[n_drones] = values[2]
    out[n_turns_max] = values[3]
    out[max_payload] = values[4]
    out[n_product_types] = next(data_gen)[0]
    out[product_weights] = next(data_gen)
    out[n_warehouses] = next(data_gen)[0]
    skip_gen(data_gen, 2 * out[n_warehouses])
    out[n_orders] = next(data_gen)[0]
    return out


INFO = info_dict()


def gen_warehouses():
    """generator of dicts of info about warehouses"""
    data_gen = refined_data()
    skip_gen(data_gen, 4)
    for i in range(INFO[n_warehouses]):
        out = dict()
        out[wh_id] = i
        out[wh_coo] = next(data_gen)
        out[wh_inventory] = next(data_gen)
        yield out


# for I in gen_warehouses():
#     print_dict(I)
#     print()


def gen_orders():
    """generator of dicts of info about orders"""
    data_gen = refined_data()
    skip_gen(data_gen, 4 + 2 * INFO[n_warehouses] + 1)
    for i in range(INFO[n_orders]):
        out = dict()
        out[order_id] = i
        out[destination] = next(data_gen)
        out[item_amount] = next(data_gen)[0]
        out[items] = next(data_gen)
        yield out


# for I in gen_orders():
#     print_dict(I)
#     print()


# ---- COMMANDS ------------------------------------------------------------


def load(drone_id_, warehouse_id, product_id, n_items):
    assert n_items > 0
    return drone_id_, 'L', warehouse_id, product_id, n_items


def unload(drone_id_, warehouse_id, product_id, n_items):
    assert n_items > 0
    return drone_id_, 'U', warehouse_id, product_id, n_items


def deliver(drone_id_, costumer_id, product_id, n_items):
    assert n_items > 0
    return drone_id_, 'D', costumer_id, product_id, n_items


def wait(drone_id_, n_turns_waiting):
    return drone_id_, 'W', n_turns_waiting


def command_to_str(command):
    return ' '.join(str(i) for i in command)


# ----


def drone(id_, inventory=None):
    """dict of info about a drone"""
    if inventory is None:
        inventory = [0 for _ in range(INFO[n_product_types])]
    return {drone_id: id_, drone_inventory: inventory}


# ---- MAIN DATA STRUCTURES ----------------------------------------------------------------


DRONES = [drone(id_=i) for i in range(INFO[n_drones])]


WAREHOUSES = [i for i in gen_warehouses()]


# ---- ALGORITHM ------------------------------------------------------------


def dist(v1, v2):
    """Eucledian distance"""
    return sum((v1[i] - v2[i])**2 for i in range(2))**.5


def flight_time(v1, v2):
    """n turns of flight of a drone"""
    return ceil(dist(v1, v2))




SOLUTION = [load(1, 2, 2, 1)]

# --- SAVING


def save_solution(commands):
    text = str(len(commands)) + '\n'
    for i in commands:
        text += command_to_str(i) + '\n'
    save(text)


save_solution(SOLUTION)
