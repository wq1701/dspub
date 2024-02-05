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

# In Python, *args and **kwargs are special syntax for passing variable numbers of arguments to a function.
#
# *args is used to pass a non-keyworded, variable-length argument list. In your example, *args in the wrapper
# function will collect any positional arguments given to the greet function (though in this specific case,
# there is only one: name).
#
# **kwargs is used to pass a keyworded, variable-length argument list. In your example, **kwargs in the wrapper
# function will collect any keyword arguments given to the greet function (though in this specific case,
# there are none).
#
# Here's a breakdown of how it works in your code:
#
# The repeat function is a decorator factory that takes one argument num_times.
#
# The decorator_repeat function is the actual decorator. It takes one argument func, which is the function to be
# decorated.
#
# The wrapper function is the new function that the decorator will return. It takes any number of positional and
# keyword arguments (*args and **kwargs), which will be passed to func.
#
# Inside the wrapper function, func is called num_times times with any arguments that were passed to wrapper.
#
# The wrapper function returns the result of the last call to func.
#
# The decorator_repeat function returns wrapper.
#
# The repeat function returns decorator_repeat.
#
# When you use @repeat(num_times=3) before the greet function definition, it's equivalent to doing greet = repeat(
# num_times=3)(greet). This replaces greet with the wrapper function returned by the decorator. Now, when you call
# greet("World"), it's actually calling wrapper("World"), which in turn calls greet("World") three times.
