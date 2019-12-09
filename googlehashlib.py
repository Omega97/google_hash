from os import mkdir
from time import strftime

def raw_file_gen(name, encoding='utf8'):
    """generator, yields one line of the file (as str, in not empty, chopping \n at the end)"""
    with open(name, 'r', encoding=encoding) as file:
        for line in file:
            line = line[:-1]
            if line:
                yield line


def q_print(item, n=None):
    """print an iterator (first n elements if n is defined) """
    print()
    for i in item:
        if n is not None:
            n -= 1
            if n < 0:
                return
        print(i)


def print_dict(d):
    """pretty-print a dict"""
    for i in d.keys():
        print(f'{i:>24} : {d[i]}')


def skip_gen(gen, n):
    """skip n elements in a generator"""
    for i in range(n):
        next(gen)


def write_file(path, text, encoding='utf-8'):
    """rewrite file"""
    with open(path, 'w', encoding=encoding) as file:
        file.write(text)


def save(text, dir_name='solutions', extension='.txt'):
    """save the solution as file in the right format"""
    try:
        mkdir(dir_name)
    except FileExistsError:
        pass
    name = strftime("%Y_%m_%d %H_%M_%S")
    write_file(dir_name + '\\' + name + extension, text)


if __name__ == '__main__':
    q_print(range(10), n=5)
