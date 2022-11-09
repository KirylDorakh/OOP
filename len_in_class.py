class Collection:

    def __init__(self, names):
        self.names = names

    def __len__(self):
        return len(self.names)


collection = Collection(['Il', 'Lil', 'Am'])
print(len(collection))
