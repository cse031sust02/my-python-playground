# - Class variables are shared by all instances of the class
# - Instance variables are owned by instances of the class

# note : each method in a class automatically takes the instance
# (object) as it's first argument. Best partctise is to name the
# paramater as 'self'

class Employee:

    company = 'My Demo Company'  # <- Class variable
    total_employees = 0

    def __init__(self, first_name, last_name, dept, id, phone):
        self.first_name = first_name  # <- Instance variable
        self.last_name = last_name
        self.dep = dept
        self.id = id
        self.phone = phone

        Employee.total_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)


employee_1 = Employee('Talha', 'Imam', 'IT', 'IT-01', '011000000')
employee_2 = Employee('Abbas', 'Ali', 'Matketing', 'M-02', '012000000')

# print("Employee One's First Name :")
print(employee_1.first_name)
# print("Employee One's Company :")
print(employee_1.company)

# print("Employee Two's Company :")
print(employee_2.first_name)
# print("Employee Two's Company :")
print(employee_2.company)

# print("Employee One's Full Name :")
print(employee_1.fullname())
# note : we can do it like below,
# print(Employee.fullname(employee_1))
# Actually, that is what our code is calling behind the scene?
# It explains the self argument in the metods in the Class

# we can access the class varaible from both the class & instance
print("Accessing class variables from the class :")
print(Employee.company)
print(Employee.total_employees)

# modifying a class variable on the class namespace affects all
# the instances of the class
Employee.company = "General Company"  # <- will affect all instances
# print("Class Variable (company) :")
print(Employee.company)
# print("Employee One's Company :"")
print(employee_1.company)
# print("Employee Two's Company :")
print(employee_2.company)

# but we can change the values for any instance without affecting
# other instances :
employee_1.company = "Company 1"  # <- affects only employee_1 instance
# print("Class Variable (company) :")
print(Employee.company)
# print("Employee One's Company :")
print(employee_1.company)
# print("Employee Two's Company :")
print(employee_2.company)

# in the above example, what happened behind the scenes is a
# new 'company' variable has been added to employee_1 object.

# when we try to access a attribute of an instance, it will first
# check if the instance contains that attribute. If it does not, then
# it will check the class or any class that it inherits from  contains that attribute

# print("company attribute for the instance :")
print(employee_1.company)
# print("company attribute for the class of the instance :")
print(employee_1.__class__.company)
