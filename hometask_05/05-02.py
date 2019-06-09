task = """

2. Реализовать примеры с functools - wraps и singledispatch

"""

print(task)

from functools import singledispatch
from random import randint

print("{:=^80s}".format("< 1. @singledispatch >"))

@singledispatch
def get_random(r=0, verbose=False):
    tmp = randint(0,r)
    if r:
        print("Generating random integer from zero to argument if argument is integer (otherwise get something else ^_^)")
        print("Random integer: ", tmp)
    return tmp


@get_random.register(str)
def _(r, verbose=False):
    tmp = randint(0, len(r)-1)
    if verbose:
        print("You passed string \'{}\'! Get it\'s random char!".format(r))
        print("Random char position: ", tmp)
    return r[tmp]


@get_random.register(list)
def _(r, verbose=False):
    tmp = randint(0, len(r)-1)
    if verbose:
        print("You passed list \'{}\'! Get it\'s random element!".format(r))
        print("Random list index: ", tmp)
    return r[tmp]

i = get_random(100, verbose = True)
print("i: \'{}\'".format(i))
s = get_random("The following documentation is automatically generated from the Python source files.", verbose = True)
print("s: \'{}\'".format(s))
l = get_random("The following documentation is automatically generated from the Python source files.".split(), verbose = True)
print("l: \'{}\'".format(l))

print("{:=^80s}".format("< 1. @wraps >"))

from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args):
        print("Before call: wrapped function \'{}\' was called".format(func.__name__))
        return func(*args)
    return wrapper

@decorator
def documented_function(x):
    """DOCSTRING: This function created to demonstate @wraps"""
    return "You entered {}".format(x)


print("name: ", documented_function.__name__)
print("docstring: ", documented_function.__doc__)
print("calling: ", documented_function("Some args"))