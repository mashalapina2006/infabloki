class Attrs:
    def __getattribute__(self, name):
        print(f"__getattribute__: Accessing attribute {name}")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        print(f"__setattr__: Setting attribute {name} to {value}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print(f"__delattr__: Deleting attribute {name}")
        super().__delattr__(name)

    def __add__(self, other):
        print(f"__add__: Adding {self} and {other}")
        return "Result of addition"

    def __getitem__(self, key):
        print(f"__getitem__: Indexing with key {key}")
        return "Item at that index"

    def __setitem__(self, key, value):
        print(f"__setitem__: Setting item at key {key} to {value}")
        pass

    def __delitem__(self, key):
        print(f"__delitem__: Deleting item at key {key}")
        pass

    def __len__(self):
        print("__len__: Getting length")
        return 10

    def __repr__(self):
        return "Attrs Instance"


obj = Attrs()

obj.x = 10

print(obj.x)

del obj.x


result = obj + 5
print(result)

print(obj[2])

print(len(obj))

obj[2] = 5

del obj[2]
