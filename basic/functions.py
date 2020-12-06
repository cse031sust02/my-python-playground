# A Function is some resusable code that takes inputs and does some stuff
# and then returns a result (or results)

# There are two types of functions in python
# - Built-in functions (example : print(), input(), type() etc )
# - functions which we define

def greet(name, msg):
    print("Hi {}! {}.".format(name, msg))

greet("Talha", "Good Morning")

# Note : The terms parameter and argument are used for the same thing.
# From a function's perspective :
# - A parameter is the variable listed inside the function definition.
#   - in the above example : `name` and `msg`
# - An argument is the value that we send during the function call.
#   - in the above example : 'Talha' and 'Good Morning'

# We can can send any data type (string, number, list, tuple, set,
# dictionary etc) as arguments of a function and it will be treated
# as the same data type inside the function.
# example : sending list as the argument

def my_func(params):
    print("Type of Parameter is : ", type(params))
    for item in params:
        print(item)

my_list = [1, "hello", {"name": 'test'}]
my_func(my_list)


#  Keyword Arguments
# =====================
# Python allows functions to be called using keyword arguments.

greet(msg="Good Morning", name="Talha")


#  Arbitrary Arguments (*args and **kwargs)
# ==============================================
# We use *args and **kwargs as an argument when we are unsure about
# the number of arguments to pass in the functions.

# *args :
# ---------
# - while calling the function, pass any number of non-keyword arguments
# - function will receive a tuple of arguments

def greet_names(*names):
    for name in names:
        print("Hello", name)

greet_names("Talha", "Sujon", "Alamin")

# **kwargs :
# ---------
# - while calling the function, pass any number of keyword arguments
# - function will receive a dictionary of arguments

def greet_persons(**person):
    print("Hello Person!")
    for key, value in person.items():
        print("Your {} is {}".format(key, value))

greet_persons(name="Talha", age=32, country='BD')
greet_persons(name="Sujon", age=29, country='BD', phone="012345678")


#  The return statement
# ========================
# To return any values from a function, we need to use the
# return statement.

def sum(a, b):
    return a + b

# note : discussion on return, return None, and no return
# https://stackoverflow.com/a/15300671/3158021


#  The pass statement
# ======================
# Function definitions cannot be empty, but if for any reason
# we need to have a function definition with no content, we need
# to put in the pass statement to avoid getting an error.

def my_empty_function():
    pass


#  Lambda Function
# ===================
# Lambda/Anonymous function is a function that is defined without a name.
# We can use it when we need a nameless function for a short period of time.

lamda_func = lambda x : x * 10
# the above function is similar to the below one.
# def lamda_func(x):
#     return x * 10

five_multiply_ten = lamda_func(5)
six_multiply_ten = lamda_func(6)
print(five_multiply_ten)
print(six_multiply_ten)

# example use case of lambda :
# here, we are using a lambda function as an anonymous function inside
# another function.

def myfunc(n):
    return lambda a: a * n

my_doubler = myfunc(2)
my_tripler = myfunc(3)

print(my_doubler(10))
print(my_tripler(10))
