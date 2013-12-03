from functools import wraps
import math
import sys


def magical_decorator(decorator):
    @wraps(decorator)
    def inner(*args, **kw):
        if len(args) == 1 and not kw and callable(args[0]):
            print args[0]
            return decorator(sys.float_info.epsilon * 1000)(args[0])
        else:
            return decorator(*args, **kw)

    return inner


@magical_decorator
class deriv(object):
    def __init__(self, h):
        self.gw_method = h

    def __call__(self, fun):
        def derivative(x):
            return (fun(x + self.gw_method) - fun(x)) / self.gw_method

        return derivative


@deriv
def f(x):
    return x ** 2


@deriv(0.0001)
def g(z):
    return math.exp(z)


print f(12)
print "\n"
print g(1)