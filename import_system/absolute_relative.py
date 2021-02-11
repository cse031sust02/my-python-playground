# Absolute Imports :
# =======================

# An absolute import uses the full path (starting from the project’s root
# folder) to import the desired module. Absolute imports are clear and
# straightforward and we can tell exactly where the imported module is by
# looking at the statement.
# 
# Let's assume our project root folder is import_system folder.

# Here is an example of Absolute import
from basic_demo import package_a
from basic_demo.package_b.module_b import func_b


# Relative Imports :
# =======================
# A relative import uses the relative path (starting from the path of the
# current module) to import the desired module.
# 
# There are two types of relative imports: implicit and explicit. Python 3
# has disabled implicit relative imports.
# 
# Relative imports make use of dot notation to specify location. A single
# dot means that the module or package referenced is in the same directory
# as the current location. Two dots mean that it is in the parent directory
# and so on.

# some usefule links :
# - https://stackoverflow.com/q/72852/3158021
# - https://stackoverflow.com/q/12172791/3158021
# - https://www.python.org/dev/peps/pep-3122/
# - https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#absolute-vs-relative-import
# 
# More Details :
# ================
# https://realpython.com/courses/absolute-vs-relative-imports-python/