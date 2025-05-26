class MyList:
    def __init__(self, initial_value=None):
        if initial_value is None:
            self._data = []
        elif isinstance(initial_value, MyList):
            self._data = initial_value._data[:]
        elif isinstance(initial_value, list):
            self._data = initial_value[:]
        else:
            raise TypeError("Initial value must be a list or MyList instance.")

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __contains__(self, item):
        return item in self._data

    def __add__(self, other):
        if isinstance(other, MyList):
            return MyList(self._data + other._data)
        elif isinstance(other, list):
            return MyList(self._data + other)
        else:
            raise TypeError("Can only add MyList or list to MyList")

    def __radd__(self, other):
        if isinstance(other, list):
            return MyList(other + self._data)
        else:
            raise TypeError("Can only add list to MyList")

    def __mul__(self, other):
        return MyList(self._data * other)

    def __rmul__(self, other):
        return MyList(self._data * other)

    def __iadd__(self, other):
        if isinstance(other, MyList):
            self._data += other._data
        elif isinstance(other, list):
            self._data += other
        else:
            raise TypeError("Can only add MyList or list to MyList")
        return self

    def __imul__(self, other):
        self._data *= other
        return self

    def __repr__(self):
        return f"MyList({self._data})"

    def append(self, item):
        self._data.append(item)

    def sort(self, *args, **kwargs):
        self._data.sort(*args, **kwargs)

    def extend(self, iterable):
        self._data.extend(iterable)

    def pop(self, index=-1):
        return self._data.pop(index)

    def insert(self, index, object):
      self._data.insert(index, object)

    def remove(self, value):
        self._data.remove(value)

    def clear(self):
        self._data.clear()

    def copy(self):
        return MyList(self._data)

    def count(self, value):
        return self._data.count(value)

    def reverse(self):
        self._data.reverse()
    
    def index(self, x, start=0, end=None):
        if end is None:
           return self._data.index(x, start)
        else:
           return self._data.index(x, start, end)


my_list1 = MyList([1, 2, 3])
my_list2 = MyList(my_list1)

print(f"my_list1: {my_list1}")
print(f"my_list2: {my_list2}")

my_list1.append(4)
print(f"my_list1 after append: {my_list1}")
print(f"my_list2 after my_list1 append: {my_list2}")

print(f"Length of my_list1: {len(my_list1)}")
print(f"my_list1[0]: {my_list1[0]}")

my_list1[0] = 10
print(f"my_list1 after modification: {my_list1}")

for item in my_list1:
    print(item)

print(f"2 in my_list1: {2 in my_list1}")
print(f"5 in my_list1: {5 in my_list1}")

my_list3 = my_list1 + [5, 6]
print(f"my_list3: {my_list3}")

my_list4 = [0] + my_list1
print(f"my_list4: {my_list4}")

my_list5 = my_list1 * 2
print(f"my_list5: {my_list5}")

my_list1 += [7, 8]
print(f"my_list1 after in-place addition: {my_list1}")

my_list1 *= 2
print(f"my_list1 after in-place multiplication: {my_list1}")

print(my_list1.pop())
print(my_list1)

my_list1.sort(reverse=True)
print(my_list1)
