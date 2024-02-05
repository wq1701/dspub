# In Python, a decorator is a design pattern that allows you to add new functionality to an existing object without
# modifying its structure. Decorators are usually applied to functions or methods. They are a very powerful tool,
# allowing you to "wrap" a function or method with additional code, effectively extending its behavior.

# %% Here's a simple example of a decorator:
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


# In this example, my_decorator is a function that takes another function as its argument. The wrapper function
# inside my_decorator is a new function that calls the original function (func) and adds some behavior before and
# after the call. The @my_decorator line is syntactic sugar for say_hello = my_decorator(say_hello).


# %% Here's a more complex example, where the decorator takes arguments and the decorated function also takes arguments:

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet("World")


# In this example, repeat is a decorator factory that takes an argument num_times and returns a decorator. The greet
# function is decorated by @repeat(num_times=3), so when you call greet("World"), it will print "Hello World" three
# times.

# ---------------------------------------------------------------------------------------------------------------------
# %% Side note
#
# A decorator typically takes one function as input and returns a new function. However, you can create
# a decorator that works with two (or more) functions by making a decorator factory, which is a function that returns
# a decorator. Here's an example:
# ---------------------------------------------------------------------------------------------------------------------

def my_decorator_factory(func2):
    def my_decorator(func1):
        def wrapper(*args, **kwargs):
            print("Before func1")
            result1 = func1(*args, **kwargs)
            print("After func1, before func2")
            result2 = func2(*args, **kwargs)
            print("After func2")
            return result1, result2

        return wrapper

    return my_decorator


def say_hello(name):
    return f"Hello, {name}!"


def say_goodbye(name):
    return f"Goodbye, {name}!"


decorated = my_decorator_factory(say_goodbye)(say_hello)
print(decorated("John"))

# In this example, my_decorator_factory takes a function func2 and returns a decorator my_decorator. This decorator
# takes another function func1 and returns a wrapper function that calls both func1 and func2. The decorated function
# is equivalent to say_hello, but with additional behavior before, between, and after the calls to say_hello and
# say_goodbye.
# When you call decorated("John"), it will print:

# Before func1
# After func1, before func2
# After func2
# ('Hello, John!', 'Goodbye, John!')

# This is a somewhat unusual use of decorators and may not be considered good practice in all situations, as it could
# make the code harder to understand. But it demonstrates that decorators in Python are very flexible and can be
# adapted to many different needs.
