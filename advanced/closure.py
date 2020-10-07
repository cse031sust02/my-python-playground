# A closure is the combination of a function bundled together (enclosed)
# with references to its surrounding state (the lexical environment).
# In easy words, A closure is an inner function which remember and has
# access to local variables of that inner function when it was created.

# All nested functions are not closures
# more details : https://stackoverflow.com/a/4020443


# Very Basic Closure example
def print_hi():
    msg = "Hi"

    def print_msg():
        print(msg)

    return print_msg


my_message = print_hi()
my_message()

# Another Tricky example
def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print("Total Count : ", count)

    return increment


add_up = counter()
add_up()
add_up()
