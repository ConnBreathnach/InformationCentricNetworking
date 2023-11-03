class ContentStore:
    def __init__(self, size):
        self.store = {}
        self.size = size

    def lookup(self, name):
        return self.store.get(name)

    def insert(self, name, data):
        if len(self.store) >= self.size:
            del self.store[next(iter(self.store))]
        if name in self.store:
            del self.store[name] # This just resets order of insertion, so not to delete recent ones
        self.store[name] = data
