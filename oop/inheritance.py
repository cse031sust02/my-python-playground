# What is Inheritance :
# ===========================
#
# Inheritance is a powerful feature in object oriented programming.
#
# If we think of inheritance in terms of biology, we can think of a
# child inheriting certain characteristic from their parent. Similarly,
# in OOP languages, child classes (or subclasses) inherit methods and
# data attributes from parent classes (or base classes).
#
# Python supports multiple inheritance (Unlike Java, PHP, C# etc) and
# multilevel inheritance.
#
#
# Advantages :
# ===================
#
# One of the key benefits of inheritance is to minimize the amount of
# duplicate code by resuing code. Inheritance also helps us to better
# organize the code in smaller and simpler units. It also represents
# real-world relationships well.
#
#
# More details/discussions :
# =============================
#
# - https://www.geeksforgeeks.org/inheritance-in-python/
# - https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3


class Animal:
    """Baseclass for all animals"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, sound):
        """An animal will speak in it's own language.
        :param sound: sound of that animal
        """
        print('{} is speaking. ({})'.format(self.name, sound))


class Cat(Animal):

    def speak(self):
        super().speak('meoooooo')


cat_1 = Cat('Demo Cat 1', 1)
cat_1.speak()

# cat_1 is a instance of Cat and Animal
print(isinstance(cat_1, Cat))
print(isinstance(cat_1, Animal))

# help(cat_1)


# The super() Function :
# =========================
# We use the super() function to get a parent method into a child
# method to make use of it.


class Bird(Animal):

    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        # Alternative way :
        # Animal.__init__(self, name, age)
        self.can_fly = can_fly

    def speak(self):
        super().speak('pee pee')

    def fly(self):
        """There are some birds which can not fly. It will check the value
        of 'can_fly' variable to determince if it can or can not fly
        """
        if self.can_fly:
            print('.....{} is flying....'.format(self.name))
        else:
            print('{} can not fly!'.format(self.name))


# Bird is a subclass of Animal
print(issubclass(Bird, Animal))
print(issubclass(Bird, Cat))

bird_1 = Bird('Demo Bird 1', 1)
bird_1.speak()
bird_1.fly()

penguin = Bird('Penguin', 1, False)
penguin.speak()
penguin.fly()


# Multiple Inheritance :
# =========================
# When a child class inherits from multiple parent classes, it is
# called multiple inheritance.

class Car:

    def run(self):
        print("I am running on road")


class Aircraft:

    def fly(self):
        print("I am flying on the sky")


class FlyingCar(Car, Aircraft):

    def start(self):
        print("I am a Flying Car!")
        self.run()
        self.fly()


my_flying_car = FlyingCar()
my_flying_car.start()
