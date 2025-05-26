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


class MyListSub(MyList):
    plus_calls = 0

    def __add__(self, other):
        print("MyListSub: Calling overloaded + operator!")
        MyListSub.plus_calls += 1
        return super().__add__(other)

    def show_plus_calls(self):
        print(f"Total + operator calls: {MyListSub.plus_calls}")


sub_list1 = MyListSub([1, 2, 3])
sub_list2 = MyListSub([4, 5, 6])

sub_list3 = sub_list1 + sub_list2
print(f"sub_list3: {sub_list3}")

sub_list1.show_plus_calls()

sub_list4 = sub_list1 + [7, 8]
print(f"sub_list4: {sub_list4}")

sub_list1.show_plus_calls()

sub_list5 = MyListSub([9, 10]) + sub_list1
print(f"sub_list5: {sub_list5}")

sub_list2.show_plus_calls()


class MyListSubInstance(MyList):
    def __init__(self, initial_value = None):
        super().__init__(initial_value)
        self.plus_calls = 0

    def __add__(self, other):
        print("MyListSubInstance: Calling overloaded + operator!")
        self.plus_calls += 1
        return super().__add__(other)

    def show_plus_calls(self):
        print(f"Total + operator calls for this instance: {self.plus_calls}")

instance_list1 = MyListSubInstance([1,2,3])
instance_list2 = MyListSubInstance([4,5,6])

instance_list3 = instance_list1 + instance_list2
print(f"instance_list3: {instance_list3}")
instance_list1.show_plus_calls()

instance_list4 = instance_list1 + [7, 8]
print(f"instance_list4: {instance_list4}")
instance_list1.show_plus_calls()

instance_list2.show_plus_calls()
