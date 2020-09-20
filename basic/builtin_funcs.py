# Built-in Functions :
# ===========================
#
# The Python interpreter has a number of built-in functions and types.
# These built-ins are always available.
#
# for the full list please check the offical link below :
# https://docs.python.org/3/library/functions.html


# Initializing different types of values in order to test the built-in
# functions on these values

my_int = 1
my_str = "Hello World"
my_list = [1, 2, 3]
my_tuple = ('a', 'b')
my_dict = {
    'name': 'Talha',
    'title': 'Software Engineer'
}


class Demo_Class:
    cls_var = 0

    def demo_method(self):
        pass


my_demo_obj = Demo_Class()


# We will now experiment some commonly used built-in functions with
# differente data types.


# type() :
# ==========
# The type function returns the (class) type of the specified object.

print(type(my_list))
print(type(my_tuple))
print(type(my_int))
print(type(my_str))
print(type(my_demo_obj))


# dir() :
# ==========

# when we pass any object as the argument, it will attempt to return
# the properties and methods (even built-in properties which are default
# for all object) for that object.

print("my_list :", dir(my_list))
print()  # to make new lines
print("my_tuple :", dir(my_tuple))
print()
print("my_int:", dir(my_int))
print()
print("my_str :", dir(my_str))
print()
print("my_demo_obj :", dir(my_demo_obj))

# If we do not pass any argument, it will return the list of names in
# the current local scope.
print(dir())


# len() :
# ===========
# It returns the length (the number of items) of an object

print(len(my_list))
print(len(my_tuple))
print(len(my_str))

# can not apply len() on integer
# print(len(my_int))

# If we want to see the length, need to implement the __len__ method
# print(len(my_demo_obj))


# repr() :
# ==========
# Returns a string containing a printable representation of an object.
# This is usually the string contains the value by what we would make
# an object of the class.

print(repr(my_list))
print(repr(my_tuple))
print(repr(my_int))
print(repr(my_str))
print(repr(my_demo_obj))  # See my experiments on OOP for better understand


# str() :
# ==========
# It returns a string version of the given object.

print(str(my_list))
print(str(my_tuple))
print(str(my_int))
print(str(my_str))
print(str(my_demo_obj))  # See my experiments on OOP for better understand


# setattr() :
# ============
# It sets the value of the specified attribute of an object.

setattr(my_demo_obj, 'cls_var', 40)


# getattr() :
# ============
# It returns the value of the specified attribute of object.
#
# If the named attribute is not present in the class, when calling
# getattr() method with a default value, it will return that default
# value.

# * when to use?
# - https://stackoverflow.com/a/55609455/3158021

attr = 'cls_var'

print(getattr(my_demo_obj, attr))  # same output as my_demo_obj.class_var

print(getattr(my_demo_obj, 'invalid_attr', 10))  # with default value


# hasattr() :
# ============
# It returns True if the object has the specificed attribute
print(hasattr(my_demo_obj, 'cls_var'))
print(hasattr(my_demo_obj, 'invalid_attr'))
