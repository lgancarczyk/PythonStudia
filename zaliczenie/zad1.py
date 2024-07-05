def log_params(func):
    def wrapper(*args, **kwargs):
        params = {**dict(zip(func.__code__.co_varnames, map(type, args))), **{k: type(v) for k, v in kwargs.items()}}
        print(f"Function '{func.__name__}' called with parameters: {params}")
        return func(*args, **kwargs)
    return wrapper

@log_params
def calculate(a, b):
    pass

calculate(12, 2)