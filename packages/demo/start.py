# Regular Package : 
# ===================
# When a regular package is imported, the __init__.py file is implicitly
# executed, and the objects it defines are bound to names in the package’s
# namespace.

# Example : 
# Let's import the regular package
import regular_package
# if we want to see the global namespace, we can see that it seems like we imported the __init__
# module from the package. So it seems it is like as we imported the __init__ file directly. (??)
print(globals())
# 'regular_package': <module 'regular_package' from '....../regular_package/__init__.py'>, 

# And as the objects the __init__ file defines are bound to names in the package’s namespace (regular_package),
# We can now access the objects from the __init__ file using the package’s namespace.
print(dir(regular_package))
print(regular_package.var_in_regular_pack)


# Namespace Package :
# =====================
# now, let's import the namespace package
import namespace_package
# now if we see the global namespace, we can see that namespace_package is tread as namespace
print (globals())
# 'namespace_package': <module 'namespace_package' (namespace)>}
# As there is no __init__ file in namespace package, there is no objects bound to the package's namespace
print(dir(namespace_package))