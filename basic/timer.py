import time
from timeit import default_timer as timer

# ---------------------------
# Normal Examples           |
# ---------------------------

# Using timeit
start = timer()
for i in range(10):
    print(i**3)
end = timer()
print("using default_timer from timeit module :", end - start)


# Using time
start_time = time.time()
for i in range(10):
    print(i**3)
end_time = time.time()
print("using time module :", end_time - start_time)

# ---------------------------
# Using Decorator           |
# ---------------------------

def timer_decorator(func):
    def inner():
        start = timer()
        func()
        end = timer()
        print("estiamted running time :", end - start)
    return inner


@timer_decorator
def do_something():
    for i in range(10):
        print(i**3)


do_something()
