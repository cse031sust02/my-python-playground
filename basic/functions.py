# Playing with python functions


def greet(name, msg):
    print("Hi {}! {}.".format(name, msg))


greet("Talha", "Good Morning")

# Keyword Arguments
# Python allows functions to be called using keyword arguments.

greet(msg="Good Morning", name="Talha")


# Arbitrary Arguments (*args and **kwargs)
# We use * args and **kwargs as an argument when we are unsure about
# the number of arguments to pass in the functions.
# *args = pass the variable number of non-keyword arguments
# **kwargs = pass the variable number of keyword arguments

def greet_names(*names):
    """function using * args

    names is a tuple
    """
    for name in names:
        print("Hello", name)


greet_names("Talha", "Sujon", "Alamin")


def greet_persons(**person):
    """function using ** kwargs

    person is dictionary
    """
    print("Hello Person!")
    for key, value in person.items():
        print("Your {} is {}".format(key, value))


greet_persons(name="Talha", age=32, country='BD')
greet_persons(name="Sujon", age=29, country='BD', phone="012345678")


# Lambda Function
# Lambda/Anonymous function is a function that is defined without a name.
# We can use it ife when we need a nameless function for a short period of time.

def lamda_func(x): return x * 10


five_multiply_ten = lamda_func(5)
six_multiply_ten = lamda_func(6)
print(five_multiply_ten)
print(six_multiply_ten)
