# Dunder methods (also known as magic methods) in Python are the methods
# having two prefix and suffix underscores in the method name. Dunder is
# the short form of “double under (Underscores)”
#
# example :  __init__, __add__, __len__, __repr__

class Employee:

    def __init__(self, name, emp_id, phone):
        """the __init__ dunder method

        this is the contructor to initialize new objects
        """
        self.name = name
        self.emp_id = emp_id
        self.phone = phone

    def __repr__(self):
        """the __repr__ dunder method

        This method is used to return the “official” string representation
        of an object. This is we you would make an object of the class.
        
        The goal of __repr__ is to be unambiguous

        >>> emp = Employee('Talha', '0001', '015000000')
        >>> repr(emp)
        "Employee('Talha', '0001', '015000000')"
        """
        return "Employee('{}', '{}', '{}')".format(self.name, self.emp_id, self.phone)

    def __str__(self):
        """the __str__ dunder method

        This method is used to return “informal” or nicely printable string
        representation of an object. This is for the enduser.

        The goal of __repr__ is to be readable

        >>> emp = Employee('Talha', '0001', '015000000')
        >>> str(emp)
        'Talha (ID-0001)'
        """
        return '{} (ID-{})'.format(self.name, self.emp_id)

    # If we define the __repr__ method but do not define the __str__
    # method, then when we call print(object) or str(object) it will
    # use from the __repr__ method

    # For more details about __repr__ vd __str__: 
    # please check https://stackoverflow.com/q/1436703/3158021


employee_1 = Employee('Talha', '0001', '015000000')
print(employee_1)

print(repr(employee_1))
print(str(employee_1))
