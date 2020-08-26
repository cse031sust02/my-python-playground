class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, sound):
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
        self.can_fly = can_fly

    def speak(self):
        super().speak('pee pee')

    def fly(self):
        if self.can_fly == True:
            print('.....{} is flying....'.format(self.name))
        else:
            print('{} can not fly!'.format(self.name))


bird_1 = Bird('Demo Bird 1', 1)
bird_1.speak()
bird_1.fly()

penguin = Bird('Penguin', 1, False)
penguin.speak()
penguin.fly()