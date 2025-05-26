class Adder:
    def __init__(self, data):
        self.data = data

    def add(self, x, y):
        raise NotImplementedError("Not Implemented")

    def __add__(self, other):
        return self.add(self.data, other)


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def add(self, x, y):
        new_dict = x.copy()
        new_dict.update(y)
        return new_dict


adder = Adder(None)
try:
    adder.add(1, 2)
except NotImplementedError as e:
    print(e)

list_adder = ListAdder([1, 2, 3])
print(list_adder.add([4, 5], [6, 7]))
print(list_adder + [4, 5])

dict_adder = DictAdder({"a": 1, "b": 2})
print(dict_adder.add({"c": 3}, {"d": 4}))
print(dict_adder + {"c": 3})
