class Mamma:

    def move(self):
        print('Move')


class Hare(Mamma):

    def move(self):
        print('Jump')


animal = Mamma()
animal.move()
hare = Hare()
hare.move()


# super
class Parent:
    def __init__(self):
        print('Parent init')

    def method(self):
        print('Parent method')


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

    def method(self):
        super(Child, self).method()


child = Child()
child.method()
