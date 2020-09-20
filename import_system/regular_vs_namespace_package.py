# Python defines two types of packages : regular packages & namespace packages.
# 
# Regular Package : 
# ===================

# Since Python 3.2, the __init__.py file used to be a required part of a
# package. We could not create a package with it. We call this type of
# traditional packages as regular packages where there is a __init__.py
# in the directory.

# When a regular package is imported, this __init__.py file is implicitly
# executed, and the objects it defines are bound to names in the package’s
# namespace.

# Namespace Package :
# =====================
# From Python 3.3 onwards, it can recognize a package even if there is no
# __init__.py file. Namespace packages were introduces in Python3. Namespace
# packages are a mechanism for splitting a single Python package across
# multiple directories on disk. If there are other modules in the same
# namespace in different paths, we can import both modules at once using
# this namespace package. 
# 
# TODO : Need to discover more
# 
# src : 
# - https://www.python.org/dev/peps/pep-0420/
# - https://docs.python.org/3/reference/import.html#regular-packages
# - https://stackoverflow.com/questions/21819649/namespace-vs-regular-package/21819733#21819733