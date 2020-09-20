#  Terminology :
# ==================
# 
# from django.utils import timezone
#   * django = library
#   * utils = package
#   * timezone = module
# 
# Module : 
# -----------
# Any python file is a module. It can have functions, classes or variables.
# 
# Packages :
# ------------
# Package is a namespace which contains multiple package/modules. Usually when
# a module becomes very big, we create a package by breaking into multiple
# modules.
# 
# Technically, a package is a Python module with an __path__ attribute.
#  
# Before Python 3.3, the __init__.py file used to be a required part of a
# package. But, Python 3.3+ treats all folders as packages, so empty 
# __init__.py files are no longer necessary. 
# src : https://stackoverflow.com/a/448279/3158021
# 
# Library :
# -----------
# Library is actually meant to be a collection of various packages. There is
# no difference between package and python library conceptually.
# more details : https://stackoverflow.com/q/19198166/3158021
# 
# The Standard Library : 
# -------------------------
# Python have a standard library which contains many built-in modules (some 
# of those modules are written in C).
# 
# Third Party modules :
# -----------------------------
# Beyond the standard library of modules packaged with Python, other developers
# have written their own modules to extend Python’s capabilities even further. 
# 
# The primary way to install third-party modules is to use Python’s pip tool.
# It securely downloads and installs Python modules onto our computer
# from PyPI (https://pypi.python.org/). PyPI (the Python Package Index), is a
# sort of free app store for Python modules.
# 
# 
# The Import System :
# =======================
# 
# The import statement is the most common way of importing codes from another
# module. There are 4 different syntaxes for writing import statements :
# - import <package>
# - import <module>
# - from <package> import <module or subpackage or object>
# - from <module> import <object>
# 
# 
# How moduleas are imported ? :
# ------------------------------
# 
# >> From Python's Official Doc :
# When a module named spam is imported, the interpreter first searches for a
# built-in module with that name. If not found, it then searches for a file
# named spam.py in a list of directories given by the variable sys.path. 
# sys.path is initialized from these locations:
# - The directory containing the input script (or the current directory when
#   no file is specified).
# - PYTHONPATH (a list of directory names, with the same syntax as the shell
#   variable PATH).
# - The installation-dependent default
# src : https://docs.python.org/3/tutorial/modules.html#the-module-search-path
# 
# We can see what is in sys.path using the following code :
import sys
print(sys.path)
# 
# 
# What happens after modules are imported?
# -----------------------------------------
# 
# When a module is imported, Python runs all of the code in the module file.
# When a package is imported, If there is a __init__.py file, Python runs all
# of the code in that __init__.py file.
# 
# I have made a demo to test these behaviours.
#
# 
# Importing * From a Package/Module :
# --------------------------------------
# 
# When we use import * statement to import a package or module, the behavior
# is different for packages and modules.
# - Package : when __all__ is not defined, import * does not import anything.
# - Module : when __all__ is not defined, import * imports everything (except
#   the names begins with an underscore)
#  
# To control the default behavior, we can define the __all__ in package and 
# module with our needs. 
# 
# src :
# - https://stackoverflow.com/q/44834/3158021
# - https://realpython.com/python-modules-packages/#importing-from-a-package
# 
# More Details :
# =================
# 
# - https://www.youtube.com/watch?v=CqvZ3vGoGs0
# - https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
# - https://realpython.com/python-import/
