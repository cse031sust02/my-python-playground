"""
Playing with python functions
"""


def add(a, b):
    return a+b


result = add(2, 3)
print(result)


"""
Python functions are first class objects

First Class Function :
------------------------
A programming language is said to have First Class Functions if it treats functions as First Class Citizen.
This means the language allows us to :
- Pass functions as arguments to another function
- Return function from another function
- Assign functions to variables


Higher Order Functions :
-------------------------
A higher order function is a function that takes a function as an argument, or returns a function.
All other functions are first-order functions.
"""


def minus(a, b):
    return a - b


def calculator(calc_func, a, b):
    result = calc_func(a, b)
    print("{} of {} and {} is : {}".format(calc_func.__name__, a, b, result))
    return result


result_add = calculator(add, 1, 2)
result_minus = calculator(minus, 10, 8)