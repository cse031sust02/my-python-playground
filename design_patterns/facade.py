"""Facade Pattern

What is Facade Pattern?
---------------------------
Facade Pattern wraps a complicated subsystem with a simpler interface.
We can use Facade Pattern when we want to hide a complex subsystem from
our calling class. This pattern is also useful when we have legacy code to work
with. We can create a facade (wrapper) around the original classes to simplify
their usage.

Real world example
---------------------
We can turn on a computer by just pressing a button, but internally there are
lots of stuff going on. The on/off buttons serve as simple interfaces to all the
underlying procedures.

References
------------
- https://git.io/JtMlU
- https://git.io/JtMlf
"""


class Computer:

    def make_sound(self):
        print('beeeeeeeeep!')

    def show_loading_screen(self):
        print('....loading....')

    def load_everything(self):
        print('loaded everything')

    def show_welcome_message(self):
        print('welcome user!')

    def close_everything(self):
        print('closed everything')

    def pull_electricity(self):
        print('pulled electricty')
        print('zzzZZZ')


class ComputerFacade:
    def __init__(self):
        self.computer = Computer()

    def turn_on(self):
        self.computer.make_sound()
        self.computer.show_loading_screen()
        self.computer.load_everything()
        self.computer.show_welcome_message()

    def turn_off(self):
        self.computer.close_everything()
        self.computer.pull_electricity()


my_computer = ComputerFacade()
my_computer.turn_on()
my_computer.turn_off()