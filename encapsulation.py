class SomeClass:

    def __init__(self, value):
        self._value = value
        self.__param = 42

    def _private(self):
        print('This is method')

    # получение значения атрибута
    def getvalue(self):
        return self._value

    # установка значения атрибута
    def setvalue(self, value):
        self._value = value

    # удаление атрибута
    def delvalue(self):
        del self._value

    value = property(getvalue, setvalue, delvalue, 'Property value')


obj = SomeClass(42)
obj._private()
print(obj._SomeClass__param)
print(obj.value)
obj.value = 43
