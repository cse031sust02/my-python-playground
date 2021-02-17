"""Proxy Pattern

What is Proxy Pattern?
------------------------
A proxy, in its most general form, is a class functioning as an interface to 
something else. [wiki]

Example
----------
In this example, We have the implementation of a door and then a proxy to secure
any doors.

References
------------
- https://github.com/kamranahmedse/design-patterns-for-humans#-proxy
"""


class Door:
    def open(self):
        print("The Door is open!")


class ProxyDoor:
    def __init__(self, password):
        self.door = Door()
        self.password = password

    def open(self):
        if self.password == 'secret':
            self.door.open()
        else:
            print("Sorry! Wrong Password")


# Using the Door class directly
door = Door()
door.open()  # The Door is open!


# Using the proxy class
secured_door1 = ProxyDoor('123')
secured_door1.open()  # Sorry! Wrong Password

secured_door2 = ProxyDoor('secret')
secured_door2.open()  # The Door is open!
