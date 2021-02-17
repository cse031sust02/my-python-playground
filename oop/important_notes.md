## Basics

- Class variables are shared by all instances of the class

- Instance variables are owned by instances of the class

- In class methods, the first parameter (cls) points to the class

- In instance methods, the first parameter (self) points to the instance

- Static methods does not point to the class or instance. They are just like normal function.

## Inheritance

- Python supports multiple inheritance (Unlike Java, PHP, C# etc) and multilevel inheritance.

- Method Resolution Order (MRO) (the order in which the base classes are searched when executing a method) plays a vital role in the context of multiple inheritance.

## Encapsulation

- In Python, There are no such keywords like public, private, protected to effectively restricts access to any instance variable or method. “Private” instance variables don’t  really exist in Python. However, there are some conventions to mark the members as public, protected or private.

- We can do getter, setter in python usin @property and @method.setter

## Abstract Class

- Python does not provide builtin functionality for abstract classes and there is no “abstract” keyword like other OOP languages. To create abstract classes, We have to use the 'abc' module.

## Interface

- There’s no interface keyword in Python. We can implement interfaces in Python using ABC or other techniques.

