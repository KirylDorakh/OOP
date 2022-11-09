class SomeClass:
    attr1 = 42

    def method1(self, x):
        return 2 * x


obj = SomeClass()
result = obj.method1(6)
print(result)
print(obj.__dict__)
