# Let's import the packages I created 
import package_a, package_b
# at this, point, we will see the below output :
# > I am running from __init__ file of Package B!
# Because package_b has a __init__.py file, so when we import package_b
# all the codes on the file will run.

# Importing a package is conceptually equivalent to importing the package’s
# __init__.py file as a module. Here is how Python will treat package A and 
# Package B. Note that : Package B contains the __init__.py file but Package
# A does not.
print() # for new line
print(package_a)
print(package_b)
print(dir()) 
# We can also access the objects in __init__ file from Package B
print(package_b.var_b_init)
package_b.func_in_init()
print()

# This code below will fail because module_a has not been imported yet :
# package_a.module_a.func_a()

# Now, lets import a module from the package A
from package_a import module_a
# at this point, we will see the below output :
# > I am running from module 1 under Package A!
# This is becuase, when a module is imported, Python runs all of the code
# in the module file.

print()
print(dir())
package_a.module_a.func_a()

# Try the following code after removing all the codes above
# from package_b import module_b
# We will see the output as below :
# > I am running from __init__ file of Package B!
# > I am running from module 1 under Package B!
# So, we can see that although we only imported module_a, Python still runs
# all of the code from the __init__ file of that package.


# Now, lets import all from the module 1
from package_a.module_a import *
print()
print(dir())