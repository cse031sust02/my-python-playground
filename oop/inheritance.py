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