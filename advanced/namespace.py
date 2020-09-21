
# What is Namespace :
# =====================
#
# A namespace is a simple system to control the names in a program. It
# ensures that names are unique and won’t lead to any conflict.
#
# Everything in Python is an object. We give names to objects to access
# those objects. let's look at the following statement :
x = 10
# Here, 10 is the object (of int type) stored in the memory and x is
# the name (or identifier) associated with it. we can use the statement
# below to get the address in the memory :
print(id(x))

# In a program of any complexity, we create hundreds or thousands of
# such names, each pointing to a specific object. Python keep track of
# all these names using namespace. We can imagine the Python namespace
# as a mapping of every name and their corresponding objects. Multiple
# namespaces may have the same name but pointing to a different object.
# 
# Python implements the global and local namespaces as dictionaries and
# the built-in namespace as a module. Python provides built-in functions
# called globals() and locals() that allow us to access global and local
# namespace dictionaries.
#
# Local Namespace :
# ------------------
# When a Python function is called, a new namespace is created for that
# function and it remains active until the function returns. This namespace
# covers the local names inside a function.
#
# Global Namespace :
# -------------------
# The global namespace contains any names defined at the level of the main
# program. This namespace also includes names from various imported modules.
# It will last until the program ends.
#
# Built-in Namespace :
# ----------------------
# This namespace includes the built-in functions and built-in exception
# names. It is created when the interpreter starts and will last till end.
#
# more details :
# - https://www.youtube.com/watch?v=QjBNfRJeIv0
# - https://www.programiz.com/python-programming/namespace

 
# What is a Scope :
# =====================

# In Python, the concept of scope is closely related to the namespace.
# A scope is the portion of a program from where a namespace can be
# accessed directly (without any prefix). It is a context in which
# variables exist and from which they are referenced. 
# 
# There are different scopes that can exist during the execution of 
# a program :
# - Local: It holds the list of all local names in the current function.
# - Enclosing: A scope of all the enclosing functions.
# - Global : A module level scope which takes care of all the global names.
# - Built-in : The outermost scope. It holds all the built-in names.
# 
# Scope Resolution :
# ---------------------
# When we refer to any name in our code, the interpreter starts searching
# for that given name in the innermost scope that’s local to that function.
# If the name isn’t in the local scope, then the interpreter searches in
# the enclosing function’s scope. If it is still not found, then the
# interpreter looks in the global scope and then lastly tries the built-in
# scope.
# 
# more details :
# - https://realpython.com/python-namespaces-scope
# - https://www.techbeamers.com/python-namespace-scope/


global_var = 'Global Varialbe'  # defined in global namespace


def outer_func():

    outer_var = 'Outer Variable'  # defined in local namespace

    print("----INSIDE OUTER FUNCTION---- ")
    print("LOCAL NAMESPACE  :",locals())
    print("GLOBAL NAMESPACE :",globals())
    print()

    def inner_func():

        inner_var = 'Inner Variable'  # defined in nested local namespace

        print("----INSIDE INNER FUNCTION----")
        print("LOCAL NAMESPACE  :",locals())
        print("GLOBAL NAMESPACE :",globals())
        print()

        # when we are in inner_function(),
        # - inner_var is local to us,
        # - outer_var is nonlocal and
        # - global_var is global
        #
        # we can read as well as assign new values to inner_var but
        # can only read outer_var and global_var here.

        # if we try to assign new values of global_var or outer_var,
        # it will create new local variables with those names and will
        # not change the values of original outer_var or global_var.
        # To change the original values, we need to use global or
        # nonlocal keywords to declare those variables as global or
        # nonlocal.

    inner_func()


outer_func()

# outside a function in the main program, locals() behaves the same as globals()
print("----TOP LEVEL----")
print("LOCAL NAMESPACE  :",locals())
print("GLOBAL NAMESPACE :",globals())
print()


# Importing Modules :
# =======================

# import module :
# -------------------
# This is the safest way of importing a module as we can avoid namespace
# pollution.
import datetime
print("import datetime :", dir())

# from module import * :
# ---------------------------
# It imports all the names from the given module directly in current
# namespace. Although, we can use the functions from that module
# directly (without adding the name of the module as a prefix) by
# importing in this way. By we also lose the ability to tell which
# module actually imported that function. As there can be common
# names that are defined in multiple modules.
from datetime import *
print("from datetime import * :", dir())