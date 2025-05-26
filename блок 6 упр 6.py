import types

class Lister:
    def __str__(self):
        supes = (self.__class__.__name__, self.__class__.__bases__)
        return '<Instance of %s%s, address %s:\n' % (supes[0], supes[1], id(self)) + \
               '\n'.join(attribute + '=>' + str(getattr(self, attribute))
                         for attribute in self.__dict__) + '>'

class Super:
    def __init__(self):
        self.message = "Hello from Super"

class Sub(Super, Lister):
    def __init__(self):
        Super.__init__(self)
        self.number = 42


instance = Sub()
print(instance)


def get_superclasses(cls):
    """Returns a string representation of the class's immediate superclasses."""
    names = [base.__name__ for base in cls.__bases__]  
    return f"({', '.join(names)})"  


class MyClass:
    def __str__(self):
        """Prints class name and superclasses."""
        bases_str = get_superclasses(self.__class__)
        return f"<Instance of {self.__class__.__name__}{bases_str}, address {id(self)}>"

class A:
    pass

class B(A):
    pass

class C(B, Lister):
    def __init__(self):
        self.data = "Hello"

    def __str__(self):
        bases_str = get_superclasses(self.__class__)
        return f"<Instance of {self.__class__.__name__}{bases_str}, address {id(self)}:\n" + \
               '\n'.join(attribute + '=>' + str(getattr(self, attribute))
                         for attribute in self.__dict__) + '>'

obj = C()
print(obj)
