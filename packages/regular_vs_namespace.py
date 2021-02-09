# Python defines two types of packages : regular packages & namespace packages.

# Regular Package : 
# ===================
# Since Python 3.2, the __init__.py file used to be a required part of a
# package. We could not create a package without this file. We call this
# type of traditional packages as regular packages where there is a 
# __init__.py in the directory.
# 
# When a regular package is imported, this __init__.py file is implicitly
# executed, and the objects it (__init__.py file) defines are bound to names in the 
# package’s namespace.
# 
# Example:
# ----------
# Imagine the following system with three subpackages:
# 
# parent/
#     __init__.py
#     one/
#         __init__.py
#     two/
#         __init__.py
#     three/
#         __init__.py
# 
# importing parent.one will implicitly execute parent/__init__.py and
# parent/one/__init__.py.


# Namespace Package :
# =====================
# From Python 3.3 onwards, it can recognize a package even if there is no
# __init__.py file. Namespace packages were introduces in Python3. Namespace
# packages are a mechanism for splitting a single Python package across
# multiple directories on disk. If there are other modules in the same
# namespace in different paths, we can import both modules at once using
# this namespace package.
# 
# Example:
# ----------
# consider path1 and path2 as separate entries on our Python-path
# 
# path1
# +--namespace
#    +--module1.py
#    +--module2.py
# path2
# +--namespace
#    +--module3.py
#    +--module4.py
# 
# We can import modules from different paths under same namespace like below:
# from namespace import module1, module3
# src : https://stackoverflow.com/a/21819733


# Differences between namespace packages and regular packages :
# =============================================================
# The main difference are: 
# - Regular packages have __init__.py module but namespace package do not have it.
# - namespace packages can automatically span multiple path segments.
# for more details:
# https://www.python.org/dev/peps/pep-0420/#differences-between-namespace-packages-and-regular-packages

# src : 
# - https://www.python.org/dev/peps/pep-0420/
# - https://docs.python.org/3/reference/import.html#regular-packages
# - https://stackoverflow.com/questions/21819649/namespace-vs-regular-package/21819733#21819733
# - http://peak.telecommunity.com/DevCenter/setuptools#namespace-packages