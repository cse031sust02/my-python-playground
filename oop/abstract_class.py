# What is Abstract Class?
# ===========================
#
# An abstract class is a class that defines some methods and
# properties, but ususally does not define any implementation.

# * The purpose of an abstract class is to provide an appropriate base
# class from which other classes can inherit.
# * An abstract class can not be instantiated, which means we are not
# allowed to create an object of it.
# * An abstract class can have abstract methods(methods without body)
# as well as concrete methods (normal methods with body). While creating
# subclasses, we need to override the abstract methods to provide the
# implementation.
#
#
# Example :
# ==========
#
# One real life example of an abstract class is a Vehicle class. A
# vehicle is an abstraction, whereas specific examples of vehicles are
# cars, buses and trucks etc. We will not create a “vehicle” in our
# code, but we will create cars, trucks, and other kinds of vehicles.
#
#
# Abstrac Class in Python :
# =============================

# In other OOP Languages, usually abstract classes are declared using the
# “abstract” keyword. But python does not provide builtin functionality
# for abstract classes. We have to import module abc (abstract base class).
#
#
# More details and discussions :
# ==================================
#
# - https://www.youtube.com/watch?v=UDmJGvM-OUw
# - https://www.python4networkengineers.com/posts/python-beginner/abstract_classes_in_python/


from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car started!")

    def stop(self):
        print("Car stopped!")


class Truck(Vehicle):

    def start(self):
        print("Truck started!")

    def stop(self):
        print("Truck stopped!")


# We are notallowed to create an object of Vehicle Class
# my_vehicle = Vehicle() # <- will throw TypeError

my_car = Car()
my_car.start()
my_car.stop()

my_truck = Truck()
my_truck.start()
my_truck.stop()
