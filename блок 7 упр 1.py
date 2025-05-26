def oops():
    """Raises an IndexError exception."""
    raise IndexError("Intentional IndexError")

def catcher():
    """Calls oops and catches the IndexError exception."""
    try:
        oops()
    except IndexError as e:
        print(f"Caught an IndexError: {e}")
