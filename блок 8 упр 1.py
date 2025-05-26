import time
def timer(label=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            run_time = end_time - start_time
            wrapper.total_time = wrapper.total_time + run_time if hasattr(wrapper, 'total_time') else run_time
            print(f"{label}: {func.__name__} took {run_time:.4f} seconds")
            return result
        return wrapper
    return decorator

if __name__ == '__main__':
    @timer(label='[CCC]')
    def list_comprehension():
        return [x**2 for x in range(100000)]

    @timer(label='[MMM]')
    def map_function():
        return list(map(lambda x: x**2, range(100000)))

    result1 = list_comprehension()
    result2 = map_function()
    print("\nAll tests passed\n")

    class MyClass:
        @timer(label='[CLS]')
        def method(self, n):
            s = 0
            for i in range(n):
                s += i
            return s

    instance = MyClass()
    instance.method(100000)
    instance.method(200000)
    print(f"Total time spent in method: {instance.method.total_time:.4f}")
