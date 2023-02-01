"""# value swapping"""

a, b = 1, 5

a, b = b, a

"""# combine elements from a list"""

a = ["x", "y", "z"]

print(" ".join(a))


"""# most frequent element in a list""" 

a = [1,2,2,3,3,3,4,4,4,4]

print(max(set(a), key=a.count))

# or from Counter

from collections import Counter

cnt = Counter(a)

print(cnt.most_common(3)) # most common three


"""# if two strings are consisted of same letter regardless of the order"""

from collections import Counter

Counter(str1) == Counter(str2)

"""# string reverse"""

a = "qwertyu"

print(a[::1])

# or use iteration

for _ in reversed(a):
    print(_)


# reversing an interger

num = 123456

print(int(str(num)[::1]))

"""reverse a list"""

a = [1,2,3,4,5]

print(a[::1])

# or

for _ in reversed(a):
    print(_)

# or 

[_ for _ in reversed(a)]

"""# transpose a 2-d array"""

# https://stackoverflow.com/questions/1303347/getting-a-map-to-return-a-list-in-python-3-x
# https://stackoverflow.com/questions/4937491/matrix-transpose-in-python

og = [['a','b'], ['c','d'],['e','f']]

og_t = zip(*og)

print(list(og_t)) # [('a', 'c', 'e'), ('b', 'd', 'f')]

og_t1 = [*zip(*og)]

og_t2 = [list(i) for i in zip(*og)] # [['a', 'c', 'e'], ['b', 'd', 'f']]

og_t3 = [*map(list, zip(*og))] # [['a', 'c', 'e'], ['b', 'd', 'f']]

og_t4 = *map(list, zip(*og)), # (['a', 'c', 'e'], ['b', 'd', 'f'])

og_t4_eq = (*map(list, zip(*og)),) # comma means in element tuple

"""# chain comparison"""

b = 6

print(3<b<7)

print(1== b < 20)


"""# calling different functions with same arguments based on condition"""

def product(a,b):
    return a*b

def add(a,b):
    return a+b

_condition=True

print((product if _condition else add)(5,7))


"""# copy list - shallow"""

a = [1,2,3,4,5]

b = a 

b[0]=10 # list a is affected

print("BOTH list changes \n", "list a:", a, "\n" , "list b:", b)

"""# copy list - typecasting"""

a = [1,2,3,4,5]

b = list(a)

b[0] = 10 # does not affect list a

"""# list.copy method"""

b = a.copy()

b[0]=10 # does not affect list a


"""# copy nested list with deepcopy"""

from copy import deepcopy

nestedls = [[1,2],[3,4]]

ls2 = deepcopy(nestedls)

print(ls2)

ls2[0] = [9,10]

print(nestedls)

ls2 = nestedls.copy() # works too


"""# dict.get(): return none or default value when the key is unavailable"""

d = {'a':1, 'b':2}

print(d.get('c'))

print(d.get('c', 3))

"""# sort dictionary """

d = {'apple':10, 'orange':20, 'banana':5, 'tomato':3, 'cilantro':15}

print(sorted(d.items(), key=lambda x: x[1])) # [('tomato', 3), ('banana', 5), ('apple', 10), ('orange', 20)]

"""sort using operator.itemgetter as the sort key instead of lambda"""

from operator import itemgetter

print(sorted(d.items(), key=itemgetter(1))) # indexing a tuple

"""# sort dict keys by value"""

print(sorted(d, key=d.get))

"""# for else"""

a = [1,2,3,4,5]

for _ in a:
    if a==0:
        break
else:
    print("did not break")

"""# list to comma seprated string"""

items = ['foo', 'bar', 'xyz']

print(",".join(items))

numbers = [1,2,3,4,5]

print(",".join(map(str, numbers)))

mixed = [1,'foo', 3,4,'xyz']

print(",".join(map(str, mixed)))

"""# merge dictionary"""

d1 = {'a':1}
d2 = {'b':2}

print({**d1, **d2})

print(dict(d1.items() | d2.items()))

d1.update(d2)

print(d1)

"""# index of the min/max element"""

ls = [99, 1, 2, 50]

def minIndex(lst):
    return min(range(len(lst)), key=lst.__getitem__)

def maxIndex(lst):
    return min(range(len(lst)), key=lst.__getitem__)

print(minIndex(ls))
print(maxIndex(ls))


"""# remove duplicate items in a list"""

items = [2,2,3,3,1]

newItem2 = list(set(items))

print(newItem2)

"""# remove duplicate items in a list and preserve the order"""

from collections import OrderedDict

print(list(OrderedDict.fromkeys(items).keys()))
