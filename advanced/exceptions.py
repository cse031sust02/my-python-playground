# A Python program terminates as soon as it encounters an error. In Python,
# There are (at least) two distinguishable kinds of errors: syntax errors
# and exceptions

# Syntax Error :
# ================
# As the name suggest, syntax error is caused by wrong syntax in the code. It
# leads to the termination of the program.
# e.g. :
print('testing syntax error'  # missing right parenthesis


#  Exception :
# ==============
#
# There may be such a situation, When the program is syntactically correct,
# but still it can result in an error.
#
# for example, let's consider the following code :
#
a = 10
b = 0
print(a/b)
#
#   Output :
#   -----------
#   Traceback (most recent call last):
#       ....
#   ZeroDivisionError: division by zero
#
# We can see there is no wrong syntax in the code. But if we try to run
# it, We will see an error message. This type of error is called Exceptions.
#
# Exceptions are raised when the program is syntactically correct but the
# code resulted in an error. Exceptions come in different types, and the type
# is printed as part of the message (In our above example, it was a type of
# ZeroDivisionError). Python has many built-in exceptions. The class hierarchy
# for built-in exception can be found at the link below :
# https://docs.python.org/3/library/exceptions.html
#
# Note : Every exception in Python inherits from the base Exception class.


# Exception Handling :
# ======================
#
# In Python, exceptions can be handled using the try statement.
#
# structure :
# -------------
#    try:
#        code for critical operations (which can raise an exception) goes here.
#    except:
#        code for handling of execption
#    else:
#        code to execute if there is no exception
#    finally:
#        code to execute regardless of the result of the try and except blocks.
#
# When any exception occur, the Python interpreter stops the current process
# and passes it to the calling process until it is handled. If not handled,
# the program will crash.
#
# For example, lets say in our program we have a function A which calls
# function B. If an exception occurs in function B but is not handled in that
# function, the exception will be passed to A. If the execption is never
# handled, the program will terminate with error.

def A():

    def B():
        print('inner function code starts')
        print(10/0)
        print('inner function code ends')

    B()


print('main code starts')

try:
    print('critical code starts')
    A()
    print('critical code ends')
except Exception as e:
    print("Caught Exception : ", e)
else:
    print("here goes code for else block")
finally:
    print('here goes code for finally block')

print('main code ends')


# An except clause may name multiple exceptions as a parenthesized tuple.
# e.g. :
# ... except (RuntimeError, TypeError, NameError):
# ...     pass


# Raising an Exception :
# ========================
#
# We can also manually throw an exception using the raise keyword.
# Example :
raise
raise Exception  # shorthand for 'raise Exception()'
raise Exception("A Manual Exception")
raise ZeroDivisionError("A Manual ZeroDivisionError Exception")


# User-defined Exceptions :
# ============================
#
# Beside the built-in exceptions, We can create user-defined or custom
# exceptions by creating a new exception class.

class CustomException(Exception):
    pass


try:
    print("testing custom exception")
    raise CustomException
except CustomException:
    print("There was a exception of CustomException type!")


# for more advanced examples, please check the link below :
# https://www.programiz.com/python-programming/user-defined-exception
