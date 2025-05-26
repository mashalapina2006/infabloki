__debug__ = True  

def Public(*args):
    if not __debug__:
        return args[0]
    else:
        class Public:
            def __init__(self, wrapped):
                self.wrapped = wrapped
            def __getattr__(self, attrname):
                print('Trace:', attrname)
                return getattr(self.wrapped, attrname)
        return Public(args[0])

def Private(*args):
    if not __debug__:
        return args[0]
    else:
        class Private:
            def __init__(self, wrapped):
                self.wrapped = wrapped
            def __getattr__(self, attrname):
                print('Trace:', attrname)
                return getattr(self.wrapped, attrname)
        return Private(args[0])
