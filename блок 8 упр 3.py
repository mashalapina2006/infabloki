import functools

def validator(*validation_specs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            arg_values = {}
            arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
            for i, arg_name in enumerate(arg_names):
                if i < len(args):
                    arg_values[arg_name] = args[i]
            arg_values.update(kwargs)
            for spec in validation_specs:
                arg_name, validation_functions = spec
                if arg_name not in arg_values:
                    continue
                arg_value = arg_values[arg_name]
                if isinstance(validation_functions, list):
                  valid = True
                  for validation_function in validation_functions:
                    if not validation_function(arg_value):
                        valid = False
                        break
                  if not valid:
                    raise ValueError(f"Invalid value for argument '{arg_name}'")
                elif not validation_functions(arg_value):
                    raise ValueError(f"Invalid value for argument '{arg_name}'")
            return func(*args, **kwargs)
        return wrapper
    return decorator
