from time import time


def func_timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        print(time() - start)
        return res

    return wrapper
