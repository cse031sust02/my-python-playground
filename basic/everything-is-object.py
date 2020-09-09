# Everything in Python is an object.

import sys


def a_function():
    pass


# This list contains data of different types
# such as interger, list, dict, tuple etc
different_types = [1, "", [], {}, (), object, a_function, sys]

# from the below iteration, we can see that all those entries are
# objects of different classes. ie., 1 is the objet of int class
for a_type in different_types:
    print(type(a_type))
    # print(help(a_type))

# object class is the base class for all other classes. So, methods in
# object class are common to all instances of Python classes.
my_obj = object()
print(type(my_obj))
print(dir(my_obj))
print(help(my_obj))
