import sys
import traceback

def safe(func, *pargs, **kargs):
    try:
        return func(*pargs, **kargs)
    except Exception:
        print("Exception occurred:")
        traceback.print_exc()
        return None
