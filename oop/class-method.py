# - In class methods the first parameter (cls) points to the class
# - In instance methods, the first parameter (self) points to the instance

class Employee:

    company = "My Demo Company"

    # normal constructor
    def __init__(self, name, id):  # <- regular instance method
        self.name = name
        self.id = id

    def check_in(self):  # <- regular instance method
        print("{} (ID - {}) has checked in".format(self.name, self.id))

    @classmethod
    def set_company(cls, company_name):  # <- class method
        cls.company = company_name

    # We can use class methods as alternative constructors
    @classmethod
    def add_from_string(cls, employee_string):  # <- class method
        name, id = employee_string.split("-")
        emp = cls(name, id)
        return emp


# Using the normal constructor
emp1 = Employee("Talha", "001")
print(emp1.company)
emp1.check_in()

# Using the normal constructor
emp2 = Employee("Abbas", "002")
print(emp1.company)
emp2.check_in()

Employee.set_company("New Company")

print(emp1.company)
print(emp1.company)

# Using the alternative constructor
emp3 = Employee.add_from_string("Miaj-003")
print(emp3.__dict__)
print(emp3.company)
emp3.check_in()
