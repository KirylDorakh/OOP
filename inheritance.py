class Mamma:
    className = 'Mamma'


class Horse:
    isHorse = True


class Dog(Mamma, Horse):
    species = 'Canis lupus'


dog = Dog()
print(dog.className)
print(dog.isHorse)