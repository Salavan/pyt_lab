from functools import reduce


def avg():
    def sum(x, y):
        sum.counter += 1
        return ((sum.counter - 1) * x + y) / (sum.counter)

    sum.counter = 1.0
    return sum


def mean(l):
    return reduce(avg(), l)


print mean([1, 2, 3])
print mean([1.5, 2.5, 3.5])
print mean([1])
print mean([-2.0, 2.0, 0])

assert mean([1, 2, 3]) == 2
assert mean([1.5, 2.5, 3.5]) == 2.5
assert mean([1]) == 1
assert mean([-2.0, 2.0, 0]) == 0
