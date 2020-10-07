# Playing with variable scope in python

# LEGB : (Local, Enclosing, Global, Built-in)


# Basic Example
# ==================

# In the example below, When we are in inner_function(), c is local
# to us, b is nonlocal and a is global.
# We can read as well as assign new values to c but can only read b
# and a from inner_function().
# src: https://www.programiz.com/python-programming/namespace

def outer_function():
    b = 20

    def inner_func():
        c = 30


a = 10


# global:
# --------
# global keyword is used to declare that a variable inside the function is
# global. If we need to read the value of a global variable, it is not
# necessary to define it as global. If we need to modify the value of a
# global variable inside a function, then we must declare it with global.
# Otherwise a local variable with that name is created.

# nonlocal:
# -----------
# very much similar to the global keyword. nonlocal is used to declare that
# a variable inside a nested function is not local to it. If we need to modify
# the value of a non-local variable inside a nested function, then we must
# declare it with nonlocal. Otherwise a local variable with that name is
# created inside the nested function.

x = 'Global X'


def outer_func():
    # to modify global x, uncomment next line
    # global x
    x = 'Outer X'

    print("From Outer Function : Before Calling Outer Function : ", x)

    def inner_func():
        # to modily outer x, uncomment next line
        # nonlocal x
        x = 'Inner X'
        print("From Inner Function : ", x)

    inner_func()

    print("From Outer Function : After Calling Outer Function : ", x)


outer_func()

print("From Root : ", x)
