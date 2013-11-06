import itertools
import functools
import multiprocessing
import operator

processes = 5
test = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]


def m_reduce(fun, iterable, starting_value=None):
    wrapped_fun = functools.partial(reducer, fun, starting_value=starting_value)
    pool = multiprocessing.Pool(processes)
    listed_result = list(pool.map_async(wrapped_fun, list(partition(iterable, int(len(iterable) / processes)))).get())
    #Mozna pobawic sie w jakas rekurencje, ale po co.
    return functools.reduce(fun, listed_result)


def reducer(fun, iterable, starting_value=None):
    iterable_iterator = iter(iterable)

    if starting_value is None:
        try:
            result = next(iterable_iterator)
        except StopIteration:
            raise TypeError('Using reducer() with empty iterable, and no starting value.')
    else:
        result = starting_value

    for element in iterable_iterator:
        result = fun(result, element)
    return result


def partition(iterable, n):
    i = iter(iterable)
    piece = list(itertools.islice(i, n))
    while piece:
        yield piece
        piece = list(itertools.islice(i, n))


if __name__ == '__main__':
    print(m_reduce(operator.add, test))
    print(m_reduce(operator.sub, test))
    print(m_reduce(operator.xor, test))
    print(m_reduce(operator.mul, test, 1))