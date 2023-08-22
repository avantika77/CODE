'''Anything can be a lists
Comma separated values
In square brackets
Can be any value, and a mix of values: Integer, Float, Boolean, None, String, List, Dictionary, …
But usually they are of the same type:
Distances of astronomical objects
Chemical Formulas
Filenames
Names of devices
Objects describing attributes of a network device.
Actions to do on your data.'''

#Any layout
'''Layout is flexible
Trailing comma is optional. It does not disturb us. Nor Python.'''

more_stuff = [
  42,
  3.14,
  True,
   None,
   "boo",
    ['another', 'list'],
        {
         'a': 'Dictionary',
         'language' : 'Python',
   },
print(more_stuff)

#Lists
'''Access single element: [index]
Access a sublist: [start:end]
Creates a copy of that sublist'''
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
print(planets)   # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
print(len(planets))    # 6
print(planets[0])         # Mercury
print(type(planets[0]))   # <class 'str'>
print(planets[3])         # Mars
print(planets[0:1])       # ['Mercury']
print(type(planets[0:1])) # <class 'list'>
print(planets[0:2])       # ['Mercury', 'Venus']
print(planets[1:3])       # ['Venus', 'Earth']
print(planets[2:])        # ['Earth', 'Mars', 'Jupiter', 'Saturn']
print(planets[:3])        # ['Mercury', 'Venus', 'Earth']
print(planets[:])         # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn\ ']

#List slice with steps
''List slice with step: [start:end:step]'''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(letters[::])       # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(letters[::1])      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(letters[::2])      # ['a', 'c', 'e', 'g', 'i']
print(letters[1::2])     # ['b', 'd', 'f', 'h', 'j']
print(letters[2:8:2])    # ['c', 'e', 'g']
print(letters[1:20:3])   # ['b', 'e', 'h']

#Change with steps
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
numbers[1::2] = [0, 0, 0, 0, 0, 0]
print(x)    #  ['qqrq', 'xyz', 'dod', 'jkl']
x[1:3] = ['bla']
print(x)    #  ['qqrq', 'bla', 'jkl']
1:2] = ['elp', 'free']
print(x)    # ['qqrq', 'elp', 'free', 'jkl']
#x[1] = ['elp', 'free']
#print(x)    # ['qqrq', ['elp', 'free'], 'jkl']

#Change with steps
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
numbers[1::2] = [0, 0, 0, 0, 0, 0]
print(numbers)  # [1, 0, 3, 0, 5, 0, 7, 0, 9, 0, 11, 0]

#List assignment and list copy
x = ['apple', 'bob', 'cat', 'drone']
y = x
x[0] = 'qqrq'
print(x)    # ['qqrq', 'bob', 'cat', 'drone']
print(y)    # ['qqrq', 'bob', 'cat', 'drone']
#There is one list in the memory and two pointers to it.
#If you really want to make a copy the pythonic way is to use the slice syntax.
#It creates a shallow copy.
x = ['apple', 'bob', 'cat', 'drone']
y = x[:]
x[0] = 'qqrq'
print(x)    # ['qqrq', 'bob', 'cat', 'drone']
print(y)    # ['apple', 'bob', 'cat', 'drone']

#Deep copy
#from copy import deepcopy
x = ['apple', 'bob', 'cat', 'drone']
y = deepcopy(x)
x[0] = 'qqrq'
print(x)    # ['qqrq', 'bob', 'cat', 'drone']
print(y)    # ['apple', 'bob', 'cat', 'drone']

join
fields = ['one', 'two and three', 'four', 'five']
together = ':'.join(fields)
print(together) # one:two and three:four:five
mixed = ' -=<> '.join(fields)
mixed = ' -=<> '.join(fields)
print(mixed) # one -=<> two and three -=<> four -=<> five
another = ''.join(fields)
print(another)  # onetwo and threefourfive



