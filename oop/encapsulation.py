# What is Encapsulation :
# ===========================

# Encapsulation is one of the fundamentals of OOP. It is a mechanism to
# wrap up data variables and memeber functions(methods that manipualte
# the data) together into a single unit (i.e. class).

# The main idea of encapsulation is to hide data from user and to make
# sure that private data is protected from outside the class.
#
# To achieve encapsulation, each object should keeps its state private,
# inside a class. And the object manages its own state via methods. If
# anoyone want to communicate with the object, they should use the 
# methods provided.


# Encapsulation in Python :
# =============================

# In other classical OOP Languages (such as C++ and Java), They control
# the access to class members by public, private and protected keywords.
# Private members of a class are denied access from the environment
# outside the class and can be handled only from within the class.
# And protected members can be handled from the class and the
# subclasses.

# But In Python, There are no such keywords to effectively restricts
# access to any instance variable or method. “Private” instance 
# variables (that cannot be accessed from outside that class) don’t 
# really exist in Python. However, there are some conventions to mark
# the members as public, protected or private.

# Official Pythonic Guideline :
# https://www.python.org/dev/peps/pep-0008/#designing-for-inheritance

# Here are the conventions to implement Encapsulation in Pythonic way.

# public :
# ---------
# All members in a Python class are public by default. Any member can
# be accessed from outside the class environment. According to the
# Official Guideline, public members should have no leading underscores.
# Also for simple public data attributes, it is best to expose just the
# attribute name, without complicated getter/setter methods.

# protected :
# ------------
# Python's convention to make a class member protected is to add a
# single underscore (_) to it. Note that, It is just a convention,
# It is still possible to access and update the values of that member
# like public members.

# private :
# ----------
# It is another convention to use double leading underscore (__) for
# private members. It gives a strong suggestion not to touch it from
# outside the class. Any attempt to do so will also result in an
# AttributeError. Note that, double leading underscore is actually
# used for name mangling.

# more details and discussions :
# - https://stackoverflow.com/q/1641219/3158021
# - https://docs.python.org/3/tutorial/classes.html#private-variables
# - https://www.tutorialsteacher.com/python/private-and-protected-access-modifiers-in-python
# - https://www.geeksforgeeks.org/access-modifiers-in-python-public-private-and-protected

class MyClass:

    def __init__(self, pub, pro, pri):
        self.pub = pub
        self._pro = pro
        self.__pri = pri


obj = MyClass('Public Value', 'Protected Value', 'Private Value')

# We can access all the attributes but for the __pri attribute, need
# to access it as <instance>._<Class>__<attribute>
print(obj.pub)
print(obj._pro)
# print(obj.__pri) # <- throws AttributeError
print(dir(obj))  # not contains value of __pri
print(obj.__dict__)  # contains value of __pri in _MyClass__pri
print(obj._MyClass__pri)


class MySubClass(MyClass):
    pass


sub_obj = MySubClass('Public', "Protected", "Private")

# We can access all attributes from this object too
print(sub_obj.pub)
print(sub_obj._pro)
# print(sub_obj.__pri) # <- throws AttributeError
print(dir(sub_obj))  # not contains value of __pri
print(sub_obj.__dict__)  # contains value of __pri in _MyClass__pri
print(sub_obj._MyClass__pri)

# We can also update the values
sub_obj.pub = "New Public"
sub_obj._pro = "New Protected"
sub_obj._MyClass__pri = "New Private"
print(sub_obj.__dict__)


##  Getter and Setter
# ==============================

# In Object-Oriented Programming (OOP), getter and setter are two
# conventional methods that are used for retrieving and updating value
# of private attributes of a class. They allow us to control how
# important variables are accessed and updated in our code.
#
# By convention, getters start with the  word "get" and setters with
# the word "set", followed by a variable name.

class Person:

    def __init__(self, name, phone):
        self.name = name
        self.__phone = phone

    def get_phone(self):
        """getter method for getting phone number"""
        return self.__phone

    def set_phone(self, phone):
        """setter method for set phone phone number

        By using this setter method, we can be sure the phone number
        is a valid number.
        """
        if phone.isdigit():
            self.__phone = phone
        else:
            print("Invalid Phone Number")
            self.__phone = None


emp_1 = Person("Talha", '015000000')

print(emp_1.name)

# We can not access the __phone attribute directly as below:
# print(emp_1.__phone) # <- will throw error

# But we can get and set the value using the getter and setter:
print(emp_1.get_phone())
emp_1.set_phone("01abc1111")
print(emp_1.get_phone())
emp_1.set_phone("018111111")
print(emp_1.get_phone())


##  Usinng @propery, setter
# ==============================

class Employee:

    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    # @property is used to get the value of a attribute without
    # using any getter methods
    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    # @method_name.setter decorator is used to set the value of a
    # attribute without using any setter methods
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first_name = first
        self.last_name = last


emp_1 = Employee("Talha", "Imam", '015000000')
print(emp_1.fullname)
# output : Talha Imam
# If we did not use the @property decorator in fullname method, the
# output would be as below :
# <bound method Employee.fullname of <__main__.Employee object at 0x7ff649386128>>

emp_1.fullname = "Talha Ibne"
print(emp_1.fullname)
print(emp_1.first_name)
print(emp_1.last_name)
