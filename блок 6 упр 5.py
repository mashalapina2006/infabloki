class MySet(set):
    def __init__(self, value=None):
        if value is None:
            super().__init__()
        elif isinstance(value, str):
            super().__init__(value)  
        else:
            super().__init__(value) 

    def __and__(self, other):
        print("__and__ called")
        return MySet(super().__and__(other))

    def __or__(self, other):
        print("__or__ called")
        return MySet(super().__or__(other))


    @staticmethod
    def intersection(*args):
        if not args:
            return MySet()  
        result = MySet(args[0])  
        for arg in args[1:]:
            if not isinstance(arg, set):
                raise TypeError("All arguments must be sets.")
            result = result & arg  
        return result

    @staticmethod
    def union(*args):
        if not args:
            return MySet()
        result = MySet(args[0])
        for arg in args[1:]:
            if not isinstance(arg, set):
                raise TypeError("All arguments must be sets.")
            result = result | arg  
        return result


# a) 
set1 = MySet({1, 2, 3, 4})
set2 = MySet({3, 4, 5, 6})

intersection_set = set1 & set2
print(f"Intersection: {intersection_set}")

union_set = set1 | set2
print(f"Union: {union_set}")

# b) 
string_set = MySet("abc")
print(f"String Set: {string_set}")  

try:
    print(string_set[0]) 
except TypeError as e:
    print(f"Error: {e}")

# c) 
print("Iterating through string_set:")
for item in string_set:
    print(item) 

# d) 
string_set = MySet("abc")
try:
    intersection = string_set & "def"
    print(f"Intersection with string: {intersection}")
except TypeError as e:
    print(f"Error: {e}") 

try:
    union = string_set | "def"
    print(f"Union with string: {union}")
except TypeError as e:
    print(f"Error: {e}") 
# e) 
set1 = MySet({1, 2, 3})
set2 = MySet({2, 3, 4})
set3 = MySet({3, 4, 5})

intersection = MySet.intersection(set1, set2, set3)
print(f"Multiple Intersection: {intersection}")

union = MySet.union(set1, set2, set3)
print(f"Multiple Union: {union}")

#f) 

class ListLikeSet(MySet):
   def __add__(self, other):
       if isinstance(other, ListLikeSet):
           return ListLikeSet(super().__or__(other))
       else:
           raise TypeError("Can only add another ListLikeSet instance")

   def __getattr__(self, name):
       if name in ('append', 'remove', 'pop', 'insert'):
           def wrapper(*args, **kwargs):
               print(f"Calling list-like method: {name}")
               return getattr(self, name)(*args, **kwargs)
           return wrapper
       raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")


list_set = ListLikeSet([1, 2, 3])
try:
  list_set.append(4)
except AttributeError as e:
   print(f"Error: {e}") 

