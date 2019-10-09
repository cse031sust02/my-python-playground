"""
Playing with python decorators

A decorator is a function that takes another function adds some functionality and returns it.

This is similar to packing a gift. The decorator acts as a wrapper. The nature of the object
that got decorated (actual gift inside) does not alter. But now, it looks pretty (since it got decorated).
"""


def decorated_func(original_func):
    def inner():
        print("*" * 15)
        original_func()
        print("*" * 15)
    return inner


@decorated_func
def get_me_gift():
    print("I am the gift")


# my_gift = get_me_gift
# my_gift()


"""
Multiple decorators can be chained in Python.

a function can be decorated multiple times with different (or same) decorators.
"""

def ship_func(original_func):
    def inner():
        original_func()
        print("I have been shipped")
    return inner

# it is equavalent to ship_func(decorated_func(ship_my_gift))
@ship_func
@decorated_func
def ship_my_gift():
    print("I am the gift")

my_shipped_gift = ship_my_gift
my_shipped_gift()
