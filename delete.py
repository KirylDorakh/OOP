class SomeClass:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f'Delete object {self.name}')


obj = SomeClass('John')
