# What is Polymorphism? :
# =============================
#
# Polymorphism is derived from two Greek words: poly(many) and
# morphs(forms). So polymorphism means "many forms".

# Polymorphism gives a way to use a class exactly like its parent so
# there’s no confusion with mixing types. But each child class can
# define its own unique behavior and still share the same behavior
# of its parent class.

# More details/discussions :
# =============================
#
# - https://www.youtube.com/watch?v=P1vH3Pfw6BI
# - https://stackoverflow.com/a/11502482/3158021
# - https://www.edureka.co/blog/polymorphism-in-python/
# - https://www.programiz.com/python-programming/polymorphism

# Example :
# ===========
#
# The classic example is the Shape class and all the classes that can
# inherit from it (square, circle, etc). With polymorphism, each of
# these classes will have different underlying data. By making the
# class responsible for its code as well as its data, we can achieve
# polymorphism. Every class would have its own Draw() function and
# the client code could simply do:

# >> shape.Draw()

# src : https://stackoverflow.com/a/1031385/3158021


# Polymorphism with Functions and Objects:
# ===========================================
#
# We can create a function that can take any object, allowing for
# polymorphism.
# Let’s take an example by creating a function which will take an
# object and will do something to do that object. Here we are passing
# objects of diferrent classes but still able to call the same method
# as the Classes have that method.

class Dog:
    def desc(self):
        print("I am a Dog!")


class Cat:
    def desc(self):
        print("I am a Cat!")


def announce(animal_obj):
    animal_obj.desc()


dog1 = Dog()
cat1 = Cat()

announce(dog1)
announce(cat1)


# Polymorphism with class methods:
# =================================

# We can use the concept of polymorphism while creating class methods.
# Python allows different classes to have methods with the same name.
#
# The below example shows that, Python is using these class methods in
# a way without knowing exactly what class type each of these objects
# is. That is, Python is using these methods in a polymorphic way.

class Bangladesh:

    def say_name(self):
        print("Hi! I am bangladesh")

    def capital(self):
        print("My capital is Dhaka")


class Qatar:

    def say_name(self):
        print("Hi! I am Qatar")

    def capital(self):
        print("My capital is Doha")


bd = Bangladesh()
qt = Qatar()

for country in (bd, qt):
    country.say_name()
    country.capital()


# Polymorphism with Inheritance:
# ===================================

# Polymorphism can be carried out through inheritance, with subclasses
# making use of base class methods or overriding them.

# Method Overriding :
# ----------------------
# In OOP, Method overriding is the ability to allows a subclass to
# provide a specific implementation of a method that is already
# provided by its parent class.

# Polymorphism allows us to access these overridden methods that have
# the same name as the parent class.

class Parent:

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print("Hi! I am the {}".format(self.name))

    def show(self):
        print("I am the parent")


class Child(Parent):

    def show(self):  # <- method overriding
        print("I am the child")


p = Parent("Abu Hasan")
p.say_name()
p.show()

c = Child('Hasan Ahmed')
c.say_name()
c.show()



# Method Overloading :
# -----------------------
# Some other OOP languages have the Method Overloading feature, where
# two or more methods in one class have the same method name but
# different parameters. Python does not support method overloading.
# We can however try to achieve similar feature using *args or
# optional arguments.