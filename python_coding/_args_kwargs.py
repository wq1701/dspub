# In Python, args and kwargs are special syntaxes used in function definitions to pass a variable number of arguments
# to a function.
#
# args is used to pass non-keyworded, variable-length argument list. It allows you to pass any number of positional
# arguments to the function. The syntax is to use the symbol * before the parameter name.
#
# kwargs is used to pass keyworded, variable-length argument list. It allows you to pass any number of keyword
# arguments to the function. The syntax is to use the symbol ** before the parameter name.
#
# Here are some examples:

# %% Using *args:
def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(add(3, 5, 7))  # Output: 15
print(add(1, 2, 3, 4, 5))  # Output: 15


# %% Using **kwargs:

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(Name="John", Age=25, Country="USA")


# %% You can also use *args and **kwargs in the same function:

def func(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


func(1, 2, 3, Name="John", Age=25)
