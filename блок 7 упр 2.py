class MyError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def oops():
    """Raises a MyError exception."""
    raise MyError("Intentional MyError")

def catcher():
    """Calls oops and catches MyError and IndexError exceptions."""
    try:
        oops()
    except IndexError as e:
        print(f"Caught an IndexError: {e}")
    except MyError as e:
        print(f"Caught a MyError: {e.message}")

catcher()
