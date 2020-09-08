# Everything in Python is an object.

import sys

def a_function():
    pass

# This list contains data of different types 
# such as interger, list, dict, tuple etc
different_types = [1, "", [], {}, (), object, a_function, sys]

for a_type in different_types:
    print(type(a_type))

# We can see that all those entries are objects of different classes.