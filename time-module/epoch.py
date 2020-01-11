# January 1, 1970 UTC
import time
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(func(*args, **kwargs))
    return wrapper

@my_decorator
def determine_system_epoch():
    return time.gmtime(0)

@my_decorator
def time_in_secs():
    return time.time()

@my_decorator
def time_in_nanosecs():
    return time.time_ns()

@my_decorator
def time_str():
    return time.ctime(time_in_secs())

if __name__ == "__main__":
    determine_system_epoch()
    time_in_secs()
    time_in_nanosecs()
    time_str()