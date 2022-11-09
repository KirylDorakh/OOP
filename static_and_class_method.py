# static method
class SomeClass:
    @staticmethod
    def hello():
        print('Hello, world')


SomeClass.hello()
obj = SomeClass()
obj.hello()


# class method
class AnotherClass:
    @classmethod
    def hello(cls):
        print('Hello, class {}'.format(cls.__name__))


AnotherClass.hello()
