# Everything in Python is an object.

import sys


def a_function():
    pass


# This list contains data of different types (such as interger, list, dict,
# tuple etc)
different_types = [1, "", [], {}, (), a_function, sys, object()]

# from the below iteration, we can see that all those entries are
# objects of different classes. ie., 1 is the objet of int class
for a_type in different_types:
    print("Type : ", type(a_type))
    print("Method Resolution Order : ", type(a_type).__mro__)
    print()

# object class is the base class for all other classes. So, methods in
# object class are common to all instances of Python classes.
my_obj = object()
print(type(my_obj))
print(dir(my_obj))
print(help(my_obj))
